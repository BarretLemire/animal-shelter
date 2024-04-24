from pydantic import BaseModel

class Shelter:
    name: str
    address: str
    animals: dict[str, int]