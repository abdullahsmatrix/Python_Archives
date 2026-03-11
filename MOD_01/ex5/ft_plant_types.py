#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 16:51:57 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 19:44:48 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plants:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name: str = name
        self.__age: int = 0
        self.__height: int = 0
        self.__set_age(age)
        self.__set_height(height)

    def __set_height(self, height: int) -> None:
        if height > 0:
            self.height = height
        else:
            print("Invalid Height")

    def __set_age(self, age: int) -> None:
        if age > 0:
            self.age = age
        else:
            print("Invalid Age")


class Flower(Plants):
    def __init__(self, name: str, age: int, height: int,
                 color: str) -> None:
        super().__init__(name, age, height)
        self.color: str = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully\n")


class Tree(Plants):
    def __init__(self, name: str, age: int, height: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, age, height)
        self.trunk_diameter: int = trunk_diameter
        print(f"{self.name} (Tree): {height}cm, {age} days, "
              f"{trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetables(Plants):

    def __init__(self, name: str, age: int, height: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, age, height)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} "
              f"days, {self.harvest_season} season")
        msg: str = f"{self.name} is rich in vitamin {self.nutritional_value}"
        print(f"{msg}\n")


def main() -> None:
    rose: Flower = Flower("Rose", 30, 25, "red")
    rose.bloom()
    tulip: Flower = Flower("Tulip", 20, 30, "purple")
    tulip.bloom()
    oak: Tree = Tree("Oak", 1825, 500, 50)
    oak.produce_shade()
    mango: Tree = Tree("Mango", 1800, 600, 60)
    mango.produce_shade()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    main()
