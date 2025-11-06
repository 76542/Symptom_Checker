# 🩺 AI Symptom-Based Disease Prediction System

## Overview  
The **AI Symptom-Based Disease Prediction System** is a machine learning-based healthcare project designed to predict possible diseases based on user-input symptoms. The model analyzes the given symptoms, identifies potential diseases, and provides general precautionary advice. This project showcases how Artificial Intelligence can support early disease detection and assist in healthcare decision-making.

---

## Features  
- Predicts possible diseases based on symptoms  
- Provides precautionary or advisory suggestions  
- Clean and easy-to-use Streamlit interface  
- Fully functional within a virtual environment  

---

## Tech Stack  
| Component | Technology |
|------------|-------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| User Interface | Streamlit |
| Data Handling | Pandas |
| Model Persistence | Joblib |

---

## Dataset  
It contains mappings between various symptoms and diseases, allowing the model to learn relationships and predict likely health conditions.

> ⚠️ This dataset is used for academic purposes only. It should not be used for professional medical diagnosis.

---

## Project Structure
```bash
symptom_checker/
│
├─ data/
│ └─ symptom_disease.csv
├─ model/
│ ├─ train_model.py
│ └─ disease_model.pkl
├─ app/
│ ├─ app.py
│ └─ disease_helper.py
├─ requirements.txt
└─ README.md
```

---

## Installation & Setup  

### Step 1: Create a Virtual Environment  
```bash
python -m venv env
env\Scripts\activate       # For Windows
# OR
source env/bin/activate    # For Mac/Linux
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Train the Model
```bash
python model/train_model.py
```
### Step 4: Run the Streamlit App
```bash
streamlit run app/app.py
```
---

## How It Works

- The user enters symptoms into the text box (e.g., “fever cough tiredness”).
- The trained model processes these symptoms using text vectorization.
- It predicts the most likely disease using a Random Forest Classifier.
- The app displays the predicted disease along with basic precautionary advice.

---
## Example Output 

### Input: 
```bash
fever cough tiredness
```
### Output:
```bash
Predicted Disease: Common Cold  
Advice: Drink warm fluids, rest, and inhale steam.
```

---

## Model Details

- Algorithm Used: Random Forest Classifier

- Feature Extraction: CountVectorizer

- Evaluation Metric: Accuracy Score

- Model Storage: Saved using joblib for easy reuse

---

## Disclaimer

This project is strictly for educational and demonstration purposes.
It is not intended to provide medical advice or diagnosis.
Always consult a qualified healthcare professional for accurate medical assistance.

---

## Future Improvements

Integration with a larger, more diverse dataset

Multi-disease prediction system

Cloud deployment using Streamlit Cloud

Interactive chatbot integration

Improved UI/UX with better medical insights
