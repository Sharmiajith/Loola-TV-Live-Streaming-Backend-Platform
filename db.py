
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="loola_db"
)

cursor = conn.cursor()

from database.db import cursor

def get_stream_data():

    cursor.execute(
        "SELECT id,title,status FROM streams"
    )

    rows = cursor.fetchall()

    streams = []

    for row in rows:
        streams.append({
            "id": row[0],
            "title": row[1],
            "status": row[2]
        })

    return streams