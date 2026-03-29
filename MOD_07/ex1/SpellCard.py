# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 22:55:30 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:45:56 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_stat: dict[str, object]) -> dict[str, object]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }

    def get_card_info(self) -> dict[str, object]:
        card_info: dict[str, object] = super().get_card_info()
        card_info['type'] = 'Spell'
        return card_info

    def resolve_effect(self, targets: list[object]) -> dict[str, object]:
        return {
            'resolved': True,
            'targets': targets,
            'effect': self.effect_type
        }
