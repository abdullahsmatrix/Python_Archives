# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 22:24:54 by amamun          #+#    #+#               #
#  Updated: 2026/02/27 23:16:52 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator
import time


def game_event_stream(count: int) -> Generator[dict, None, None]:
    player: list = ['alice', 'bob', 'charlie', 'dave', 'michal']
    action: list = ['killed monster', 'found treasure', 'leveled up']

    for i in range(count):
        yield {
            "id": i+1,
            "player": player[i % len(player)],
            "level": (i * 3) % 20 + 1,
            "action": action[i % len(action)]
        }


def process_events(stream: Generator[dict, None, None]) -> None:
    total: int = 0
    high_level: int = 0
    treasure: int = 0
    level_up: int = 0

    for event in stream:
        total += 1
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            level_up += 1
        if total <= 5:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"({event['level']}) {event['action']}"
            )
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")


def fibonacci(count: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers(count: int) -> Generator[int, None, None]:
    num = 2
    found = 0

    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    start_time = time.time()
    stream = game_event_stream(1000)
    process_events(stream)
    elapsed_time = time.time() - start_time
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed_time:.3f} seconds")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in fibonacci(10):
        print(_, end=", ")
    print()

    print("Prime numbers (first 5):", end=" ")
    for p in prime_numbers(5):
        print(p, end=", ")
    print()


if __name__ == "__main__":
    main()
