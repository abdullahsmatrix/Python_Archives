# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 21:50:59 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 21:00:38 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):

    def __init__(self) -> None:
        self.total_damage_dealt: int = 0
        self.cards_played: int = 0

    def execute_turn(self, hand: list[Card],
                     battlefield: list[Card]) -> dict[str, object]:
        actions: dict[str, object] = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }

        sorted_hand: list[Card] = sorted(hand, key=lambda card: card.cost)
        available_mana: int = 10

        for card in sorted_hand:
            if card.cost <= available_mana:
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
                available_mana -= card.cost
                self.cards_played += 1

                if hasattr(card, 'attack'):
                    damage: int = int(getattr(card, 'attack'))
                    damage_dealt: int = int(actions["damage_dealt"])
                    actions["damage_dealt"] = damage_dealt + damage
                    cast_targets = actions["targets_attacked"]
                    if isinstance(cast_targets, list):
                        cast_targets.append("Enemy Player")
                    self.total_damage_dealt += damage

        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[object]
                           ) -> list[object]:
        prioritized: list[object] = []

        for target in available_targets:
            if isinstance(target, str):
                if target.lower() in ["player", "enemy player"]:
                    prioritized.append(target)

        remaining = [t for t in available_targets if t not in prioritized]

        def get_health(target: object) -> float:
            if hasattr(target, 'health'):
                return float(getattr(target, 'health'))
            return float('inf')

        remaining.sort(key=get_health)
        prioritized.extend(remaining)

        return prioritized
