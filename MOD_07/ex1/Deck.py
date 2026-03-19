# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 23:17:46 by amamun          #+#    #+#               #
#  Updated: 2026/03/19 23:34:49 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ArtifactCard import ArtifactCard
from SpellCard import SpellCard
from typing import List
from random import shuffle

class Deck:
    def __init__(self) -> None:
        self.cards_list: List[Card] = []
    
    def add_card(self, card: Card) -> None:
        self.cards_list.append(card)
    
    def remove_card(self, card: Card) -> bool:
        try:
            self.cards_list.remove(card)
            return True
        except ValueError as err:
            return False
    
    def shuffle_cards(self) -> None:
        shuffle(self.cards_list)
    
    def draw_card(self) -> Card:
        
        