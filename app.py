from textblob import TextBlob
import streamlit as st

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Happy"
    elif analysis.sentiment.polarity < 0:
        return "Sad / Stressed"
    else:
        return "Neutral"

def recommend_task(mood):
    if mood == "Happy":
        return "Creative tasks / Team collaboration"
    elif mood == "Sad / Stressed":
        return "Light work / Take a break"
    else:
        return "Routine tasks"

st.title("AI-Powered Task Optimizer")

user_input = st.text_area("Enter employee text:")

if st.button("Analyze"):
    mood = get_sentiment(user_input)
    task = recommend_task(mood)

    st.write("### Mood:", mood)
    st.write("### Recommended Task:", task)

    if mood == "Sad / Stressed":
        st.warning("⚠️ Alert: Employee may need support")   
