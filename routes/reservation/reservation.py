from fastapi import APIRouter, HTTPException
from sqlalchemy.sql import select
from datetime import time
from config.db import conn
from models.index import reservations
from models.index import doctors
from models.index import doctor_slots
from models.index import patients
from schemas.index import Reservation

reservation = APIRouter()


# get all data
@reservation.get("/")
async def read_all_data():
    query = select([reservations, 
                    patients.c.name.label("patient_name"), 
                    patients.c.addres.label("patient_addres"), 
                    doctors.c.name.label("doctor_name"), 
                    doctors.c.specialty.label("doctor_specialty"), 
                    doctor_slots.c.location.label("reservation_location")]).select_from(
        reservations.join(patients, patients.c.id == reservations.c.patient_id)
        .join(doctors, doctors.c.id == reservations.c.doctor_id)
        .join(doctor_slots, doctor_slots.c.doctor_id == reservations.c.doctor_id)
    ).order_by(reservations.c.id)
    result = conn.execute(query).fetchall()
    return result


# get specific data
@reservation.get("/{id}")
async def read_data(id: int):
    query = select([reservations, 
                    patients.c.name.label("patient_name"), 
                    patients.c.addres.label("patient_addres"), 
                    doctors.c.name.label("doctor_name"), 
                    doctors.c.specialty.label("doctor_specialty"), 
                    doctor_slots.c.location.label("reservation_location")]).select_from(
        reservations.join(patients, patients.c.id == reservations.c.patient_id)
        .join(doctors, doctors.c.id == reservations.c.doctor_id)
        .join(doctor_slots, doctor_slots.c.doctor_id == reservations.c.doctor_id)
    ).where(reservations.c.id==id)
    result = conn.execute(query).fetchall()
    return result

# write data
@reservation.post("/")
async def write_data(reservation: Reservation):
    # checking if doctor_id exists
    doctor_exists = conn.execute(
        select([doctors.c.id]).where(doctors.c.id == reservation.doctor_id)
    ).fetchone()

    if not doctor_exists:
        raise HTTPException(status_code=400, detail="Doctor not found")
    
    # checking if patient_id exists
    patient_exists = conn.execute(
        select([patients.c.id]).where(patients.c.id == reservation.patient_id)
    ).fetchone()

    if not patient_exists:
        raise HTTPException(status_code=400, detail="Patient not found")


    # checking the encounter date
    doctor_slot_date_query = doctor_slots.select().where(doctor_slots.c.doctor_id == reservation.doctor_id)
    doctor_slot_date_result = conn.execute(doctor_slot_date_query).fetchone()

    if doctor_slot_date_result is None:
        raise HTTPException(status_code=404, detail="Doctor slots not found")
    
    start_date = doctor_slot_date_result["startDate"]
    end_date = doctor_slot_date_result["endDate"]

    if not (start_date <= reservation.encounter_date <= end_date):
        raise HTTPException(status_code=400, detail=f"The doctor is offline in that date, please chose date between {start_date} and {end_date}")
    
    
    # checking the encounter time
    doctor_slot_time_query = doctor_slots.select().where(doctor_slots.c.doctor_id == reservation.doctor_id)
    doctor_slot_time_result = conn.execute(doctor_slot_time_query).fetchone()
    

    if doctor_slot_time_result is None:
        raise HTTPException(status_code=404, detail="Doctor slots not found")
    
    start_time = doctor_slot_time_result["startTime"]
    end_time = doctor_slot_time_result["endTime"]

    reservation_time_parts = map(int, reservation.encounter_time.split('.'))
    reservation_time = time(*reservation_time_parts)

    if not (start_time <= reservation_time <= end_time):
        raise HTTPException(
            status_code=400,
            detail=f"The doctor is unavailable during that time. Please choose a time between {start_time} and {end_time}."
        )
    
   
    conn.execute(reservations.insert().values(
        doctor_id=reservation.doctor_id,
        patient_id=reservation.patient_id,
        encounter_date=reservation.encounter_date,
        encounter_time=reservation_time
    ))
    return {"message": "Data added successfully"}


# modify data
@reservation.put("/{id}")
async def update_data(id: int, reservation: Reservation):
     # checking if doctor_id exists
    doctor_exists = conn.execute(
        select([doctors.c.id]).where(doctors.c.id == reservation.doctor_id)
    ).fetchone()

    if not doctor_exists:
        raise HTTPException(status_code=400, detail="Doctor not found")
    
    # checking if patient_id exists
    patient_exists = conn.execute(
        select([patients.c.id]).where(patients.c.id == reservation.patient_id)
    ).fetchone()

    if not patient_exists:
        raise HTTPException(status_code=400, detail="Patient not found")


    # checking the encounter date
    doctor_slot_date_query = doctor_slots.select().where(doctor_slots.c.doctor_id == reservation.doctor_id)
    doctor_slot_date_result = conn.execute(doctor_slot_date_query).fetchone()

    if doctor_slot_date_result is None:
        raise HTTPException(status_code=404, detail="Doctor slots not found")
    
    start_date = doctor_slot_date_result["startDate"]
    end_date = doctor_slot_date_result["endDate"]

    if not (start_date <= reservation.encounter_date <= end_date):
        raise HTTPException(status_code=400, detail=f"The doctor is offline in that date, please chose date between {start_date} and {end_date}")
    
    
    # checking the encounter time
    doctor_slot_teme_query = doctor_slots.select().where(doctor_slots.c.doctor_id == reservation.doctor_id)
    doctor_slot_time_result = conn.execute(doctor_slot_teme_query).fetchone()
    

    if doctor_slot_time_result is None:
        raise HTTPException(status_code=404, detail="Doctor slots not found")
    
    start_time = doctor_slot_time_result["startTime"]
    end_time = doctor_slot_time_result["endTime"]

    reservation_time_parts = map(int, reservation.encounter_time.split('.'))
    reservation_time = time(*reservation_time_parts)

    if not (start_time <= reservation_time <= end_time):
        raise HTTPException(
            status_code=400,
            detail=f"The doctor is unavailable during that time. Please choose a time between {start_time} and {end_time}."
        )
    

    conn.execute(reservations.update().values(
        doctor_id=reservation.doctor_id,
        patient_id=reservation.patient_id,
        encounter_date=reservation.encounter_date,
        encounter_time=reservation_time
    ).where(reservations.c.id == id))
    return {"message": "Data updated successfully"}


# delete data
@reservation.delete("/{id}")
async def delete_data(id: int):
    conn.execute(reservations.delete().where(reservations.c.id == id))
    return {"message": "Data deleted successfully"}
