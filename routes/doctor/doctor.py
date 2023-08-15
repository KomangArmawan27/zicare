from fastapi import APIRouter
from config.db import conn
from models.index import doctors
from schemas.index import Doctor

doctor = APIRouter()

# get all data
@doctor.get("/")
async def read_data():
    return conn.execute(doctors.select()).fetchall()

# get specific data
@doctor.get("/{id}")
async def read_data(id: int):
    return conn.execute(doctors.select().where(doctors.c.id == id)).fetchall()

# write data
@doctor.post("/")
async def write_data(doctor: Doctor):
    conn.execute(doctors.insert().values(
        name=doctor.name,
        gender=doctor.gender,
        addres=doctor.addres,
        specialty=doctor.specialty,
    ))
    return {"message": "Data added successfully"}

# modify data
@doctor.put("/{id}")
async def update_data(id: int, doctor: Doctor):
    
    conn.execute(doctors.update().values(
        name=doctor.name,
        gender=doctor.gender,
        addres=doctor.addres,
        specialty=doctor.specialty,
    ).where(doctors.c.id == id))
    return {"message": "Doctor updated successfully"}

# delete data
@doctor.delete("/{id}")
async def delete_data(id: int):
    conn.execute(doctors.delete().where(doctors.c.id == id))
    return {"message": "Data deleted successfully"}

