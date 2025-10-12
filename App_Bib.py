import streamlit as st
import random
import json

# Încarcă versetele din fișierul JSON
try:
    with open("App_Bib.json", "r", encoding="utf-8") as f:
        versete = json.load(f)
except FileNotFoundError:
    st.error("❌ Fișierul 'versete.json' nu a fost găsit.")
    st.stop()

# Configurare pagină
st.set_page_config(page_title="Verset pentru suflet", page_icon="📖", layout="centered")

# Titlu aplicație
st.title("📖 Verset biblic pentru suflet")
st.write("Alege starea ta emoțională și primește un verset care să-ți aducă mângâiere și speranță.")

# Alege emoția
emotie_selectata = st.selectbox("Cum te simți azi?", list(versete.keys()))

# Afișează versetul când apasă pe buton
if st.button("🔍 Afișează versetul"):
    selectie = random.choice(versete[emotie_selectata])
    st.markdown("### 📜 Verset ales:")
    st.success(f"**{selectie['referinta']}** – *{selectie['text']}*")

    st.markdown("---")
    st.info("📎 Poți salva acest verset pentru mai târziu sau îl poți împărtăși cu cineva drag.")

# Footer
st.markdown("<br><sub>Aplicație creată cu ❤️ folosind Streamlit.</sub>", unsafe_allow_html=True)
