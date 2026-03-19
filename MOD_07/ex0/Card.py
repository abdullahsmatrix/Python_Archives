# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 21:48:19 by amamun          #+#    #+#               #
#  Updated: 2026/03/19 19:49:33 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name:    str, cost:  int, rarity:    str) -> None:
        self.name = name
        if not isinstance(cost, (int, float)) or cost < 0:
            raise ValueError("Invalid cost type or negative!")
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_stat:   dict) -> dict:
        pass
    
    def get_card_info(self) -> dict:
        card_info: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
            }
        return card_info
            

    def is_playable(self, available_mana:   int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False