#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 19:07:32 by amamun          #+#    #+#               #
#  Updated: 2026/02/11 22:24:55 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def grow(self, amount = 1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name,height)
        self.color = color
    def speciality(self):
        print(f", {self.color.lower()} flowers (blooming)")

    def grow(self, amount = 1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def grow(self, amount = 1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")
    
    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            if isinstance(plant, Plant):
                plant._Plant__grow()
            else:
                plant.grow()
            self.total_growth += 1
        
        
def main():
    alice_garden = Garden("Alice")
    bob_garden = Garden ("Bob")
    
    oak = Plant("Oak", 0)
    rose = FloweringPlant("Rose", 0, "red")
    sunflower = PrizeFlower("Sunflower", 0, "yellow", 0)
    
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print("\n")
    alice_garden.help_plants_grow()

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    main()