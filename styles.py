"""
Shared design system for the UPI Fraud Detection app.
Import inject_css() at the top of every page to apply the theme.

Palette:
  bg          #0B1120  ink navy — app background
  surface     #121A2C  card background
  surface-alt #1A2540  hover / nested surface
  border      #24304D  hairline borders
  text        #F1F5F9  primary text
  muted       #8CA0C4  secondary text
  teal        #2DD4BF  "verified / legitimate" signal
  coral       #FB7185  "fraud / alert" signal

Type:
  Display  Space Grotesk  — headings
  Body     Inter          — paragraphs, UI copy
  Mono     JetBrains Mono — transaction data, amounts, IDs, metrics
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #0B1120;
    --surface: #121A2C;
    --surface-alt: #1A2540;
    --border: #24304D;
    --text: #F1F5F9;
    --muted: #8CA0C4;
    --teal: #2DD4BF;
    --coral: #FB7185;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3, h4 { font-family: 'Space Grotesk', sans-serif !important; letter-spacing: -0.01em; }

[data-testid="stSidebar"] {
    background: var(--surface);
    border-right: 1px solid var(--border);
}

[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace;
}

/* ---------- Hero banner ---------- */
.hero {
    position: relative;
    background: linear-gradient(135deg, #0B1120 0%, #142038 55%, #1B2A4A 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2.75rem 3rem;
    overflow: hidden;
    margin-bottom: 1.75rem;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    color: var(--teal);
    font-size: 0.8rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.hero h1 {
    font-size: 2.4rem;
    margin: 0 0 0.6rem 0;
    color: var(--text);
}
.hero p {
    color: var(--muted);
    font-size: 1.05rem;
    max-width: 640px;
    margin: 0;
}

/* Signature element: scanning radar ring, evokes real-time transaction scanning */
.radar {
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 2px solid rgba(45, 212, 191, 0.35);
}
.radar::before, .radar::after {
    content: "";
    position: absolute;
    inset: -22px;
    border-radius: 50%;
    border: 1px solid rgba(45, 212, 191, 0.18);
}
.radar::after { inset: -44px; border-color: rgba(45, 212, 191, 0.08); }
.radar-dot {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: radial-gradient(circle at center, rgba(45,212,191,0.9), transparent 70%);
    animation: sweep 2.4s ease-in-out infinite;
}
@keyframes sweep {
    0%   { opacity: 0.25; transform: scale(0.85); }
    50%  { opacity: 0.9;  transform: scale(1.05); }
    100% { opacity: 0.25; transform: scale(0.85); }
}
@media (max-width: 900px) { .radar { display: none; } }
@media (prefers-reduced-motion: reduce) { .radar-dot { animation: none; opacity: 0.6; } }

/* ---------- Cards ---------- */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.5rem;
    height: 100%;
}
.card h4 { margin: 0 0 0.4rem 0; color: var(--text); }
.card p { color: var(--muted); font-size: 0.92rem; margin: 0; }

/* ---------- KPI cards ---------- */
.kpi { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 1.1rem 1.3rem; }
.kpi-label { color: var(--muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; }
.kpi-value { font-family: 'JetBrains Mono', monospace; font-size: 1.9rem; font-weight: 600; color: var(--text); margin-top: 0.2rem; }
.kpi-value.teal { color: var(--teal); }
.kpi-value.coral { color: var(--coral); }

/* ---------- Badges ---------- */
.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 999px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    margin: 0.2rem 0.35rem 0.2rem 0;
}
.badge-teal { background: rgba(45,212,191,0.10); color: var(--teal); border: 1px solid rgba(45,212,191,0.35); }
.badge-coral { background: rgba(251,113,133,0.10); color: var(--coral); border: 1px solid rgba(251,113,133,0.35); }
.badge-neutral { background: var(--surface-alt); color: var(--muted); border: 1px solid var(--border); }

/* ---------- Pipeline steps (About page) ---------- */
.step { display: flex; gap: 1rem; padding: 0.9rem 0; border-bottom: 1px solid var(--border); }
.step:last-child { border-bottom: none; }
.step-num { font-family: 'JetBrains Mono', monospace; color: var(--teal); font-weight: 600; min-width: 2.2rem; }
.step-body h4 { margin: 0; font-size: 1rem; }
.step-body p { margin: 0.15rem 0 0 0; color: var(--muted); font-size: 0.88rem; }

/* ---------- Result ring (Predict page) ---------- */
.result-wrap { text-align: center; padding: 1rem 0; }
.result-ring {
    width: 132px; height: 132px; border-radius: 50%;
    margin: 0 auto 1rem auto;
    display: flex; align-items: center; justify-content: center;
    font-family: 'JetBrains Mono', monospace; font-size: 1.5rem; font-weight: 600;
}
.result-ring.idle { border: 2px dashed var(--border); color: var(--muted); }
.result-ring.safe { border: 3px solid var(--teal); color: var(--teal); animation: pulse-teal 2.2s infinite; }
.result-ring.fraud { border: 3px solid var(--coral); color: var(--coral); animation: pulse-coral 1.1s infinite; }
@keyframes pulse-teal { 0%{box-shadow:0 0 0 0 rgba(45,212,191,.45);} 70%{box-shadow:0 0 0 16px rgba(45,212,191,0);} 100%{box-shadow:0 0 0 0 rgba(45,212,191,0);} }
@keyframes pulse-coral { 0%{box-shadow:0 0 0 0 rgba(251,113,133,.5);} 70%{box-shadow:0 0 0 20px rgba(251,113,133,0);} 100%{box-shadow:0 0 0 0 rgba(251,113,133,0);} }
@media (prefers-reduced-motion: reduce) { .result-ring { animation: none !important; } }

.verdict-label { font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; font-weight: 600; }
.verdict-label.safe { color: var(--teal); }
.verdict-label.fraud { color: var(--coral); }

.mono-table { width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }
.mono-table td { padding: 0.4rem 0.6rem; border-bottom: 1px solid var(--border); color: var(--text); }
.mono-table td:first-child { color: var(--muted); }
</style>
"""


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)