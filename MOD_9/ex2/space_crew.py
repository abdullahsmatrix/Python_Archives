from enum import Enum
from datetime import datetime
from pydantic import BaseModel, constr, conint, Field
from pathlib import Path
from typing import Any, List
import json
from pydantic import confloat, model_validator, ValidationError


DATA_DIR = (Path(__file__).resolve().parent.parent / "data_generator" /
            "generated_data")
SPACE_MISSION_JSON = DATA_DIR / "space_missions.json"


def load_space_mission_data() -> dict[str, Any]:
    with SPACE_MISSION_JSON.open("r", encoding="utf-8") as f:
        return json.load(f)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: constr(min_length=3, max_length=10)
    name: constr(min_length=2, max_length=50)
    rank: Rank
    age: conint(ge=18, le=80)
    specialization: constr(min_length=3, max_length=30)
    years_experience: conint(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: constr(min_length=5, max_length=15)
    mission_name: constr(min_length=3, max_length=100)
    destination: constr(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: conint(ge=1, le=3650)
    crew: List[CrewMember] = Field(
        default_factory=list, min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: confloat(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        has_leader: bool = False

        for member in self.crew:
            if member.rank in [Rank.CAPTAIN, Rank.COMMANDER]:
                has_leader = True

        if not has_leader:
            raise ValueError("Must have atleast one commander or captain")

        expereince_crew: int = 0

        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience > 5:
                    expereince_crew += 1
            if expereince_crew < (len(self.crew) / 2):
                raise ValueError("Long mission need half team with 5+ "
                                 "years experienced crew")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    mission_data: list = load_space_mission_data()
    count = 1

    try:
        for missions in mission_data:
            mission = SpaceMission(**missions)
            print(f"Valid mission created. Mission-{count}:")
            print(f"Mission: {mission.mission_name}")
            print(f"ID: {mission.mission_id}")
            print(f"Destination: {mission.destination}")
            print(f"Duration: {mission.duration_days} days")
            print(f"Budget: ${mission.budget_millions}M")
            print(f"Crew size: {len(mission.crew)}")
            print("Crew members:")
            for member in mission.crew:
                print(f"- {member.name} ({member.rank.value}) "
                      f"- {member.specialization}")
            count += 1
            print()
        print("\n========================================")
        print("Expected validation error:")
        invalid_crew = [
            CrewMember(
                member_id="CM004",
                name="James Holden",
                rank=Rank.OFFICER,
                age=30,
                specialization="Pilot",
                years_experience=4
            )
        ]
        mission_data[0]["crew"] = invalid_crew
        SpaceMission(**mission_data[0])

    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
