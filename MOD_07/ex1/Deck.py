# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 23:17:46 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:46:47 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.Card import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.cards_list: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards_list.append(card)

    def remove_card(self, card: Card) -> bool:
        try:
            self.cards_list.remove(card)
            return True
        except ValueError:
            return False

    def shuffle_cards(self) -> None:
        shuffle(self.cards_list)

    def draw_card(self) -> Card | None:
        if not self.cards_list:
            return None
        return self.cards_list.pop()

    def get_deck_status(self) -> dict[str, object]:
        creature_card: int = 0
        artifact_card: int = 0
        spell_card: int = 0
        total_cost: int = 0
        for i in self.cards_list:
            if isinstance(i, CreatureCard):
                creature_card += 1
            elif isinstance(i, ArtifactCard):
                artifact_card += 1
            elif isinstance(i, SpellCard):
                spell_card += 1
            total_cost += i.cost

        total_cards: int = len(self.cards_list)
        avg: float = total_cost / total_cards if self.cards_list else 0.0
        return {
            "total_cards": total_cards,
            "creatures": creature_card,
            "spells": spell_card,
            "artifacts": artifact_card,
            "avg_cost": round(avg, 2)
        }
