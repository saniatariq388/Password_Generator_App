
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import random 
import string


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits  # add numbers

    if use_special:
        characters += string.punctuation  # add special characters (! , @, # ,$, %, &, )

    return ''.join(random.choice(characters) for _ in range(length))


st.title("🔐 Password Generator 🔑")

length = st.slider("📏 Password Length", min_value=6, max_value=30, value=12)

use_digits = st.checkbox("🔢 Include Digits")

use_special = st.checkbox("💥 Include Special Characters")

if st.button("🎲 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.markdown(f"<h2 style='text-align: center; font-size: 40px;'>🔑 {password} 🔑</h2>", unsafe_allow_html=True)

st.write("---------------------------------")

st.write("🚀 Built with 🤍 by [Sania Tariq]")

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

genai.configure(api_key=API_KEY)

st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://i.pinimg.com/736x/5c/f7/12/5cf712daad50b04c91f31aab21d53456.jpg");
            background-size: cover;
            background-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Ask a Question to LLM 🧠")
user_question = st.text_input("💡 Enter your question:")

if st.button("📩 Get Answer"):
    if user_question.strip():
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        with st.spinner("⚡ Generating your answer..."):
            response = model.generate_content(user_question)
        st.subheader("💡 Your Answer:")
        st.write(response.text.strip())
    else:
        st.warning("⚠️ Please enter a question before submitting.")