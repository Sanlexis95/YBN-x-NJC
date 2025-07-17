import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host="49.12.169.210",
        port=3306,
        user=os.getenv("DB_PORT", 3306"),          # à définir dans Streamlit Cloud
        password=os.getenv("DFKyRfGvhaKkywkB"),
        database=os.getenv("nexus_db_9374")
    )
