from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class BillCreate(BaseModel):
    appointment_id: int
    amount: float
    payment_method: str


@router.get("/bills")
def get_bills():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        b.bill_id,
        p.name AS patient_name,
        d.name AS doctor_name,
        b.amount,
        b.payment_status,
        b.payment_method,
        b.generated_at
    FROM bills b
    JOIN appointments a
        ON b.appointment_id = a.appointment_id
    JOIN patients p
        ON a.patient_id = p.patient_id
    JOIN doctors d
        ON a.doctor_id = d.doctor_id
    """

    cursor.execute(query)

    bills = cursor.fetchall()

    cursor.close()
    conn.close()

    return bills


@router.post("/bills")
def create_bill(bill: BillCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bills
        (
            appointment_id,
            amount,
            payment_method
        )
        VALUES (%s, %s, %s)
        """,
        (
            bill.appointment_id,
            bill.amount,
            bill.payment_method
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Bill generated successfully"}

@router.get("/bills/{bill_id}")
def get_bill(bill_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM bills
        WHERE bill_id = %s
        """,
        (bill_id,)
    )

    bill = cursor.fetchone()

    cursor.close()
    conn.close()

    return bill


@router.put("/bills/{bill_id}/pay")
def pay_bill(bill_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE bills
        SET payment_status = 'Paid'
        WHERE bill_id = %s
        """,
        (bill_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Bill marked as paid"}