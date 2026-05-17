# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/31 19:42:37 by amamun          #+#    #+#               #
#  Updated: 2026/04/03 20:47:21 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from pydantic import BaseModel, Field, ValidationError
from typing import Annotated
from datetime import datetime


# Reusable type annotation type:
str_3_10 = Annotated[str, Field(min_length=3, max_length=10)]
str_1_50 = Annotated[str, Field(min_length=1, max_length=50)]
int_1_20 = Annotated[int, Field(ge=1, le=20)]
flt_1_100 = Annotated[float, Field(ge=0.0, le=100.0)]


class SpaceStation(BaseModel):
    station_id: str_3_10
    name: str_1_50
    crew_size: int_1_20
    power_level: flt_1_100
    oxygen_level: flt_1_100
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str = Field(default="", min_length=0, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=======================================")

    data: dict = {
        'station_id': "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "is_operational": True
    }

    try:
        space_station_obj = SpaceStation(**data)
        print("Valid station created:")
        print(f"ID: {space_station_obj.station_id}")
        print(f"Name: {space_station_obj.name}")
        print(f"Crew: {space_station_obj.crew_size} people")
        print(f"Power: {space_station_obj.power_level}%")
        print(f"Oxygen: {space_station_obj.oxygen_level}%")
        is_operational = space_station_obj.is_operational is True
        status = 'Operational' if is_operational else 'Offline'
        print(f"Status: {status}")

    except Exception as err:
        print(err)

    print("===============================")
    print("Expected validation error:")
    data['crew_size'] = 25
    try:
        SpaceStation(**data)
    except ValidationError as err:
        for error in err.errors():
            if error['loc'][0] == "crew_size":
                print(error['msg'])


if __name__ == "__main__":
    main()
