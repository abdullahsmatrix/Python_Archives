# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Magical.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 19:01:01 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 21:18:58 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod

class Magical(ABC):
    
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass
    
    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
