#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/01 17:34:03 by amamun          #+#    #+#               #
#  Updated: 2026/02/01 21:49:07 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def track_plant(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plant_object = [
        Plant('Rose', 25, 30),
        Plant('Sunflower', 80, 45),
        Plant('Cactus', 15, 120)
    ]
    for plant in plant_object:
        print(plant.track_plant())


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    main()
