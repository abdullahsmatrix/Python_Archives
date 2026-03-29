# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 21:48:19 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:46:47 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int | float, rarity: str) -> None:
        self.name: str = name
        if not isinstance(cost, (int, float)) or cost < 0:
            raise ValueError("Invalid cost type or negative!")
        self.cost: int | float = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_stat: dict[str, object]) -> dict[str, object]:
        pass

    def get_card_info(self) -> dict[str, object]:
        card_info: dict[str, object] = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False
