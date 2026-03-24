# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameStrategy.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 21:44:31 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 21:47:41 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod

class GameStrategy(ABC):
    
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass
    
    @abstractmethod
    def get_strategy_name(self) -> str:
        pass
    
    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
    