from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Enum
from config.db import meta

patients = Table(
    'patient', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('gender', Enum('l', 'p')),
    Column('addres', String(255)),
)