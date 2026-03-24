# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 22:26:28 by amamun          #+#    #+#               #
#  Updated: 2026/03/24 17:16:48 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    try:
        creature_card = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        print(creature_card.get_card_info())
    except ValueError as err:
        print(err)
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(6)}")
    print(f"Play result: {creature_card.play({})}")
    
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creature_card.attack_target('Goblin Warrior')}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}")
    print("Abstract pattern successfully demonstrated!")
    
if __name__ == "__main__":
    main()