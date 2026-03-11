# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 19:07:50 by amamun          #+#    #+#               #
#  Updated: 2026/02/24 23:18:03 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def achievement_analytics(players: dict) -> None:
    print("=== Achievement Analytics ===")

    unique_achievements: set = (players["alice"] | players["bob"]
                                | players["charlie"])
    print(f"All unique achievements:{unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    common_achievemnts: set = (players["alice"] & players["bob"]
                               & players["charlie"])
    print(f"Common to all players: {common_achievemnts}")

    rare_achievements: set = {a for a in unique_achievements
                              if sum(1 for p in players.values()
                                     if a in p) == 1}
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common: set = players["alice"] & players["bob"]
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique: set = players["alice"] - players["bob"]
    bob_unique: set = players["bob"] - players["alice"]
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


def print_achievements(players: dict) -> None:
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
    print()


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    players: dict = {'alice': alice, 'bob': bob, 'charlie': charlie}
    print_achievements(players)
    achievement_analytics(players)


if __name__ == "__main__":
    main()
