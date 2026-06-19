from fastapi import APIRouter
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class RoomCreate(BaseModel):
    room_number: str
    room_type: str


@router.get("/rooms")
def get_rooms():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rooms")

    rooms = cursor.fetchall()

    cursor.close()
    conn.close()

    return rooms


@router.post("/rooms")
def create_room(room: RoomCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO rooms
        (room_number, room_type)
        VALUES (%s, %s)
        """,
        (
            room.room_number,
            room.room_type
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Room created successfully"}