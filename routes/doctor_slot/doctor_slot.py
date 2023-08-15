from fastapi import APIRouter,HTTPException
from datetime import time
from sqlalchemy.sql import select
from config.db import conn
from models.index import doctor_slots
from models.index import doctors
from schemas.index import Doctor_slot

doctor_slot = APIRouter()

# get all data
@doctor_slot.get("/")
async def read_data():
    return conn.execute(doctor_slots.select()).fetchall()

# get specific data
@doctor_slot.get("/{id}")
async def read_data(id: int):
    return conn.execute(doctor_slots.select().where(doctor_slots.c.id == id)).fetchall()

# write data
@doctor_slot.post("/")
async def write_data(doctor_slot: Doctor_slot):
    # checking if doctor_id exists
    doctor_exists = conn.execute(
        select([doctors.c.id]).where(doctors.c.id == doctor_slots.c.doctor_id)
    ).fetchone()

    if not doctor_exists:
        raise HTTPException(status_code=400, detail="Doctor not found")
    
    start_time_parts = map(int, doctor_slot.startTime.split('.'))
    start_time = time(*start_time_parts)

    end_time_parts = map(int, doctor_slot.endTime.split('.'))
    end_time = time(*end_time_parts)


    conn.execute(doctor_slots.insert().values(
        doctor_id=doctor_slot.doctor_id,
        startTime=start_time,
        endTime=end_time,
        startDate=doctor_slot.startDate,
        endDate=doctor_slot.endDate,
        location=doctor_slot.location
    ))
    return {"message": "Data added successfully"}

# modify data
@doctor_slot.put("/{id}")
async def update_data(id: int, doctor_slot: Doctor_slot):
    # checking if doctor_id exists
    doctor_exists = conn.execute(
        select([doctors.c.id]).where(doctors.c.id == doctor_slot.doctor_id)
    ).fetchone()

    if not doctor_exists:
        raise HTTPException(status_code=400, detail="Doctor not found")
    
    start_time_parts = map(int, doctor_slot.startTime.split('.'))
    start_time = time(*start_time_parts)

    end_time_parts = map(int, doctor_slot.endTime.split('.'))
    end_time = time(*end_time_parts)


    conn.execute(doctor_slots.update().values(
        doctor_id=doctor_slot.doctor_id,
        startTime=start_time,
        endTime=end_time,
        startDate=doctor_slot.startDate,
        endDate=doctor_slot.endDate,
        location=doctor_slot.location
    ).where(doctor_slots.c.id == id))
    return {"message": "Data updated successfully"}

# delete data
@doctor_slot.delete("/{id}")
async def delete_data(id: int):
    conn.execute(doctor_slots.delete().where(doctor_slots.c.id == id))
    return {"message": "Data deleted successfully"}

