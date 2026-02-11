#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 20:10:19 by amamun          #+#    #+#               #
#  Updated: 2026/02/03 19:59:48 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
class Plants:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
    def get_info(self):
        return f"Created: {self.name} ({self.starting_height}cm, {self.starting_age} days old)"

def main():
    plant_object = [
        Plants("Rose", 25, 30),
        Plants("Oak", 200, 365),
        Plants("Cactus", 5, 90),
        Plants("Sunflower", 80, 45),
        Plants("Fern", 15, 120)
    ]

    total_plant = 0
    for _ in plant_object:
        total_plant += 1
    for i in plant_object:
        print(i.get_info())
    print(f"Total plants created: {total_plant}")

if __name__ == "__main__":
    main()