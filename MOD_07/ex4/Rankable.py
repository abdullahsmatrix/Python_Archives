# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Rankable.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 20:43:06 by amamun          #+#    #+#               #
#  Updated: 2026/03/25 20:44:34 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from abc import ABC, abstractmethod

class Rankable(ABC):
    
    @abstractmethod
    def calculate_rating(self):
        
    