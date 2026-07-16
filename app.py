import streamlit as st
from styles import inject_css

st.set_page_config(
    page_title="UPI Fraud Detection",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)
inject_css()

# -------------------- Hero --------------------
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Real-time transaction screening</div>
    <h1>Every UPI transaction, scanned before it settles.</h1>
    <p>A CatBoost classifier trained on the PaySim mobile-money dataset flags fraudulent
    transactions in milliseconds — compare it against four other models, explore the data,
    and try it on a live transaction below.</p>
    <div class="radar"><div class="radar-dot"></div></div>
</div>
""", unsafe_allow_html=True)

# -------------------- Nav cards --------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("#### 🏠 Home")
        st.caption("Project overview and objectives")
        st.page_link("pages/1_Home.py", label="Open", icon="➡️")

with col2:
    with st.container(border=True):
        st.markdown("#### 📊 Dashboard")
        st.caption("Dataset stats and fraud distribution")
        st.page_link("pages/2_Dashboard.py", label="Open", icon="➡️")

with col3:
    with st.container(border=True):
        st.markdown("#### 🔍 Predict")
        st.caption("Score a transaction in real time")
        st.page_link("pages/3_Predict.py", label="Open", icon="➡️")

with col4:
    with st.container(border=True):
        st.markdown("#### ℹ️ About")
        st.caption("Models, metrics, and tech stack")
        st.page_link("pages/4_About.py", label="Open", icon="➡️")

st.write("")
st.markdown('<span class="badge badge-teal">CatBoost · Best Model</span>'
            '<span class="badge badge-neutral">PaySim Dataset</span>'
            '<span class="badge badge-neutral">Scikit-learn</span>'
            '<span class="badge badge-neutral">Streamlit</span>',
            unsafe_allow_html=True)