import streamlit as st
from dashboard.precog_tab import render_precog_tab
from dashboard.chronos_tab import render_chronos_tab
from dashboard.klang_tab import render_klang_tab

st.set_page_config(page_title="ChronoLogistics Crisis Dashboard", layout="wide")

tab1, tab2, tab3 = st.tabs(["Precog", "Chronos", "K-Lang"])

with tab1:
    render_precog_tab()

with tab2:
    render_chronos_tab()

with tab3:
    render_klang_tab()