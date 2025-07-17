import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host="49.12.169.210",
        port=3306,
        user=os.getenv("DB_USER"),          # à définir dans Streamlit Cloud
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
