# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 21:55:40 by amamun          #+#    #+#               #
#  Updated: 2026/03/18 22:38:09 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health can't be negtive! Defaulting to 0")
            self.health = 0
        else:
            self.health = health
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack cannot be negative! Defaulting to 0")
            self.attack = 0
        else:
            self.attack = attack
    
    def get_card_info(self) -> dict:
        card_info: dict = super().get_card_info()
        card_info['type'] = 'Creature'
        card_info['attack'] = self.attack
        card_info['health'] = self.health
    
    def play(self, game_stat: dict) -> dict:
        

    def attack_target(self, target) -> dict:
        pass