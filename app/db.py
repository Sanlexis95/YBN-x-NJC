import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="votre_host",
        user="votre_user",
        password="votre_mot_de_passe",
        database="votre_bdd"
    )