# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 23:09:38 by amamun          #+#    #+#               #
#  Updated: 2026/03/29 19:33:53 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from tools.card_generator import CardGenerator


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.generator: CardGenerator = CardGenerator()

        self.creatures: dict[str, dict[str, object]] = {
            creature['name']: creature
            for creature in self.generator.get_all_creatures()
        }

        self.spells: dict[str, dict[str, object]] = {
            spell['name']: spell
            for spell in self.generator.get_all_spells()
        }

        self.artifacts: dict[str, dict[str, object]] = {
            artifact['name']: artifact
            for artifact in self.generator.get_all_artifacts()
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.creatures:
            return CreatureCard(**self.creatures[name_or_power])
        else:
            return CreatureCard(**self.generator.get_random_creature())

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.spells:
            return SpellCard(**self.spells[name_or_power])
        else:
            return SpellCard(**self.generator.get_random_spell())

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.artifacts:
            return ArtifactCard(**self.artifacts[name_or_power])
        else:
            return ArtifactCard(**self.generator.get_random_artifact())

    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        creatures: list[Card] = []
        spells: list[Card] = []
        artifacts: list[Card] = []

        creature_count = size // 2
        spell_count = (size * 3) // 10
        artifact_count = size - creature_count - spell_count

        for _ in range(creature_count):
            creatures.append(self.create_creature())

        for _ in range(spell_count):
            spells.append(self.create_spell())

        for _ in range(artifact_count):
            artifacts.append(self.create_artifact())

        return {
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts
        }

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            "creatures": ["Dragon", "Gobliin", "Beast"],
            "spells": ["Meteor", "Ice Shard", "Shield Spell"],
            "artifacts": ["Crown of Kings", "Cloak of Shadows",
                          "Mana Crystal"]
        }
