import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Fraud Prediction")

model = joblib.load("models/catboost_model.pkl")

type = st.selectbox(
    "Transaction Type",
    ["PAYMENT","TRANSFER","CASH_OUT","DEBIT","CASH_IN"]
)

amount = st.number_input("Amount",0.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)",0.0)

newbalanceOrig = st.number_input("New Balance (Sender)",0.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)",0.0)

newbalanceDest = st.number_input("New Balance (Receiver)",0.0)

if st.button("Predict"):

    data = pd.DataFrame({

        "type":[type],
        "amount":[amount],
        "oldbalanceOrg":[oldbalanceOrg],
        "newbalanceOrig":[newbalanceOrig],
        "oldbalanceDest":[oldbalanceDest],
        "newbalanceDest":[newbalanceDest]

    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")