# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/19 19:05:11 by amamun          #+#    #+#               #
#  Updated: 2026/04/19 20:12:37 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}")
        start: float = time.time()
        result: Any = func(*args, **kwargs)
        end: float = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int,
                    *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(0, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    msg: str = (
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
                    print(msg)
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        valid_chars: bool = all(c.isalpha() or c.isspace() for c in name)
        return len(name) >= 3 and valid_chars

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        msg: str = f"Successfully cast {spell_name} with {power} power"
        return msg


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def slow_spell() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {slow_spell()}")
    print()

    print("\nTesting MageGuild...")
    guild: MageGuild = MageGuild()
    print(f"{guild.validate_mage_name('Alex')}")
    print(f"{guild.validate_mage_name('Jo')}")

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))
    print()

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> None:
        raise Exception("Mana leak!")

    print(unstable_spell())


if __name__ == "__main__":
    main()
