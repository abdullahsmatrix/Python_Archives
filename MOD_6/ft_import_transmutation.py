# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 16:30:13 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 16:53:44 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion as strength
import alchemy.elements
from alchemy.elements import create_fire, create_water, create_earth


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print()
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire: {alchemy.elements.create_fire()}")
    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")
    print()
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"Strength_potion(): {strength()}")
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
