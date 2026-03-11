# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally _block.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 15:32:24 by amamun          #+#    #+#               #
#  Updated: 2026/02/19 16:06:28 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
        raise
    finally:
        print("Closing watering system (cleanup)")
        print()


def test_watering_system(plants):
    try:
        water_plants(plants)
        print("Watering completed successfully!")
        print()
    except Exception:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden watering system ===\n")
    good_plants: list = ['Rose', 'Tomato', 'Lemon', 'Oak']
    bad_plants: list = ['tomato', None]
    print("Test normal watering...")
    test_watering_system(good_plants)
    print("Testing with error...")
    test_watering_system(bad_plants)
