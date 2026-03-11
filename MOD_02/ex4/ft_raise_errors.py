# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 16:07:12 by amamun          #+#    #+#               #
#  Updated: 2026/02/19 22:46:00 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str,
                       water_level: str, sunlight_hours: str) -> None:
    if plant_name is None or not isinstance(plant_name, str):
        raise ValueError("Error: Invalid name\n")
    if int(water_level) > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too high (max 10)\n")
    elif int(water_level) < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too low (min 1)\n")
    if int(sunlight_hours) < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)\n")
    elif int(sunlight_hours) > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)\n")
    print(f"Plant {plant_name} is healthy!\n")


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        check_plant_health("tomato", 3, 5)
    except ValueError as exc:
        print(exc)

    print("Testing empty plant name...")
    try:
        check_plant_health(None, 3, 5)
    except ValueError as exc:
        print(exc)

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as exc:
        print(exc)

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("rose", 5, 0)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    print("=== Garden Plant Health Check ===")
    print()
    test_plant_checks()
    print()
    print("All error raising test complete!")
