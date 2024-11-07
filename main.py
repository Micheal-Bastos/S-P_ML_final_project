from fastapi import FastAPI
import numpy as np
import pandas as pd  # Import Pandas pour créer un DataFrame
import joblib

# Initialiser l'application FastAPI
app = FastAPI()

# Charger le modèle de machine learning
model = joblib.load("best_model.pkl")

# Définir un endpoint pour faire une prédiction directement avec des données codées en dur
@app.get("/predict-from-data/")
def predict_from_data():
    # Créer un tableau des données codées en dur (similaire à ce qu'il y aurait dans le JSON)
    data = {
        "Age": 41,
        "DailyRate": 1102,
        "DistanceFromHome": 1,
        "Education": 2,
        "EmployeeCount": 1,
        "EmployeeNumber": 1,
        "EnvironmentSatisfaction": 2,
        "HourlyRate": 94,
        "JobInvolvement": 3,
        "JobLevel": 2,
        "JobSatisfaction": 4,
        "MonthlyIncome": 5993,
        "MonthlyRate": 19479,
        "NumCompaniesWorked": 8,
        "PercentSalaryHike": 11,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 1,
        "StandardHours": 80,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 8,
        "TrainingTimesLastYear": 0,
        "WorkLifeBalance": 1,
        "YearsAtCompany": 6,
        "YearsInCurrentRole": 4,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 5,
        # Les colonnes catégorielles qui manquaient
        "JobRole": "Sales Executive",
        "Over18": "Y",
        "OverTime": "Yes",
        "Gender": "Female",
        "Department": "Sales",
        "EducationField": "Life Sciences",
        "BusinessTravel": "Travel_Rarely",
        "MaritalStatus": "Single",
        # Features d'ingénierie
        "TotalWorkingYears_AgeRatio": 8 / 41,
        "YearsAtCompany_AgeRatio": 6 / 41
    }

    # Convertir les données en DataFrame Pandas avec les colonnes appropriées
    df = pd.DataFrame([data])

    # Faire la prédiction
    prediction = model.predict(df)

    # Retourner la prédiction
    return {"prediction": int(prediction[0])}