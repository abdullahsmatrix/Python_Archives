# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 19:05:02 by amamun          #+#    #+#               #
#  Updated: 2026/02/27 23:22:49 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class Inventory:
    def __init__(self, item: str, quantity: int):
        self.item = item
        self.quantity = quantity

    def percentage(self, total_items) -> float:
        return (self.quantity/total_items) * 100


def item_categories(inventory_dict: dict) -> None:
    print("=== Item Categories ===")
    total_items = sum(inventory_dict.values())
    moderate: dict = {
        k: v for k, v in inventory_dict.items()
        if Inventory(k, v).percentage(total_items) > 40
    }
    scarce: dict = {
        k: v for k, v in inventory_dict.items()
        if Inventory(k, v).percentage(total_items) <= 40
    }
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")


def inventory_statistics(inventory_dict: dict) -> None:
    print("=== Inventory Statistics ===")

    inverted_dict: dict = {v: k for k, v in inventory_dict.items()}
    most_abundant = max(inventory_dict.values())
    least_abundant = min(inventory_dict.values())
    print(
        f"Most abundant: {inverted_dict[most_abundant]} "
        f"({most_abundant} units)"
    )
    print(
        f"Least abundant: {inverted_dict[least_abundant]} "
        f"({least_abundant} units)"
    )
    print()


def current_inventory(inventory_dict: dict) -> None:
    print("=== Current Inventory ===")

    total_items = sum(inventory_dict.values())
    for key, value in inventory_dict.items():
        obj = Inventory(key, value)
        print(
            f"{key}: {value} units ({obj.percentage(total_items):.2f}%)"
        )
    print()


def sample_lookup(inventory_dict: dict, item: str) -> None:
    for k in inventory_dict.keys():
        if item == k:
            print(f"Sample lookup - '{item}' in inventory: True")


def main() -> None:
    print("=== Inventory System Analysis===")

    inventory_dict: dict = {}
    for item in sys.argv[1:]:
        key, value_str = item.split(":")
        try:
            inventory_dict[key] = int(value_str)
        except ValueError:
            print(
                "Invalid data type! Available item can only be positive "
                "number."
            )
    total_items = sum(inventory_dict.values())
    unique_items = len(inventory_dict)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print()

    current_inventory(inventory_dict)
    inventory_statistics(inventory_dict)
    item_categories(inventory_dict)

    print("=== Management Suggestions ===")
    restock: list = [k for k, v in inventory_dict.items() if v == 1]
    print(f"Restock needed: {', '.join(restock)}")

    print("=== Dictionary Properties Demo ===")
    keys: list = [k for k in inventory_dict.keys()]
    values: list = [v for v in inventory_dict.values()]
    print(f"Dictionary keys: {', '.join(keys)}")
    print(f"Dictionary values: {', '.join(str(v) for v in values)}")

    sample_lookup(inventory_dict, "sword")


if __name__ == "__main__":
    main()
