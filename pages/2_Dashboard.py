import streamlit as st
import pandas as pd
import plotly.express as px
from styles import inject_css

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
inject_css()

st.markdown("""
<div class="hero-eyebrow">Dashboard</div>
<h1>Dataset overview</h1>
<p style="color: var(--muted); max-width: 640px;">
A snapshot of the transaction data behind the model — volume, fraud rate, and transaction mix.
</p>
""", unsafe_allow_html=True)
st.write("")

DATA_PATH = "data/processed/cleaned_upi_sample.csv"
TEAL = "#2DD4BF"
CORAL = "#FB7185"
MUTED_SCALE = ["#2DD4BF", "#5EEAD4", "#8CA0C4", "#64748B", "#475569"]

try:
    df = pd.read_csv(DATA_PATH)

    total = len(df)
    fraud_count = int(df["isFraud"].sum()) if "isFraud" in df.columns else None
    fraud_rate = (fraud_count / total * 100) if fraud_count is not None and total else None

    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown(f"""<div class="kpi"><div class="kpi-label">Total Transactions</div>
        <div class="kpi-value">{total:,}</div></div>""", unsafe_allow_html=True)
    with k2:
        val = f"{fraud_count:,}" if fraud_count is not None else "—"
        st.markdown(f"""<div class="kpi"><div class="kpi-label">Fraudulent Transactions</div>
        <div class="kpi-value coral">{val}</div></div>""", unsafe_allow_html=True)
    with k3:
        val = f"{fraud_rate:.3f}%" if fraud_rate is not None else "—"
        st.markdown(f"""<div class="kpi"><div class="kpi-label">Fraud Rate</div>
        <div class="kpi-value teal">{val}</div></div>""", unsafe_allow_html=True)

    st.write("")
    c1, c2 = st.columns(2)

    if "isFraud" in df.columns:
        with c1:
            st.markdown("##### Fraud distribution")
            counts = df["isFraud"].value_counts().rename({0: "Legitimate", 1: "Fraudulent"})
            fig = px.pie(
                values=counts.values, names=counts.index, hole=0.55,
                color=counts.index, color_discrete_map={"Legitimate": TEAL, "Fraudulent": CORAL}
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_color="#F1F5F9", legend_title_text="", margin=dict(t=10, b=10, l=10, r=10)
            )
            st.plotly_chart(fig, use_container_width=True)

    if "type" in df.columns:
        with c2:
            st.markdown("##### Transaction types")
            type_counts = df["type"].value_counts()
            fig2 = px.bar(
                x=type_counts.index, y=type_counts.values,
                color=type_counts.index, color_discrete_sequence=MUTED_SCALE
            )
            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_color="#F1F5F9", showlegend=False,
                xaxis_title="", yaxis_title="Count", margin=dict(t=10, b=10, l=10, r=10)
            )
            st.plotly_chart(fig2, use_container_width=True)

    st.write("")
    st.markdown("##### Dataset preview")
    st.dataframe(df.head(), use_container_width=True)

except FileNotFoundError:
    st.warning(f"Processed dataset not found at `{DATA_PATH}`. "
               f"Make sure this file is included in your deployment.")
except pd.errors.EmptyDataError:
    st.error(f"The file at `{DATA_PATH}` is empty or unreadable.")
except Exception as e:
