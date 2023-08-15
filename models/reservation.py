from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Time, Date
from config.db import meta

reservations = Table(
    'reservation', meta,
    Column('id', Integer, primary_key=True),
    Column('doctor_id', Integer),
    Column('patient_id', Integer),
    Column('encounter_date', Date),
    Column('encounter_time', Time),
)