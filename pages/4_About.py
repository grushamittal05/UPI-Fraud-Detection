import streamlit as st
from styles import inject_css

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
inject_css()

st.markdown("""
<div class="hero-eyebrow">About</div>
<h1>How this project works</h1>
<p style="color: var(--muted); max-width: 640px;">
An end-to-end machine learning pipeline for detecting fraudulent UPI transactions,
built on the PaySim mobile-money simulation dataset.
</p>
""", unsafe_allow_html=True)
st.write("")

st.markdown("#### Pipeline")
steps = [
    ("01", "Data collection", "PaySim mobile-money transaction dataset."),
    ("02", "Preprocessing", "Cleaning, encoding the transaction type, handling class imbalance with SMOTE."),
    ("03", "Model training", "Logistic Regression, Decision Tree, Random Forest, XGBoost, and CatBoost."),
    ("04", "Evaluation", "Compared on accuracy, precision, recall, F1-score, and ROC-AUC."),
    ("05", "Model selection", "CatBoost selected as the best performer."),
    ("06", "Deployment", "Served through this Streamlit interface for real-time scoring."),
]
with st.container(border=True):
    for num, title, desc in steps:
        st.markdown(f"""
        <div class="step">
            <div class="step-num">{num}</div>
            <div class="step-body"><h4>{title}</h4><p>{desc}</p></div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
c1, c2 = st.columns(2)

with c1:
    st.markdown("#### Technologies")
    st.markdown(
        '<span class="badge badge-neutral">Python</span>'
        '<span class="badge badge-neutral">Pandas</span>'
        '<span class="badge badge-neutral">Scikit-learn</span>'
        '<span class="badge badge-teal">CatBoost</span>'
        '<span class="badge badge-neutral">XGBoost</span>'
        '<span class="badge badge-neutral">Streamlit</span>'
        '<span class="badge badge-neutral">Joblib</span>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown("#### Evaluation metrics")
    st.markdown(
        '<span class="badge badge-neutral">Accuracy</span>'
        '<span class="badge badge-neutral">Precision</span>'
        '<span class="badge badge-neutral">Recall</span>'
        '<span class="badge badge-neutral">F1-Score</span>'
        '<span class="badge badge-teal">ROC-AUC</span>',
        unsafe_allow_html=True
    )

st.write("")
st.caption("Developed by a Computer Science student.")