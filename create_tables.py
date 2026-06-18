from app.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

with open("app/database/schema.sql", "r") as f:
    cursor.execute(f.read())

conn.commit()

print("✅ Tables Created Successfully")

cursor.close()
conn.close()