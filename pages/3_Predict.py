import streamlit as st
import pandas as pd
import joblib
import os
from styles import inject_css

st.set_page_config(page_title="Fraud Prediction", page_icon="🔍", layout="wide")
inject_css()

st.markdown("""
<div class="hero-eyebrow">Predict</div>
<h1>Check a transaction</h1>
<p style="color: var(--muted); max-width: 640px;">
Enter the transaction details and run it through the CatBoost model.
</p>
""", unsafe_allow_html=True)
st.write("")

MODEL_PATH = "models/catboost_model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

model = load_model()

if model is None:
    st.error(f"Model file not found at `{MODEL_PATH}`. "
             f"Make sure `catboost_model.pkl` is committed to your repo at this path.")
    st.stop()

type_mapping = {"CASH_IN": 0, "CASH_OUT": 1, "DEBIT": 2, "PAYMENT": 3, "TRANSFER": 4}

left, right = st.columns([1.1, 1])

with left:
    with st.container(border=True):
        st.markdown("##### Transaction details")

        r1c1, r1c2 = st.columns(2)
        step = r1c1.number_input("Step", min_value=1, value=1)
        transaction_type = r1c2.selectbox("Transaction Type", list(type_mapping.keys()))

        amount = st.number_input("Amount", min_value=0.0, value=1000.0)

        r2c1, r2c2 = st.columns(2)
        oldbalanceOrg = r2c1.number_input("Old Balance (Sender)", min_value=0.0, value=5000.0)
        newbalanceOrig = r2c2.number_input("New Balance (Sender)", min_value=0.0, value=4000.0)

        r3c1, r3c2 = st.columns(2)
        oldbalanceDest = r3c1.number_input("Old Balance (Receiver)", min_value=0.0, value=1000.0)
        newbalanceDest = r3c2.number_input("New Balance (Receiver)", min_value=0.0, value=2000.0)

        isFlaggedFraud = st.selectbox("Is Flagged Fraud (system flag)", [0, 1])

        run = st.button("🚀 Scan Transaction", type="primary", use_container_width=True)

with right:
    with st.container(border=True):
        st.markdown("##### Result")

        if not run:
            st.markdown("""
            <div class="result-wrap">
                <div class="result-ring idle">—</div>
                <div class="verdict-label" style="color: var(--muted);">Awaiting scan</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            input_data = pd.DataFrame({
                "step": [step],
                "type": [type_mapping[transaction_type]],
                "amount": [amount],
                "oldbalanceOrg": [oldbalanceOrg],
                "newbalanceOrig": [newbalanceOrig],
                "oldbalanceDest": [oldbalanceDest],
                "newbalanceDest": [newbalanceDest],
                "isFlaggedFraud": [isFlaggedFraud]
            })

            try:
                prediction = model.predict(input_data)[0]
                probability = model.predict_proba(input_data)[0][1]

                if prediction == 1:
                    st.markdown(f"""
                    <div class="result-wrap">
                        <div class="result-ring fraud">{probability*100:.0f}%</div>
                        <div class="verdict-label fraud">🚨 Fraudulent Transaction</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="result-wrap">
                        <div class="result-ring safe">{probability*100:.0f}%</div>
                        <div class="verdict-label safe">✅ Legitimate Transaction</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.write("")
                rows = "".join(
                    f"<tr><td>{k}</td><td>{v}</td></tr>"
                    for k, v in {
                        "step": step, "type": transaction_type, "amount": amount,
                        "oldbalanceOrg": oldbalanceOrg, "newbalanceOrig": newbalanceOrig,
                        "oldbalanceDest": oldbalanceDest, "newbalanceDest": newbalanceDest,
                        "isFlaggedFraud": isFlaggedFraud
                    }.items()
                )
                st.markdown(f'<table class="mono-table">{rows}</table>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Prediction failed: {e}")
                st.info("This usually means the input columns/order don't match what the model expects.")