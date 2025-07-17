import streamlit as st
from app.db import get_connection

def admin_panel():
    st.title("Panel Admin - Ajouter des questions")

    question = st.text_input("Question")
    choix1 = st.text_input("Choix 1")
    choix2 = st.text_input("Choix 2")
    choix3 = st.text_input("Choix 3")
    choix4 = st.text_input("Choix 4")
    bonne_reponse = st.selectbox("Bonne réponse", [choix1, choix2, choix3, choix4])

    if st.button("Ajouter la question"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO qcm_questions (question, choix1, choix2, choix3, choix4, bonne_reponse)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (question, choix1, choix2, choix3, choix4, bonne_reponse))
        conn.commit()
        st.success("Question ajoutée avec succès.")