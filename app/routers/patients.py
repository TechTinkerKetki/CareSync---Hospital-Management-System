from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/patients")
def get_patients():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows