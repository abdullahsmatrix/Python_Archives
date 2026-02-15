#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 20:10:19 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 19:43:31 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
class Plants:
    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        self.name: str = name
        self.starting_height: int = starting_height
        self.starting_age: int = starting_age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.starting_height}cm, "
              f"{self.starting_age} days old)")


def main() -> None:
    plant_object: list[Plants] = [
        Plants("Rose", 25, 30),
        Plants("Oak", 200, 365),
        Plants("Cactus", 5, 90),
        Plants("Sunflower", 80, 45),
        Plants("Fern", 15, 120)
    ]

    total_plant: int = 0
    for _ in plant_object:
        total_plant += 1
    for i in plant_object:
        i.get_info()
    print(f"Total plants created: {total_plant}")


if __name__ == "__main__":
    main()
