# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 21:08:55 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:46:47 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.Card import Card
from ex2.Elitecard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main() -> None:
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    Card_methods: list = [
        method for method in Card.__dict__
        if not method.startswith("_")]
    Magical_methods: list = [
        method for method in Magical.__dict__
        if not method.startswith("_")]
    Combatable_methods: list = [
        method for method in Combatable.__dict__
        if not method.startswith("_")]
    print(f"Card: {Card_methods}")
    print(f"Combatable: {Combatable_methods}")
    print(f"Magical: {Magical_methods}")
    print()

    print("Playing Arcane Warrior (Elite Card):")
    Arcane_Warrior = EliteCard('Arcane Warrior', 4, "Legendary",
                               3, 5, 10, 8)
    print("Combat phase:")
    print(f"Attack result: {Arcane_Warrior.attack('Enemy')}")
    print(f"Defense result: {Arcane_Warrior.defend(5)}\n")

    print("Magic phase:")
    spell_result = Arcane_Warrior.cast_spell('Fireball',
                                             ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {spell_result}")
    print(f"Mana channel: {Arcane_Warrior.channel_mana(3)}\n")

    print("Multiple interface implementation succesful!")


if __name__ == "__main__":
    main()
