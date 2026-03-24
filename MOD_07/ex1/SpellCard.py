# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 22:55:30 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 19:04:44 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
    
    def play(self, game_stat: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }

    def get_card_info(self) -> dict:
        card_info: dict = super().get_card_info()
        card_info['type'] = 'Spell'
        return card_info
        
    def resolve_effect(self, targets: list) -> dict:
        ...