import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Code Alchemist - The Web Dev Mad Hatter")
st.write("Enter your web code and watch it transform into something... else.")

code = st.text_area("Enter your web code:", "<div><h1>Hello, World!</h1></div>")

conversion_type = st.selectbox(
    "Choose your conversion:",
    [
        "Retrofy",
        "Abstractify",
        "Language Roulette",
        "Emotion Injection",
        "Quantum Optimization",
        "Aesthetic Chaos",
        "Pirate Code",
        "AI Code Commentary",
        "Code to Song",
        "Code to Poetry",
    ],
)

if st.button("Transmute Code!"):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        if conversion_type == "Retrofy":
            prompt = f"Convert this modern web code to HTML 3.2 with inline styles and table layouts: {code}"
        elif conversion_type == "Abstractify":
            prompt = f"Create a visually abstract WebGL representation of this code: {code}"
        elif conversion_type == "Language Roulette":
            languages = ["React", "Svelte", "Elm", "Vue", "Angular"]
            random_language = random.choice(languages)
            prompt = f"Convert this code to {random_language} and then back to HTML: {code}"
        elif conversion_type == "Emotion Injection":
            prompt = f"Inject emotional styling and animations into this code: {code}"
        elif conversion_type == "Quantum Optimization":
            prompt = f"Quantum optimize this web code for maximum performance: {code}"
        elif conversion_type == "Aesthetic Chaos":
            prompt = f"Transform this code into a maximalist, neon-drenched design: {code}"
        elif conversion_type == "Pirate Code":
            prompt = f"Convert this code to a pirate-themed version: {code}"
        elif conversion_type == "AI Code Commentary":
            prompt = f"Convert this code and provide a comical commentary: {code}"
        elif conversion_type == "Code to Song":
            prompt = f"Convert the logic of this code into a musical representation: {code}"
        elif conversion_type == "Code to Poetry":
            prompt = f"Transform this code into a poem: {code}"
        else:
            prompt = f"Convert this code: {code}"

        response = model.generate_content(prompt)
        st.write("Transmuted Code:")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
