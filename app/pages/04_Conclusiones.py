import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")

st.title("✅ Conclusiones")

st.subheader("Hallazgos")
st.markdown("""
- El **plan de suscripción** está fuertemente asociado al tiempo de visualización: la mediana de consumo
  casi se **duplica** entre el plan Básico (~553 min/mes) y Premium (~1122 min/mes).
- El **país** aporta una variación mucho más chica (~5% entre el país más alto y el más bajo) y de forma
  pareja en todos los planes.
- No se observa una interacción fuerte entre plan y país: el salto de consumo al subir de plan es de
  magnitud similar en los 7 países analizados.
- El análisis de PCA sobre las variables numéricas (edad, tiempo de visualización, tickets de soporte) no
  encuentra un "perfil" numérico distinto por plan — el efecto del plan es específico del tiempo de
  visualización, no de un patrón general de comportamiento.

**Conclusión general:** el patrón de consumo en la plataforma está **principalmente explicado por el plan
de suscripción**, mientras que el país actúa como un factor secundario y consistente.
""")

st.subheader("Limitaciones")
st.markdown("""
- El dataset no incluye información sobre contenido consumido, dispositivo o franja horaria, que podría
  explicar mejor la variabilidad de consumo dentro de un mismo plan.
- Una parte de `monthly_watch_time_mins` (262 registros) fue imputada durante la limpieza por corresponder
  a datos faltantes o inválidos en el dataset original, lo que puede suavizar levemente la variabilidad
  real dentro de cada grupo.
""")

st.subheader("Próximos pasos")
st.markdown("""
- Incorporar variables adicionales (dispositivo, franja horaria, género consumido con más detalle) para
  explicar mejor la variabilidad dentro de cada plan.
- Analizar la evolución temporal del consumo a partir de `last_login_date`, una vez completada esa
  información.
""")

st.divider()
st.caption("Ver el detalle técnico completo de este análisis en el repositorio de GitHub "
           "(notebooks 01 a 05) y en `reports/informe_final.pdf`.")
