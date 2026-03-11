#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 21:16:02 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 19:43:35 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        self.name: str = name
        self.set_height(starting_height)
        self.set_age(starting_age)

    def get_height(self) -> int:
        return self.__starting_height

    def get_age(self) -> int:
        return self.__starting_age

    def set_height(self, starting_height: int) -> None:
        if starting_height > 0:
            self.__starting_height = starting_height
        else:
            print(f"Invalid operation attempted: height "
                  f"{starting_height}cm [Rejected]")
            print("Security: Negative height rejected")

    def set_age(self, starting_age: int) -> None:
        if starting_age > 0:
            self.__starting_age = starting_age
        else:
            print(f"Invalid operation attempted: age "
                  f"{starting_age}cm [Rejected]")
            print("Security: Negative age rejected")


def main() -> None:
    plant: SecurePlant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.name}")
    print(f"Height updated: {plant.get_height()}cm [OK]")
    print(f"Age updated: {plant.get_age()}cm [OK]")
    print("\n")
    plant.set_height(-5)
    print("\n")
    print(f"Current plant: {plant.name} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    main()
