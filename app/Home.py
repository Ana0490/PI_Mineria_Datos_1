import streamlit as st
from pathlib import Path
import pandas as pd


st.set_page_config(page_title="Streaming - Proyecto Integrador", page_icon="🎬", layout="wide")

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "streaming_users_clean.csv"

st.title("🎬 Patrones de consumo en una plataforma de streaming")

st.markdown("""
### Proyecto Integrador — Minería de Datos 1

**Integrante:** _Ana Santillan_
**Fecha:** _07/07/2026_

---

### Contexto

Este proyecto analiza cómo se relaciona el **tiempo mensual de visualización** de los usuarios de una
plataforma de streaming con su **plan de suscripción** (Básico / Estándar / Premium) y su **país**,
con el objetivo de identificar patrones de consumo.

La aplicación resume, para público general, los resultados del análisis técnico desarrollado en las
notebooks del repositorio. No reemplaza la evidencia técnica — para el detalle completo de las decisiones
de limpieza, el análisis exploratorio y el PCA, ver el repositorio de GitHub.

**Repositorio del proyecto:** _(https://github.com/Ana0490/PI_Mineria_Datos_1)_
""")

st.divider()

if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)
    c1, c2, c3 = st.columns(3)
    c1.metric("Usuarios analizados", f"{len(df):,}")
    c2.metric("Países", df['country'].nunique())
    c3.metric("Planes de suscripción", df['subscription_plan'].nunique())
else:
    st.warning("No se encontró el dataset procesado en data/processed/.")

st.caption("Navegá por las secciones en el menú lateral: Dataset, EDA, PCA y Conclusiones.")
