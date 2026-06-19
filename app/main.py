from fastapi import FastAPI
from app.routers.patients import router as patient_router
from app.routers.doctors import router as doctor_router
from app.routers.appointments import router as appointment_router
from app.routers.auth import router as auth_router
from app.routers.medical_records import router as medical_record_router
from app.routers.rooms import router as room_router
from app.routers.admissions import router as admission_router
from app.routers.bills import router as bill_router
from app.routers.hospital import router as hospital_router

app = FastAPI()

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(auth_router)
app.include_router(medical_record_router)
app.include_router(room_router)
app.include_router(admission_router)
app.include_router(bill_router)
app.include_router(hospital_router)

@app.get("/")
def home():
    return {"status": "running"}
