# dashboard/chronos_tab.py

import streamlit as st

def render_chronos_tab():
    st.header("Chronos: Visión Estratégica 2040")

    estrategia = st.radio("Selecciona Estrategia", ["Fortaleza Verde", "Búnker Tecnológico"])

    if estrategia == "Fortaleza Verde":
        st.image("assets/fortaleza_verde.png", caption="Fortaleza Verde")
        st.markdown("""
        Reforzar las zonas menos vulnerables donde la empresa ubicaría sus almacenes logísticos principales, rutas seguras y centros de distribución
        Implementar infraestructuras resilientes al agua (elevación de instalaciones, drenajes naturales, áreas verdes absorbentes) para minimizar el impacto de lluvias extremas
        Las zonas en verde y amarillo periféricas serían candidatas a concentrar la mayor parte de los recursos logísticos porque tienen menor exposición
        """)
    else:
        st.image("assets/bunker_tecnologico.png", caption="Búnker Tecnológico")
        st.markdown("""
        Apostamos por asegurar sus núcleos críticos en zonas de alto riesgo, construyendo instalaciones ultra protegidas
        Estos búnkers serían centros tecnológicos reforzados contra inundaciones:
            Edificios elevados.

            Muros de contención.

            Sistemas automáticos de bombeo y energía autónoma.

            Digitalización total para operar incluso si las rutas físicas quedan interrumpidas.

        Funcionan como refugios tecnológicos, manteniendo activa la red logística aunque la periferia quede afectada
        """)