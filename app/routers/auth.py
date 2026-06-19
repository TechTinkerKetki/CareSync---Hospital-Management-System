from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database.db import get_connection

router = APIRouter()


class UserRegister(BaseModel):
    username: str
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserRegister):

    conn = get_connection()
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (user.username,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        conn.close()

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Insert new user
    cursor.execute(
        """
        INSERT INTO users
        (username, password_hash, role)
        VALUES (%s, %s, %s)
        """,
        (
            user.username,
            user.password,
            user.role
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT user_id, username, role
        FROM users
        WHERE username = %s
        AND password_hash = %s
        """,
        (
            user.username,
            user.password
        )
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return {
        "message": "Login successful",
        "user_id": result[0],
        "username": result[1],
        "role": result[2]
    }