# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Elitecard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 18:56:35 by amamun          #+#    #+#               #
#  Updated: 2026/03/26 20:47:23 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, armor: int,
                 attack_power: int, health: int, mana_pool: int) -> None:
        super().__init__(name, cost, rarity)
        self.armor: int = armor
        self.attack_power: int = attack_power
        self.health: int = health
        self.mana_pool: int = mana_pool

    def attack(self, target: int) -> dict[str, object]:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict[str, object]:
        blocked: int = min(self.armor, incoming_damage)
        actual_damage: int = incoming_damage - blocked
        self.armor -= blocked
        self.health -= actual_damage
        is_alive: bool = self.health > 0
        return {
            'defender': self.name,
            'damage_taken': actual_damage,
            'damage_blocked': blocked,
            'still_alive': is_alive
        }

    def get_combat_stats(self) -> dict[str, object]:
        return {
            'power': self.attack_power,
            'health': self.health,
            'armor': self.armor
        }

    def cast_spell(self, spell_name: str,
                   targets: list[object]) -> dict[str, object] | None:
        if self.cost <= self.mana_pool:
            self.mana_pool -= self.cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "target": targets,
                "mana_used": self.cost
            }
        return None

    def channel_mana(self, amount: int) -> dict[str, object]:
        self.mana_pool += amount
        return {
            "channelled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict[str, object]:
        return {
            "cast_cost": self.cost,
            "mana_pool": self.mana_pool
        }

    def play(self, game_state: dict[str, object]) -> dict[str, object]:
        return {
            "event": "card_played",
            "card_name": self.name,
            "rarity": self.rarity,
            "combat_stats": self.get_combat_stats(),
            "magic_stats": self.get_magic_stats()
        }
