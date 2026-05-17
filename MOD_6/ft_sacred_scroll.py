# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 23:35:41 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 00:19:09 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


# for module level access we have to define where the module is located:
import alchemy

# for package level access we have to import exposed functions
from alchemy import create_fire, create_water


def main() -> None:
    print("=== Sacred Scroll Mastery===\n")
    print("Testin direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_air()}")
    print()
    print("Testing package level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {create_fire()}")
    print(f"alchemy.create_water(): {create_water()}")
    try:
        print(f"alchemy.create_earth(): {create_earth()}")
    except NameError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {create_air()}")
    except NameError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
