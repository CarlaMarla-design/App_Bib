import streamlit as st
import random
import json

# Încarcă datele din fișierul JSON
try:
    with open("App_Bib.json", "r", encoding="utf-8") as f:
        date_emotii = json.load(f)
except FileNotFoundError:
    st.error("❌ Fișierul 'App_Bib.json' nu a fost găsit.")
    st.stop()

# Configurare pagină
st.set_page_config(page_title="Verset pentru suflet", page_icon="📖", layout="centered")

# Titlu aplicație
st.title("📖 Verset biblic pentru suflet")
st.write("Alege starea ta emoțională și primește un verset și o rugăciune care să-ți aducă mângâiere și speranță.")

# Creează 4 coloane
coloane = st.columns(4)
emotii = list(date_emotii.keys())
emotie_selectata = None

# Afișează 5 emoții în fiecare coloană
for i in range(5):
    for j in range(4):
        index = i + j * 5
        if index < len(emotii):
            if coloane[j].button(emotii[index]):
                emotie_selectata = emotii[index]

# Afișează versetul și rugăciunea dacă s-a selectat o emoție
if emotie_selectata:
    selectie_verset = random.choice(date_emotii[emotie_selectata]["versete"])
    selectie_rugaciune = random.choice(date_emotii[emotie_selectata]["rugaciuni"])

    st.markdown(f"## 🟦 Emoție aleasă: **{emotie_selectata}**")
    st.markdown("### 📜 Verset ales:")
    st.success(f"**{selectie_verset['referinta']}** – *{selectie_verset['text']}*")

    st.markdown("### 🙏 Rugăciune potrivită:")
    st.info(f"*{selectie_rugaciune}*")

    st.markdown("---")
    st.caption("📎 Poți salva acest mesaj pentru mai târziu sau îl poți împărtăși cu cineva drag.")

# Footer
st.markdown("<br><sub>Aplicație creată cu ❤️ folosind Streamlit.</sub>", unsafe_allow_html=True)
