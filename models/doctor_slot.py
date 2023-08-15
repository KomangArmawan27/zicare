from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Time
from config.db import meta

doctor_slots = Table(
    'doctor_slot', meta,
    Column('id', Integer, primary_key=True),
    Column('doctor_id', Integer),
    Column('startTime', Time),
    Column('endTime', Time),
    Column('startDate', Date),
    Column('endDate', Date),
    Column('location', String(255)),
)