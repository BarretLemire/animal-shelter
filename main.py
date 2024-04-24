# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI, HTTPException
from schemas import Shelter 
from dataclasses import dataclass

app = FastAPI()


shelters_data = [
    {
        "name": "St. George Animal Shelter",
        "address": "605 Waterworks Dr, St. George, UT 84770",
        "animals": {
            "cats": 13,
            "dogs": 15,
        }
    },
    {
        "name": "St. George Paws",
        "address": "1125 W 1130 N, St. George, UT 84770",
        "animals": {
            "cats": 12,
            "dogs": 9,
        }
    },
    {
        "name": "Animal Rescue Team",
        "address": "1838 W 1020 N Ste. B, St. George, UT 84770",
        "animals": {
            "cats": 4,
            "dogs": 7,
        }
    }
]

shelters = [Shelter(**shelter_data) for shelter_data in shelters_data]

@app.get("/shelters")
async def get_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters/new") 
async def create_shelter(name: str, address: str, animals: dict[str, int]) -> list[Shelter]:
    new_shelter_data = {
        "name": name,
        "address": address,
        "animals": animals
    }
    new_shelter = Shelter(**new_shelter_data)
    shelters.append(new_shelter)
    return shelters

@app.put("/shelters/{name}")
async def update_shelter(name: str, address: str, animals: dict[str, int] = None) -> Shelter:
    found_shelter = None
    for shelter in shelters:
        if shelter.name == name:
            found_shelter = shelter
            break

    if found_shelter is None:
        raise HTTPException(status_code=404, detail="Shelter not found")
    
    if address is not None:
        found_shelter.address = address
    if animals is not None:
        found_shelter.animals = animals

    return found_shelter

@app.delete("/shelters/{name}")
async def delete_shelter(name: str):
    global shelters
    initial_length = len(shelters)
    shelters = [shelter for shelter in shelters if shelter.name != name]
    if len(shelters) == initial_length:
        raise HTTPException(status_code=404, detail="Shelter not found")
    return {"message": f"Shelter '{name}' had been deleted"}

