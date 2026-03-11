# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 20:24:15 by amamun          #+#    #+#               #
#  Updated: 2026/02/18 22:45:57 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
        print()

    print("Testing ZeroDivisionError...")
    try:
        result: int = 10/0
        print(result)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
        print()

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print()

    print("Testing KeyError...")
    plants = {
        "rose": "red",
        "tulip": "yellow",
    }
    try:
        print(plants["missing_plant"])
    except KeyError as error:
        print(f"Caught KeyError: {error}")
        print()

    print("Testing multiple errors together...")
    try:
        value: int = int("abc")
        result: int = value / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
        print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
