#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 16:51:57 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 17:18:45 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plants:
    def __init__(self, name, age, height):
        self.name = name
        self.__age = 0
        self.__height = 0
        self.__set_age(age)
        self.__set_height(height)

    def __set_height(self, height):
        if height > 0:
            self.height = height
        else:
            print("Invalid Height")

    def __set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Invalid Age")


class Flower(Plants):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully\n")


class Tree(Plants):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {height}cm, {age} days, "
              f"{trunk_diameter}cm diameter")

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetables(Plants):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} "
              f"days, {self.harvest_season} season")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")


def main():
    rose = Flower("Rose", 30, 25, "red")
    rose.bloom()
    tulip = Flower("Tulip", 20, 30, "purple")
    tulip.bloom()
    oak = Tree("Oak", 1825, 500, 50)
    oak.produce_shade()
    mango = Tree("Mango", 1800, 600, 60)
    mango.produce_shade()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    main()
