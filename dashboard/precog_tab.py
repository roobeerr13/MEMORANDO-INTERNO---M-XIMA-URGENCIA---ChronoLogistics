# dashboard/precog_tab.py

import streamlit as st
from precog import predecir_riesgo

def render_precog_tab():
    st.header("Precog: Monitor de Riesgo Táctico")
    st.image("assets/mapa_calor.png", caption="Triángulo del Peligro")

    velocidad = st.slider("Velocidad Media (km/h)", 0, 150, 50)
    lluvia = st.slider("Intensidad de Lluvia (mm/h)", 0, 100, 20)

    riesgo = predecir_riesgo(velocidad, lluvia)
    st.metric("Nivel de Riesgo en Cascada", riesgo)