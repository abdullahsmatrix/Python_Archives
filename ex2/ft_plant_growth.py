#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 15:51:39 by amamun          #+#    #+#               #
#  Updated: 2026/02/02 20:08:27 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    initial_height = rose.height
    print("=== Day 7 ===")
    for i in range(1, 7):
        rose.grow()
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")

if __name__ == "__main__":
    main()