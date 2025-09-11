from dashboard.utils import cargar_protocolos, mostrar_ficha_protocolo, mostrar_alerta_protocolo

def render_klang_tab():
    st.header("K-Lang: Manual de Batalla Interactivo")

    protocolos = cargar_protocolos()
    protocolo = st.selectbox("Selecciona Protocolo", list(protocolos.keys()))

    mostrar_ficha_protocolo(protocolo, protocolos)

    st.divider()
    st.subheader("🧪 Simulador de Protocolos")

    viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 30)
    inundacion = st.slider("Nivel de Inundación (cm)", 0, 500, 100)

    mostrar_alerta_protocolo(viento, inundacion)