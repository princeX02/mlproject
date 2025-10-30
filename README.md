## End to End Machine learning Projects
# 🎓 Student Exam Performance Predictor

This project predicts a student's **Math Score** using **FastAPI** for the backend and **Streamlit** for the frontend.

---



### Project Structure

```
MLPROJECT/
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── pipeline/
│ │ ├── predict_pipeline.py
│ │ └── train_pipeline.py
│ │
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
│
├── templates/
│ └── index.py # Streamlit Frontend
│
├── app.py # FastAPI Backend
├── requirements.txt
├── setup.py
└── README.md
```

### To run this project locally, follow these steps:

### git Clone the Repository
```bash
git clone https://github.com/princechaudhary/MLPROJECT.git
cd MLPROJECT
```


### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # For Mac/Linux
venv\Scripts\activate           # For Windows


```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
``` 

### 3️⃣ Run FastAPI Backend
```bash
uvicorn app:app --reload
``` 

### 4️⃣ Run Streamlit Frontend
```bash
streamlit run templates/index.py
``` 

### 5️⃣ Access the Application
Open your web browser and navigate to `http://localhost:8501` to access the Streamlit frontend. 

### 6️⃣ API Documentation
For API documentation, navigate to `http://localhost:8000/docs` to access the Swagger UI provided by FastAPI.   

### 7️⃣ Project Authors
- Prince Chaudhary - [GitHub](https://github.com/princechaudhary)
- B.Tech CSE | Aspiring Data Scientist | ML Enthusiast
