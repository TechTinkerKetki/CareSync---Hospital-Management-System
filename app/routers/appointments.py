from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    appointment_time: str
    status: str


@router.get("/appointments")
def get_appointments():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        a.appointment_id,
        p.name AS patient_name,
        d.name AS doctor_name,
        a.appointment_date,
        a.appointment_time,
        a.status
    FROM appointments a
    JOIN patients p
    ON a.patient_id = p.patient_id
    JOIN doctors d
    ON a.doctor_id = d.doctor_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


@router.post("/appointments")
def create_appointment(appointment: AppointmentCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO appointments
        (
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            status
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            appointment.patient_id,
            appointment.doctor_id,
            appointment.appointment_date,
            appointment.appointment_time,
            appointment.status
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Appointment created successfully"}

@router.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM appointments
        WHERE appointment_id = %s
        """,
        (appointment_id,)
    )

    appointment = cursor.fetchone()

    cursor.close()
    conn.close()

    return appointment


@router.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM appointments
        WHERE appointment_id = %s
        """,
        (appointment_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Appointment deleted successfully"}