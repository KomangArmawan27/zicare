from fastapi import APIRouter

from routes.index import patient as patient_router
from routes.index import doctor as doctor_router
from routes.index import reservation as reservation_router
from routes.index import doctor_slot as doctor_slot_router

router = APIRouter()

router.include_router(patient_router, prefix="/patient", tags=["patient"])
router.include_router(doctor_router, prefix="/doctor", tags=["doctor"])
router.include_router(doctor_slot_router, prefix="/doctor_slot", tags=["doctor_slot"])
router.include_router(reservation_router, prefix="/reservation", tags=["reservation"])