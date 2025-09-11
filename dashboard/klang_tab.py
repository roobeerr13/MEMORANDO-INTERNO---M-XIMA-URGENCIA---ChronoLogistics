# dashboard/klang_tab.py

import streamlit as st
import json

def render_klang_tab():
    st.header("K-Lang: Manual de Batalla Interactivo")

    with open("protocols.json") as f:
        protocols = json.load(f)

    protocolo = st.selectbox("Selecciona Protocolo", list(protocols.keys()))
    ficha = protocols[protocolo]

    st.subheader(f"🔧 Disparador: {ficha['disparador']}")
    st.markdown("**📋 Acciones a ejecutar:**")
    for accion in ficha["acciones"]:
        st.markdown(f"- {accion}")

    st.divider()
    st.subheader("🧪 Simulador de Protocolos")

    viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 30)
    inundacion = st.slider("Nivel de Inundación (cm)", 0, 500, 100)

    if viento > 90:
        st.markdown("## 🟥 PROTOCOLO ACTIVO: CÓDIGO ROJO - TITÁN")
    elif inundacion > 300:
        st.markdown("## 🟦 PROTOCOLO ACTIVO: RENACIMIENTO")
    elif viento < 50:
        st.markdown("## 🟩 PROTOCOLO ACTIVO: VÍSPERA")
    else:
        st.markdown("## 🟨 SIN PROTOCOLO ACTIVO")