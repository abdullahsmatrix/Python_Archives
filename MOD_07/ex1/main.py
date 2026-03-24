# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 16:31:36 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 18:25:18 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from tools.card_generator import CardGenerator
from typing import Dict
def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    
    generator = CardGenerator()
    creature: Dict = generator.get_random_creature()
    artifact: Dict = generator.get_random_artifact()
    spell: Dict = generator.get_random_spell()

    creature_obj = CreatureCard(**creature)
    artifact_obj = ArtifactCard(**artifact)
    spell_obj = SpellCard(**spell)

    print("Building deck with different card types...")
    deck_obj = Deck()
    deck_obj.add_card(creature_obj)
    deck_obj.add_card(artifact_obj)
    deck_obj.add_card(spell_obj)
    
    print(f"Deck stats: {deck_obj.get_deck_status()}")
    
    print("Drawing and playing cards:\n")
    for i in range(len(deck_obj.cards_list)):
        deck_obj.shuffle_cards()
        card_drew = deck_obj.draw_card()
        card_type: str = card_drew.get_card_info().get("type", "None")
        print(f"Drew: {card_drew.name} ({card_type})")
        print(f"Play result: {card_drew.play({})}")
        print()
    print("Polymorphism in action: Same interface, differenr card behaviours!")

if __name__ == "__main__":
    main()