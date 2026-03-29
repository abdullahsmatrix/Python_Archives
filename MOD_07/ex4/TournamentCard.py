# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/26 17:20:52 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:59:36 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, armor: int = 0,
                 base_rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self.max_health: int = health
        self.armor: int = armor
        self._rating: int = base_rating
        self._wins: int = 0
        self._losses: int = 0

    def play(self, game_state: dict[str, object]) -> dict[str, object]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered the battlefield",
            "stats": self.get_combat_stats()
        }

    def get_card_info(self) -> dict[str, object]:
        info: dict[str, object] = super().get_card_info()
        info["type"] = "TournamentCard"
        info["attack"] = self.attack_power
        info["health"] = self.health
        return info

    def attack(self, target: object) -> dict[str, object]:
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict[str, object]:
        blocked: int = min(self.armor, incoming_damage)
        actual_damage = incoming_damage - blocked
        self.armor = max(0, self.armor - blocked)
        self.health -= actual_damage
        return {
            'power': self.attack_power,
            'health': self.health,
            'armor': self.armor,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict[str, object]:
        return {
            "power": self.attack_power,
            "health": self.health,
            "armor": self.armor
        }

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating = max(0, self._rating - losses * 16)

    def get_rank_info(self) -> dict[str, object]:
        return {
            "name": self.name,
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
            "record": f"{self._wins} - {self._losses}"
        }

    def reset_for_match(self) -> None:
        self.health = self.max_health

    def get_tournament_stats(self) -> dict[str, object]:
        return {
            "card_info": self.get_card_info(),
            "combat_stats": self.get_combat_stats(),
            "rank_info": self.get_rank_info(),
            "interfaces": ["Card", "Combatable", "Rankable"]
        }
