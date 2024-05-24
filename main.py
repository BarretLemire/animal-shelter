# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

class Animal(BaseModel):
    cats: int
    dogs: int

class Shelter(BaseModel):
    name: str
    address: str
    animals: Animal

app = FastAPI()

shelters_db: List[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animal(cats=13, dogs=15)
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animal(cats=12, dogs=9)
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animal(cats=4, dogs=7)
    )
]

# CRUD endpoints

@app.post("/shelters/", response_model=Shelter)
async def create_shelter(shelter: Shelter):
    shelters_db.append(shelter)
    return shelter

@app.get("/shelters/", response_model=List[Shelter])
async def read_shelters():
    return shelters_db

@app.get("/shelters/{shelter_id}", response_model=Shelter)
async def read_shelter(shelter_id: int):
    try:
        return shelters_db[shelter_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Shelter not found")

@app.put("/shelters/{shelter_id}", response_model=Shelter)
async def update_shelter(shelter_id: int, shelter: Shelter):
    try:
        shelters_db[shelter_id] = shelter
        return shelter
    except IndexError:
        raise HTTPException(status_code=404, detail="Shelter not found")

@app.delete("/shelters/{shelter_id}")
async def delete_shelter(shelter_id: int):
    if shelter_id < 0 or shelter_id >= len(shelters_db):
        raise HTTPException(status_code=404, detail="Shelter not found")
    deleted_shelter = shelters_db.pop(shelter_id)
    return JSONResponse(content={"message": "Shelter deleted successfully", "shelter": deleted_shelter.dict()})
