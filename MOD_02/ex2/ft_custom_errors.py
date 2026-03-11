# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 00:00:15 by amamun          #+#    #+#               #
#  Updated: 2026/02/21 15:42:33 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


def plant_error_test(temp: int) -> None:
    if temp > 40:
        raise PlantError("The tomato plant is wilting!")


def water_error_test(water_level: int) -> None:
    if water_level < 20:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing Plant Error...")
    try:
        plant_error_test(60)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print()

    print("Testing Water Error...")
    try:
        water_error_test(10)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
        print()

    print("Testing catching all garden errors...")
    try:
        plant_error_test(60)
    except (GardenError) as error:
        print(f"Caught a garden error: {error}")
    try:
        water_error_test(10)
    except (GardenError) as error:
        print(f"Caught a garden error: {error}")

    print()
    print("All custom error types worked correctly")
