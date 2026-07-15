import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

try:
    df = pd.read_csv("data/processed/processed_data.csv")

    col1, col2 = st.columns(2)

    col1.metric("Total Transactions", len(df))

    if "isFraud" in df.columns:
        col2.metric("Fraud Transactions", int(df["isFraud"].sum()))

        st.subheader("Fraud Distribution")
        st.bar_chart(df["isFraud"].value_counts())

    if "type" in df.columns:
        st.subheader("Transaction Types")
        st.bar_chart(df["type"].value_counts())

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

except:
    st.warning("Processed dataset not found.")