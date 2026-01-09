import streamlit as st
from deep_translator import GoogleTranslator
from bot_logic import librarian_bot

st.set_page_config(page_title="School Librarian Bot", page_icon="📚")

st.title("📚 School Librarian AI Bot")

language = st.selectbox("Select Language", ["English", "Hindi", "Punjabi"])
user_input = st.text_input("Ask your question")

lang_map = {"English": "en", "Hindi": "hi", "Punjabi": "pa"}

def translate(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)

if st.button("Ask"):
    query = user_input
    if language != "English":
        query = translate(user_input, "en")

    response = librarian_bot(query)

    if language != "English":
        response = translate(response, lang_map[language])

    st.text_area("Bot Response", response, height=200)

