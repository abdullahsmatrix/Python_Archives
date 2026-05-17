# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/15 23:25:18 by amamun          #+#    #+#               #
#  Updated: 2026/04/19 20:18:41 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from typing import Callable, Any
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        msg: str = ("Invalid operation! must be 'add', 'multiply', "
                    "'max' or 'min'")
        raise KeyError(msg)
    valid_op: Callable = operations[operation]
    return reduce(valid_op, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire: Callable = partial(base_enchantment, 50, 'fire')
    ice: Callable = partial(base_enchantment, 50, 'ice')
    lightning: Callable = partial(base_enchantment, 50, 'lightning')
    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_spell(arg):
        return "Unknown magic type"

    @base_spell.register(int)
    def _(damage):
        return f"Cast damage spell: {damage} power"

    @base_spell.register(str)
    def _(name):
        return f"Cast enchantment: {name}"

    @base_spell.register(list)
    def _(spells):
        return f"Multi-cast: {len(spells)} spells"

    return base_spell


def main() -> None:
    try:
        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer([1, 2, 3, 4], 'hell')}")
        print(f"Product: {spell_reducer([1, 2, 3, 4], 'multiply')}")
        print(f"Max: {spell_reducer([1, 2, 3, 4], 'max')}")
    except KeyError as err:
        print(err)

    print()

    print("Testing partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element} spell with {power} power hits {target}"

    enchanters: dict[str, Callable] = partial_enchanter(base_enchant)
    print(enchanters['fire_enchant']("Sword"))
    print(enchanters['ice_enchant']("Shield"))
    print()

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(7)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()

    print("\nTesting spell dispatcher...")
    dispatch: Callable = spell_dispatcher()
    print(dispatch(100))
    print(dispatch("Fireball"))
    print(dispatch([1, 2, 3]))


if __name__ == "__main__":
    main()
