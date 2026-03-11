# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 22:46:56 by amamun          #+#    #+#               #
#  Updated: 2026/02/21 15:40:36 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class InvalidPlantError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class WaterError(GardenError):
    pass


class ResourceError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name: str, water_level: str,
                  sunlight_hours: str) -> None:
        if name is None or not isinstance(name, str) or name.strip() == "":
            raise InvalidPlantError("Plant name cannot be empty!")

        if not (2 <= sunlight_hours <= 12):
            level = 'low (min 2)' if sunlight_hours < 2 else 'high (max 12)'
            raise SunlightError(
                f"Plant '{name}': Sunlight hours {sunlight_hours} is "
                f"too {level}"
            )
        if not (1 <= water_level <= 10):
            level = 'low (min 1)' if water_level < 1 else 'high (max 10)'
            raise WaterError(
                f"Plant '{name}': Water level {water_level} is "
                f"too {level}"
            )
        self.plants[name] = {
            "water level": water_level,
            "sunlight hours": sunlight_hours
        }
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise ResourceError("No plant added to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name):
        if name not in self.plants:
            raise GardenError(f"Plant {name} does not exist")
        plant = self.plants[name]
        if plant["water level"] > 10 or plant["water level"] < 1:
            level = ('low (min 1)' if plant['water level'] < 1
                     else 'high (max 10)')
            raise WaterError(
                f"Water level {plant['water level']} is too {level}"
            )
        if plant["sunlight hours"] < 2 or plant["sunlight hours"] > 12:
            level = ('low (min 2)' if plant['sunlight hours'] < 2
                     else 'high (max 12)')
            raise SunlightError(
                f"Sunlight hours {plant['sunlight hours']} is too {level}"
            )
        print(f"{name}: healthy ", end="")
        print(f"(water level: {plant['water level']}", end=" ")
        print(f"sunlight hours: {plant['sunlight hours']})")


def test_garden_management():
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 7, 6)
        garden.add_plant("", 4, 6)
    except GardenError as e:
        print("Error adding plant: ", e)
    print()

    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenError as e:
        print("Error during watering: ", e)
    print()

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato")
        garden.check_plant_health("lettuce")
    except GardenError as e:
        print("Error checking lettuce: ", e)
    print()

    print("Testing error recovery...")
    try:
        empty_garden = GardenManager()
        empty_garden.water_plants()
    except GardenError as e:
        print("Caught GardenError: ", e)
        print("System recovered and continueing...\n")
    print("Garden management system test complete")


if __name__ == "__main__":
    test_garden_management()
