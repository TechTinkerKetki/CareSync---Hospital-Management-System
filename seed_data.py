from app.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

with open("app/database/sample_data.sql", "r") as f:
    cursor.execute(f.read())

conn.commit()

print("✅Data Filled Successfully")

cursor.close()
conn.close()