# MEMORANDO-INTERNO---M-XIMA-URGENCIA---ChronoLogistics
https://github.com/roobeerr13/MEMORANDO-INTERNO---M-XIMA-URGENCIA---ChronoLogistics.git
# 🧭 ChronoLogistics Crisis Dashboard

**Sistema de Mando y Control en Tiempo Real para Respuesta Estratégica ante Crisis Climáticas**

Este proyecto es una aplicación web interactiva desarrollada para ChronoLogistics como parte de su plan de contingencia. El objetivo es proporcionar una herramienta operativa en vivo que centralice la monitorización de riesgos, la simulación de escenarios y la activación de protocolos de emergencia.

---

## 🚀 Descripción General

El dashboard está dividido en tres pestañas principales:

1. **Precog: Monitor de Riesgo Táctico**
   - Visualización del mapa de calor con los clústeres críticos.
   - Simulador interactivo que calcula el nivel de riesgo en cascada en tiempo real.

2. **Chronos: Visión Estratégica 2040**
   - Selector de estrategia futura: *Fortaleza Verde* o *Búnker Tecnológico*.
   - Visualización de imágenes generadas por GAN y defensa argumentativa de cada visión.

3. **K-Lang: Manual de Batalla Interactivo**
   - Selector de protocolos operativos: *VÍSPERA*, *CÓDIGO ROJO*, *RENACIMIENTO*.
   - Simulador de condiciones que activa automáticamente el protocolo correspondiente.

---

## 🧠 Lógica de Predicción

La función `predecir_riesgo()` calcula el nivel de riesgo en cascada según dos variables:

- **Velocidad Media del Viento**
- **Intensidad de Lluvia**

El resultado se clasifica en tres niveles: `BAJO`, `MODERADO`, `ALTO`.

---

## 📜 Protocolos de Emergencia

Los protocolos están definidos en `protocols.json` y se activan según condiciones simuladas:

- **VÍSPERA**: Viento < 50 km/h
- **CÓDIGO ROJO**: Viento > 90 km/h
- **RENACIMIENTO**: Inundación > 300 cm

Cada protocolo incluye un disparador y una lista de acciones operativas.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend & Backend**: [Streamlit](https://streamlit.io/)
- **Lenguaje**: Python 3.9+
- **Visualización**: Imágenes pre-generadas, sliders interactivos, métricas dinámicas

---

## 📦 Instalación

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/chrono-dashboard.git
cd chrono-dashboard

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
streamlit run dashboard/app.py




