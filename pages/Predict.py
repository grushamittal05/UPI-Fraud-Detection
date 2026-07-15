import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Fraud Prediction",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 UPI Fraud Detection")

# ---------------- Load Model ----------------
model = joblib.load("models/catboost_model.pkl")

st.markdown("Enter the transaction details below.")

# ---------------- User Inputs ----------------
step = st.number_input(
    "Step",
    min_value=1,
    value=1
)

transaction_type = st.selectbox(
    "Transaction Type",
    ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
)

type_mapping = {
    "CASH_IN": 0,
    "CASH_OUT": 1,
    "DEBIT": 2,
    "PAYMENT": 3,
    "TRANSFER": 4
}

transaction_type = type_mapping[transaction_type]

amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Old Balance (Sender)",
    min_value=0.0,
    value=5000.0
)

newbalanceOrig = st.number_input(
    "New Balance (Sender)",
    min_value=0.0,
    value=4000.0
)

oldbalanceDest = st.number_input(
    "Old Balance (Receiver)",
    min_value=0.0,
    value=1000.0
)

newbalanceDest = st.number_input(
    "New Balance (Receiver)",
    min_value=0.0,
    value=2000.0
)

isFlaggedFraud = st.selectbox(
    "Is Flagged Fraud",
    [0, 1]
)

# ---------------- Prediction ----------------
if st.button("🚀 Predict"):

    input_data = pd.DataFrame({
        "step": [step],
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest],
        "isFlaggedFraud": [isFlaggedFraud]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")

    st.metric("Fraud Probability", f"{probability:.2%}")

    st.subheader("Input Data")

    st.dataframe(input_data)