# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/04 17:40:50 by amamun          #+#    #+#               #
#  Updated: 2026/04/19 20:16:45 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from typing import List, Dict


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    min_power: dict = min(mages, key=lambda x: x['power'])
    max_power: dict = max(mages, key=lambda x: x['power'])
    avg_power: float = sum(map(lambda x: x['power'], mages)) / len(mages)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:
    data_artifacts: List[Dict] = [
        {'name': 'Fire Staff', 'power': 70, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 74, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 104, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 63, 'type': 'focus'}
    ]

    sorted_artifacts: list[dict] = artifact_sorter(data_artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
          f"power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)\n")

    print("Testing spell transformer...")
    spells: list[str] = ["fireball", "heal", "shield"]
    new_spells: list[str] = spell_transformer(spells)
    for spell in new_spells:
        print(f"{spell} ", end="")
    print()


if __name__ == "__main__":
    main()
