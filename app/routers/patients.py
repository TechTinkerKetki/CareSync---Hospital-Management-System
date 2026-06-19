from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str


@router.get("/patients")
def get_patients():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


@router.post("/patients")
def create_patient(patient: PatientCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO patients
        (name, age, gender, phone, address)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            patient.name,
            patient.age,
            patient.gender,
            patient.phone,
            patient.address,
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Patient created successfully"}

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE patient_id = %s",
        (patient_id,)
    )

    patient = cursor.fetchone()

    cursor.close()
    conn.close()

    return patient


@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE patient_id = %s",
        (patient_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Patient deleted successfully"}