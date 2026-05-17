# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 20:54:58 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 23:17:40 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire import record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    result1 = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {result1}')
    result2 = validate_ingredients('dragon scales')
    print(f"validate_ingredients('dragon scales'): {result2}")
    print()

    print("Testing spell recording with validation:")
    result3 = record_spell('Fireball', 'fire air')
    print(f"record_spell('Fireball', 'fire air'): {result3}")
    result4 = record_spell('Dark Magic', 'shadow')
    print(f"record_spell('Dark Magic', 'shadow'): {result4}")
    print()
    print("Testing late import technique:")
    result5 = record_spell('Lightning', 'air')
    print(f"record_spell('Lightning', 'air'): {result5}")
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
