import streamlit as st
from app.db import get_connection
# from app.discord_bot import give_role  # À activer plus tard

seuil = 3  # Score minimum pour réussir

def afficher_qcm():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM qcm_questions")
    questions = cursor.fetchall()

    score = 0
    for q in questions:
        reponse = st.radio(q['question'], [q['choix1'], q['choix2'], q['choix3'], q['choix4']], key=q['id'])
        if reponse == q['bonne_reponse']:
            score += 1

    if st.button("Soumettre"):
        st.success(f"Score : {score}/{len(questions)}")
        if score >= seuil:
            st.balloons()
            st.success("Bravo ! Le rôle Discord va être ajouté.")
            # give_role(discord_id)  # à activer plus tard
        else:
            st.error("Échec. Tu peux réessayer.")