# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 22:59:38 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 18:23:11 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
    
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }
    def get_card_info(self) -> dict:
        card_info: dict = super().get_card_info()
        card_info['type'] = 'Artifact'
        return card_info
        

    def activate_ability(self) -> dict:
        pass