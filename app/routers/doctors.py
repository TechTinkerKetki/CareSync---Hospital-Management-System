from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class DoctorCreate(BaseModel):
    department_id: int
    name: str
    specialization: str
    phone: str
    consultation_fee: float


@router.get("/doctors")
def get_doctors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctors")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


@router.post("/doctors")
def create_doctor(doctor: DoctorCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO doctors
        (department_id, name, specialization, phone, consultation_fee)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            doctor.department_id,
            doctor.name,
            doctor.specialization,
            doctor.phone,
            doctor.consultation_fee,
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Doctor created successfully"}  

@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM doctors WHERE doctor_id = %s",
        (doctor_id,)
    )

    doctor = cursor.fetchone()

    cursor.close()
    conn.close()

    return doctor