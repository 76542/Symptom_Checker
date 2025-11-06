import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("data/symptom_disease.csv")

X = data["symptoms"]
y = data["disease"]

# Pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('clf', RandomForestClassifier())
])

# Train
model.fit(X, y)

# Save model
joblib.dump(model, "model/disease_model.pkl")

print("Model trained & saved successfully!")
