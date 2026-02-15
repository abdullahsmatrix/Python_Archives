#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 19:07:32 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 17:23:34 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount=1):
        self.height += amount
        return f"grew {amount}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def speciality(self):
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager():
    total_managers = 0

    class GardenStats:
        @staticmethod  # called within class. Cannot operate on instances
        def plant_type_breakdown(plants):
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_height(plants):
            return sum(plant.height for plant in plants)

    def __init__(self):
        self.gardens = []
        GardenManager.total_managers += 1
        # each time manager is added, it increments

    def add_garden(self, garden):
        self.gardens.append(garden)

    @staticmethod
    def validate_height(height):
        return height > 0

    def show_scores(self):
        scores = {}
        for garden in self.gardens:
            scores[garden.owner] = self.GardenStats.total_height(
                garden.plants)
        return scores


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
                print(f"{plant.name} {plant.grow()}")
            else:
                print(f"{plant.name} {plant.grow()}")
            self.total_growth += 1
        print("\n")

    def get_summary(self):
        return {
            "plants": self.plants,
            "total_growth": self.total_growth,
            "count": len(self.plants)
        }

    def report(self, manager):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming), Prize points: "
                      f"{plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")

        regular, flowering, prize = (
            manager.GardenStats.plant_type_breakdown(self.plants))

        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")
        print()


def main():
    manager = GardenManager()
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    plants = [oak, rose, sunflower]
    for plant in plants:
        alice_garden.add_plant(plant)

    print()

    alice_garden.help_plants_grow()
    alice_garden.report(manager)

    # Add gardens to manager
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    print("Height validation test:",
          GardenManager.validate_height(10))
    print("Garden scores-", manager.show_scores())
    print("Total gardens managed:", len(manager.gardens))


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    main()
