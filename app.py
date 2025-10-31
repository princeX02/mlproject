import os
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn

app = FastAPI(title="Student Exam Performance Indicator")

# Input schema (same as frontend)
class InputData(BaseModel):
    gender: str
    ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: float
    writing_score: float


# Load model and preprocessor
with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("artifacts/proprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Welcome to the Student Exam Performance Prediction API!"}


@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # ✅ Rename column to match what the preprocessor expects
        # (your preprocessor was trained with 'race_ethnicity')
        input_df.rename(columns={'ethnicity': 'race_ethnicity'}, inplace=True)

        # Transform using preprocessor
        transformed = preprocessor.transform(input_df)

        # Predict math score
        prediction = model.predict(transformed)

        return {"predicted_math_score": round(float(prediction[0]), 2)}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
