import streamlit as st
import requests
import base64

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55);
            z-index: 0;
            pointer-events: none;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_background("starwars_background.jpg")


############################################
API_URL = "http://127.0.0.1:8000"


def layout():
    st.markdown("# Cool Movies")

    movie_string = st.text_input("Give a statement and it will give back a movie")

    movie = requests.post(f"{API_URL}/movie", json={"prompt": movie_string}).json()

    if movie:
        st.write(movie)

    genre = st.selectbox(
        "Choose genre", options=["action", "comedy", "cartoon", "adventure", "romance"]
    )

    movies = requests.get(f"{API_URL}/movies?genre={genre}").json()

    st.dataframe(movies)


if __name__ == "__main__":
    layout()