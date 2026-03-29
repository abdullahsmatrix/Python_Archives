# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Rankable.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 20:43:06 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:45:56 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod


class Rankable(ABC):

    @abstractmethod
    def calculate_rating(self) -> int:
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        ...

    @abstractmethod
    def get_rank_info(self) -> dict:
        ...
