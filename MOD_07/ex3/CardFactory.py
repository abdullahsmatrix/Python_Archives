# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CardFactory.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 21:47:57 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 21:50:45 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod

class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
