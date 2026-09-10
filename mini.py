import streamlit as st

st.title("Movie recommendation based on your emotion")
st.write("This is our Mini project")

def recommend_movies(emotion):
    movie_dict = {
        "happy": [
            "The Pursuit of Happiness",
            "Forrest Gump",
            "The Intouchables",
            "Amélie"
        ],
        "sad": [
            "The Green Mile",
            "Schindler's List",
            "Manchester by the Sea",
            "Requiem for a Dream"
        ],
        "excited": [
            "Mad Max: Fury Road",
            "Inception",
            "The Dark Knight",
            "Guardians of the Galaxy",
            "Avengers: Infinity War",
            "Avengers: End Game",
            "Eleven",
            "The Amazing Spiderman",
            "The Amazing Spiderman 2",
            "The Amazing Spiderman 3",
            "Spiderman: No Way Home",
            "spiderman: far from home",
            "Spiderman: HomeComing",
            "The Karate Kid",
            "Shang Chi: The Legend of the Ten Rings"
        ],
        "romantic": [
            "The Notebook",
            "Pride & Prejudice",
            "La La Land",
            "Romeo Juliet",
            "Titanic"
        ],
        "horror": [
            "The Conjuring",
            "The Conjuring 2",
            "The Conjuring 3",
            "The Nun",
            "Get Out",
            "Hereditary",
            "A Quiet Place",
            "Annabelle",
            "Annabelle Creation",
            "Annabelle Comes Home",
            "Sinister",
            "The Medium",
            "Evil Dead",
            "The Ring",
            "The Exorcist",
            "IT",
            "The Grudge",
            "The Grudge 2",
            "Insidious"
        ],
        "adventure": [
            "Indiana Jones: Raiders of the Lost Ark",
            "Jurassic Park",
            "Jurassic Park 2",
            "Jurassic Park 3",
            "Jurassic World Dominion",
            "Jurassic World Rebirth",
            "Godzilla VS Kong",
            "Godzilla X Kong The New Empire",
            "Pirates of the Caribbean",
            "The Lord of the Rings",
            "Jumanji"
            "toy story",
            "toy story 2",
            "toy story 3",
            "lightning mcqueen"
        ]
    }

    emotion = emotion.lower()
    if emotion in movie_dict:
        st.write(f"### Movies to watch when you're feeling **{emotion}**:")
        for movie in movie_dict[emotion]:
            st.write(f"- {movie}")
    else:
        st.write("Sorry, I don't have movie recommendations for that emotion.")

# Streamlit user input
user_emotion = st.selectbox(
    "How are you feeling today?",
    options=["happy", "sad", "excited", "romantic", "horror", "adventure"]
)

if st.button("Get Recommendations"):
    recommend_movies(user_emotion)
