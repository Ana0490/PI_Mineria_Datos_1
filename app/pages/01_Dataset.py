import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📊", layout="wide")
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "streaming_users_clean.csv"

st.title("📊 El dataset")

st.markdown("""
El dataset original contiene registros de usuarios de una plataforma de streaming, con información sobre
edad, plan de suscripción, tiempo de visualización mensual, país, género favorito, fecha de último login
y tickets de soporte al cliente.
""")

df = pd.read_csv(DATA_PATH)

st.subheader("Resumen de calidad")
st.markdown("""
El dataset original llegó con varios problemas de calidad: duplicados, formatos de texto inconsistentes
en las variables categóricas (mayúsculas, tildes, abreviaturas), valores imposibles (edades negativas,
tiempos de visualización negativos o con un valor centinela) y fechas en múltiples formatos.
Estos problemas se documentaron y resolvieron con decisiones justificadas — el detalle completo
(evidencia, decisión e impacto de cada paso) está en `notebooks/02_calidad_y_limpieza.ipynb`
y en `logs/pipeline_log.csv`.
""")

c1, c2, c3 = st.columns(3)
c1.metric("Filas en dataset procesado", f"{len(df):,}")
c2.metric("Columnas", df.shape[1])
c3.metric("Valores nulos restantes", int(df.isna().sum().sum()))

st.subheader("Vista previa")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("Transformaciones principales aplicadas")
st.markdown("""
- Eliminación de filas y de `user_id` duplicados.
- Normalización de texto en `subscription_plan`, `country` y `favorite_genre` (unificación de mayúsculas,
  tildes, abreviaturas y códigos de país).
- Corrección de valores imposibles en `age` (fuera de 13-100 años) y en `monthly_watch_time_mins`
  (negativos y un valor centinela en 99999), con imputación por mediana usando grupos relevantes.
- Acotamiento de `customer_support_tickets` a un rango plausible.
- Unificación de formato de fecha en `last_login_date`.

Log completo, paso a paso, en `logs/pipeline_log.csv`.
""")
