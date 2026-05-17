# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/04 21:35:15 by amamun          #+#    #+#               #
#  Updated: 2026/04/19 20:18:31 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from typing import Callable, List, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> tuple:
        return (base_spell(*args, **kwargs) * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def simple_damage() -> int:
        return 10

    print("\nTesting spell combiner...")
    combined: Callable = spell_combiner(fireball, heal)
    result: tuple = combined('Dragon')
    print(f"Combined spell result: {result[0]}, "
          f"{result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball: Callable = power_amplifier(simple_damage, 3)
    original: int = simple_damage()
    amplified: Any = mega_fireball()
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    is_dragon: Callable = lambda target: target == "Dragon"
    dragon_slayer: Callable = conditional_caster(is_dragon, fireball)

    print(f"Casting on Dragon: {dragon_slayer('Dragon')}")
    print(f"Casting on Goblin: {dragon_slayer('Goblin')}")

    print("\nTesting spell sequence...")
    party_buff: Callable = spell_sequence([fireball, heal])
    print(f"Sequence results: {party_buff('Knight')}")


if __name__ == "__main__":
    main()
