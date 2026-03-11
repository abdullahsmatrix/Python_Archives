# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/21 21:02:36 by amamun          #+#    #+#               #
#  Updated: 2026/02/27 23:16:08 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def command_quest() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguement received: {len(sys.argv) - 1}")

    print(f"Program name: {sys.argv[0]}")
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
