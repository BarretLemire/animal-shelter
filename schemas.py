from pydantic import BaseModel
from typing import Dict

class Shelter(BaseModel):
    name: str
    address: str
    animals: Dict[str, int]

shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals={"cats": 13, "dogs": 15}
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals={"cats": 12, "dogs": 9}
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals={"cats": 4, "dogs": 7}
    )
]
