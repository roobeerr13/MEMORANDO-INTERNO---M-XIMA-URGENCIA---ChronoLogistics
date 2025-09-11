# dashboard/utils.py

import streamlit as st
import json

def cargar_protocolos(ruta="protocols.json"):
    """
    Carga el archivo JSON con los protocolos de emergencia.
    """
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_ficha_protocolo(protocolo, protocolos):
    """
    Muestra la ficha técnica de un protocolo específico.
    """
    ficha = protocolos[protocolo]
    st.subheader(f"🔧 Disparador: {ficha['disparador']}")
    st.markdown("**📋 Acciones a ejecutar:**")
    for accion in ficha["acciones"]:
        st.markdown(f"- {accion}")

def mostrar_alerta_protocolo(viento, inundacion):
    """
    Determina y muestra qué protocolo está activo según los datos simulados.
    """
    if viento > 90:
        st.markdown("## 🟥 PROTOCOLO ACTIVO: CÓDIGO ROJO - TITÁN")
    elif inundacion > 300:
        st.markdown("## 🟦 PROTOCOLO ACTIVO: RENACIMIENTO")
    elif viento < 50:
        st.markdown("## 🟩 PROTOCOLO ACTIVO: VÍSPERA")
    else:
        st.markdown("## 🟨 SIN PROTOCOLO ACTIVO")