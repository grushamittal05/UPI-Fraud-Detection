import streamlit as st
from styles import inject_css

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")
inject_css()

st.markdown("""
<div class="hero-eyebrow">Home</div>
<h1>UPI Fraud Detection System</h1>
<p style="color: var(--muted); max-width: 640px; font-size: 1.02rem;">
Detecting fraudulent UPI transactions using machine learning, trained and benchmarked
on the PaySim mobile-money simulation dataset.
</p>
""", unsafe_allow_html=True)

st.write("")
c1, c2, c3, c4 = st.columns(4)
features = [
    ("⚡", "Real-Time Prediction", "Score a single transaction instantly from the Predict page."),
    ("📊", "Interactive Dashboard", "Explore fraud distribution and transaction types in the dataset."),
    ("🎯", "High-Accuracy Model", "CatBoost outperformed 4 other models on recall and ROC-AUC."),
    ("🧩", "Simple Interface", "No setup needed — just enter transaction details and check."),
]
for col, (icon, title, desc) in zip([c1, c2, c3, c4], features):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{icon} {title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown("#### Models compared")
st.markdown(
    '<span class="badge badge-neutral">Logistic Regression</span>'
    '<span class="badge badge-neutral">Decision Tree</span>'
    '<span class="badge badge-neutral">Random Forest</span>'
    '<span class="badge badge-neutral">XGBoost</span>'
    '<span class="badge badge-teal">⭐ CatBoost — best model</span>',
    unsafe_allow_html=True
)

st.write("")
st.markdown("#### Dataset")
st.markdown('<span class="badge badge-neutral">PaySim Mobile Money Transaction Dataset</span>', unsafe_allow_html=True)

st.write("")
st.info("👈 Use the sidebar, or go back to the main page, to navigate between sections.")