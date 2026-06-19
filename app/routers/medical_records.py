from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class MedicalRecordCreate(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    diagnosis: str
    prescription: str


@router.get("/medical-records")
def get_medical_records():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        mr.record_id,
        p.name AS patient_name,
        d.name AS doctor_name,
        mr.diagnosis,
        mr.prescription,
        mr.visit_date
    FROM medical_records mr
    JOIN patients p
        ON mr.patient_id = p.patient_id
    JOIN doctors d
        ON mr.doctor_id = d.doctor_id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records


@router.post("/medical-records")
def create_medical_record(record: MedicalRecordCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO medical_records
        (
            appointment_id,
            patient_id,
            doctor_id,
            diagnosis,
            prescription
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            record.appointment_id,
            record.patient_id,
            record.doctor_id,
            record.diagnosis,
            record.prescription
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Medical record created successfully"
    }

@router.get("/medical-records/{record_id}")
def get_medical_record(record_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM medical_records
        WHERE record_id = %s
        """,
        (record_id,)
    )

    record = cursor.fetchone()

    cursor.close()
    conn.close()

    return record