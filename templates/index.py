import streamlit as st
import requests

# FastAPI endpoint
# FASTAPI_URL = "http://127.0.0.1:8000/predict"
# FASTAPI_URL = "https://student-api.onrender.com/predict"
FASTAPI_URL = "https://mlproject-yg6x.onrender.com/predict"



st.set_page_config(page_title="Student Exam Performance Indicator", layout="centered")

st.title("🎓 Student Exam Performance Indicator")
st.markdown("Enter student details below to predict the **Math Score**.")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
)
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", min_value=0.0, max_value=100.0, step=1.0)
writing_score = st.number_input("Writing Score", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Predict Math Score"):
    input_data = {
        "gender": gender,
        "ethnicity": ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation_course,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    try:
        response = requests.post(FASTAPI_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            if "predicted_math_score" in result:
                st.success(f"📘 Predicted Math Score: **{result['predicted_math_score']}**")
            else:
                st.error(f"⚠️ Error: {result.get('error', 'Unknown error')}")
        else:
            st.error(f"Server Error: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Failed to connect to backend: {e}")

