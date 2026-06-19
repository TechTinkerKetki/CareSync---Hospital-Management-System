from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class AdmissionCreate(BaseModel):
    patient_id: int
    room_id: int
    admission_date: str
    discharge_date: str | None = None


@router.get("/admissions")
def get_admissions():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        a.admission_id,
        p.name AS patient_name,
        r.room_number,
        r.room_type,
        a.admission_date,
        a.discharge_date
    FROM admissions a
    JOIN patients p
        ON a.patient_id = p.patient_id
    JOIN rooms r
        ON a.room_id = r.room_id
    """

    cursor.execute(query)

    admissions = cursor.fetchall()

    cursor.close()
    conn.close()

    return admissions


@router.post("/admissions")
def create_admission(admission: AdmissionCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO admissions
        (
            patient_id,
            room_id,
            admission_date,
            discharge_date
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            admission.patient_id,
            admission.room_id,
            admission.admission_date,
            admission.discharge_date
        )
    )

    cursor.execute(
        """
        UPDATE rooms
        SET availability_status='Occupied'
        WHERE room_id=%s
        """,
        (admission.room_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Admission created successfully"}

@router.put("/admissions/{admission_id}/discharge")
def discharge_patient(admission_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT room_id
        FROM admissions
        WHERE admission_id = %s
        """,
        (admission_id,)
    )

    room_id = cursor.fetchone()[0]

    cursor.execute(
        """
        UPDATE admissions
        SET discharge_date = CURRENT_DATE
        WHERE admission_id = %s
        """,
        (admission_id,)
    )

    cursor.execute(
        """
        UPDATE rooms
        SET availability_status = 'Available'
        WHERE room_id = %s
        """,
        (room_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Patient discharged successfully"}