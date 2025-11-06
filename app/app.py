import streamlit as st
import joblib
from disease_helper import advice_dict

st.set_page_config(page_title="AI Symptom Checker")

model = joblib.load("model/disease_model.pkl")

st.title("🩺 AI Symptom-Based Disease Predictor")

symptoms = st.text_input("Enter symptoms (example: fever cough tiredness):")

if st.button("Predict"):
    if symptoms.strip() == "":
        st.warning("Please enter symptoms first.")
    else:
        prediction = model.predict([symptoms])[0]

        st.success(f"🔍 Possible Disease: **{prediction}**")
        st.info(f"🩻 Advice: {advice_dict.get(prediction,'Consult a doctor.')}")
