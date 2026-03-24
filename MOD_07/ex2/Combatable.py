# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Combatable.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 18:57:11 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 19:06:20 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod

class Combatable(ABC):
    
    @abstractmethod
    def attack(self, target: int) -> dict:
        pass
    
    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass
    
    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass