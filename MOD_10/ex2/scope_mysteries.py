# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 21:42:43 by amamun          #+#    #+#               #
#  Updated: 2026/04/15 23:21:44 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from typing import Callable, Dict


def mage_counter() -> Callable:
    count: int = 0

    def function_counter() -> int:
        nonlocal count
        count += 1
        return count
    return function_counter


def spell_accumulator(initial_power: int) -> Callable:
    current_power: int = initial_power

    def power_accumulator(amount: int) -> int:
        nonlocal current_power
        current_power += amount
        return current_power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment_name(enchantment_name: str) -> str:
        return f"{enchantment_type} {enchantment_name}"
    return enchantment_name


def memory_vault() -> Dict[str, Callable]:
    vault: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("Testing mage counter...")
    my_counter: Callable = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {my_counter()}")

    print("\nTesting enchanment factory...")
    my_enchantment1: Callable = enchantment_factory("Flaming")
    my_enchantment2: Callable = enchantment_factory("Frozen")
    print(my_enchantment1("Sword"))
    print(my_enchantment2("Shield"))

    print("\nTesting spell accumulator...")
    current_power: int = 10
    my_accumulator: Callable = spell_accumulator(current_power)
    print(f"Current power: {current_power}, accumulated:{my_accumulator(5)}")

    print("Testing memory vault...")
    vault: dict = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
