import streamlit as st

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="UPI Fraud Detection",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Main Page --------------------
st.title("💳 UPI Fraud Detection System")

st.markdown("""
Welcome to the **UPI Fraud Detection System**.

This application uses **Machine Learning** to identify whether a UPI transaction is **Fraudulent** or **Legitimate**.

---

### 🚀 Features
- 🔍 Predict fraudulent UPI transactions
- 📊 Interactive dashboard with dataset insights
- 🤖 CatBoost Machine Learning model
- 📈 Model evaluation and performance analysis

---

### 📂 Navigate Using the Sidebar

Select any page from the left sidebar:

- 🏠 **Home** – Project overview
- 📊 **Dashboard** – Dataset statistics and visualizations
- 🔍 **Predict** – Predict fraud for a transaction
- ℹ️ **About** – Project details and technologies

---

### 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- CatBoost
- Streamlit
""")

st.success("👈 Choose a page from the sidebar to get started.")