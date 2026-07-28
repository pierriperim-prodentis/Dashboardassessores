import streamlit as st
import os

st.set_page_config(
    page_title="Relatório ARP 2025 vs 2026",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove padding
st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    header { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
</style>
""", unsafe_allow_html=True)

# Load and display HTML
html_path = os.path.join(os.path.dirname(__file__), "relatorio.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=900, scrolling=True)
