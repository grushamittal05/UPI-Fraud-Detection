import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Project")

st.markdown("""
# UPI Fraud Detection System

## Overview

This project uses Machine Learning to detect fraudulent UPI transactions.

---

## Dataset

PaySim Mobile Money Transaction Dataset

---

## Technologies

- Python
- Pandas
- Scikit-learn
- CatBoost
- XGBoost
- Streamlit
- Joblib

---

## Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- CatBoost

---

## Best Model

⭐ CatBoost

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

## Developed By

Computer Science Student
""")