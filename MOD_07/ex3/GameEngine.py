# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 21:52:24 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:49:04 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list[Card] = []
        self._battlefield: list[Card] = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0
        self._mana_pool: int = 10
        self._max_mana: int = 10

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy

        deck: dict[str, list[Card]] = self._factory.create_themed_deck(size=10)

        self._hand = deck['creatures'] + deck['spells'] + deck['artifacts']
        self._cards_created: int = len(self._hand)
        self._mana_pool: int = self._max_mana

    def simulate_turn(self) -> dict[str, object]:
        if self._factory is None or self._strategy is None:
            raise ValueError("Engine not configured.")

        turn_result: dict[str, object] = self._strategy.execute_turn(
            self._hand, self._battlefield)

        cards_played: list[str] = list(turn_result.get("cards_played", []))
        total_mana_spent: int = 0

        for card_name in cards_played:
            card_to_play: Card | None = None
            for card in self._hand:
                if card.name == card_name:
                    card_to_play = card
                    break

            if card_to_play:
                total_mana_spent += card_to_play.cost

                self._hand.remove(card_to_play)

                if (hasattr(card_to_play, 'attack') and
                        hasattr(card_to_play, 'health')):
                    self._battlefield.append(card_to_play)

        self._mana_pool = max(0, self._mana_pool - total_mana_spent)

        damage_dealt: int = int(turn_result.get("damage_dealt", 0))
        self._total_damage += damage_dealt

        self._turns_simulated += 1

        return {
            "turn_number": self._turns_simulated,
            "strategy": self._strategy.get_strategy_name(),
            "cards_played": cards_played,
            "mana_spent": total_mana_spent,
            "mana_remaining": self._mana_pool,
            "damage_dealt": damage_dealt,
            "hand_size": len(self._hand),
            "battlefield_size": len(self._battlefield),
            "actions": turn_result
        }

    def get_engine_status(self) -> dict[str, object]:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": (self._strategy.get_strategy_name()
                              if self._strategy else None),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
            "current_hand_size": len(self._hand),
            "battlefield_size": len(self._battlefield),
            "mana_available": self._mana_pool,
            "max_mana": self._max_mana,
            "factory_configured": self._factory is not None,
            "strategy_configured": self._strategy is not None
        }

    def get_hand(self) -> list[Card]:
        return self._hand

    def get_battlefield(self) -> list[Card]:
        return self._battlefield

    def get_supported_types(self) -> dict[str, list[str]]:
        if self._factory is None:
            raise ValueError("Engine not configured.")
        return self._factory.get_supported_types()

    def add_card_to_hand(self, card: Card) -> None:
        self._hand.append(card)

    def reset_mana(self) -> None:
        self._mana_pool = self._max_mana
