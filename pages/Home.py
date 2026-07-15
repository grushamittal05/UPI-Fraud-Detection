import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Home")

st.markdown("""
# 💳 UPI Fraud Detection System

## Objective

To detect fraudulent UPI transactions using Machine Learning.

---

## Features

✅ Real-time Fraud Prediction

✅ Interactive Dashboard

✅ High Accuracy CatBoost Model

✅ Easy-to-use Interface

---

## Models Compared

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- ⭐ CatBoost

---

### Dataset

PaySim Mobile Money Transaction Dataset
""")

st.success("Use the sidebar to navigate.")