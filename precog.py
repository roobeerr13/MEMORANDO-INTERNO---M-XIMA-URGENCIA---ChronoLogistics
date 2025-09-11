def predecir_riesgo(velocidad_media, intensidad_lluvia):
    riesgo = min(100, velocidad_media * 0.5 + intensidad_lluvia * 0.8)
    if riesgo > 80:
        nivel = "ALTO"
    elif riesgo > 50:
        nivel = "MODERADO"
    else:
        nivel = "BAJO"
    return f"{riesgo:.1f}% - {nivel}"