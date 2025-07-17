import streamlit as st
from app import qcm, admin

st.set_page_config(page_title="QCM FiveM", layout="centered")

page = st.sidebar.selectbox("Navigation", ["Accueil", "QCM", "Admin"])

if page == "Accueil":
    st.title("Bienvenue sur le test QCM FiveM")
    st.write("Choisis une page dans le menu à gauche.")
elif page == "QCM":
    qcm.afficher_qcm()
elif page == "Admin":
    admin.admin_panel()
