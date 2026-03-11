# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 00:13:15 by amamun          #+#    #+#               #
#  Updated: 2026/02/24 19:06:48 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def create_pos(pos: tuple) -> tuple:
    print(f"Position created: {pos}")
    return pos


def distance(pos1: tuple, pos2: tuple) -> None:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    dis: float = math.sqrt((x2 - x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {pos1} and {pos2}: {dis:.2f}")
    print()


def parse(position: str, origin) -> None:
    pos: list = position.split(',')
    try:
        x1 = int(pos[0])
        x2 = int(pos[1])
        x3 = int(pos[2])
        pos_tuple: tuple = (x1, x2, x3)
        print(f"Parsing coordinates: \"{position}\"")
        print(f"Parsed position: {pos_tuple}")
        distance(origin, pos_tuple)
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{position}\"")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        print()


def unpacking_demonstration(position) -> None:
    x, y, z = position
    print(f"Player at x={x}, y={y}, z= {z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    position = create_pos((10, 20, 5))
    distance(origin, position)
    position2: str = "3, 4, 0"
    parse(position2, origin)
    position3: str = "abc,def,ghi"
    parse(position3, origin)
    unpacking_demonstration(position)


if __name__ == "__main__":
    main()
