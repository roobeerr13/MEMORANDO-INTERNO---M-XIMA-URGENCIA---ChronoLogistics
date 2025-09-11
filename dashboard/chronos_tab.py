# dashboard/chronos_tab.py

import streamlit as st

def render_chronos_tab():
    st.header("Chronos: Visión Estratégica 2040")

    estrategia = st.radio("Selecciona Estrategia", ["Fortaleza Verde", "Búnker Tecnológico"])

    if estrategia == "Fortaleza Verde":
        st.image("assets/fortaleza_verde.png", caption="Fortaleza Verde")
        st.markdown("""
        **Defensa Estratégica:**  
        Madrid se transforma en un bastión ecológico, resiliente y autosuficiente.  
        Esta visión prioriza la sostenibilidad, la descentralización energética y la protección climática como pilares de nuestra supervivencia.
        """)
    else:
        st.image("assets/bunker_tecnologico.png", caption="Búnker Tecnológico")
        st.markdown("""
        **Defensa Estratégica:**  
        Infraestructura blindada, IA avanzada y control total del entorno urbano.  
        Esta visión garantiza continuidad operativa en escenarios extremos y posiciona a ChronoLogistics como líder en resiliencia tecnológica.
        """)