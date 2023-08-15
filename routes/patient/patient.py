from fastapi import APIRouter
from config.db import conn
from models.index import patients
from schemas.index import Patient

patient = APIRouter()

# get all data
@patient.get("/")
async def read_data():
    return conn.execute(patients.select()).fetchall()


# get specific date
@patient.get("/{id}")
async def read_data(id: int):
    return conn.execute(patients.select().where(patients.c.id == id)).fetchall()


# write data
@patient.post("/")
async def write_data(patient: Patient):
    conn.execute(patients.insert().values(
        name=patient.name,
        gender=patient.gender,
        addres=patient.addres
    ))
    return {"message": "Data added successfully"}


# modify data
@patient.put("/{id}")
async def update_data(id: int, patient: Patient):
    conn.execute(patients.update().values(
        name=patient.name,
        gender=patient.gender,
        addres=patient.addres
    ).where(patients.c.id == id))
    return {"message": "Data updated successfully"}


# delete data
@patient.delete("/{id}")
async def delete_data(id: int):
    conn.execute(patients.delete().where(patients.c.id == id))
    return {"message": "Data deleted successfully"}

