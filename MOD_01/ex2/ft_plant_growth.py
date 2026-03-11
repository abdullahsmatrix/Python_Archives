#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 15:51:39 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 19:37:16 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    initial_height: int = rose.height
    print("=== Day 7 ===")
    for i in range(1, 7):
        rose.grow()
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")


if __name__ == "__main__":
    main()
