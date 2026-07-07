import streamlit as st
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="🔎", layout="wide")
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "streaming_users_clean.csv"
sns.set_style("whitegrid")

df = pd.read_csv(DATA_PATH)
orden_plan = ['Básico', 'Estándar', 'Premium']

st.title("🔎 Análisis exploratorio de datos")
st.markdown("Cinco visualizaciones (2 univariadas, 2 bivariadas, 1 multivariada) que responden a la pregunta: "
            "**¿cómo se relaciona el tiempo de visualización con el plan y el país?**")

st.divider()
st.header("Análisis univariado")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribución del tiempo de visualización")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['monthly_watch_time_mins'], bins=40, kde=True, ax=ax, color="#4C72B0")
    ax.set_xlabel("Minutos de visualización mensual")
    st.pyplot(fig)
    st.caption("**Interpretación:** la distribución es unimodal con cola hacia la derecha — no hay un "
               "'usuario típico' único de consumo, lo que motiva buscar qué variables explican esa dispersión.")

with col2:
    st.subheader("Usuarios por plan de suscripción")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='subscription_plan', order=orden_plan, ax=ax, hue='subscription_plan',
                  hue_order=orden_plan, palette='viridis', legend=False)
    ax.set_xlabel("Plan")
    st.pyplot(fig)
    st.caption("**Interpretación:** el plan Básico concentra a la mayoría de los usuarios; hay que tener esto "
               "en cuenta al comparar promedios, ya que Premium representa un grupo más chico.")

st.divider()
st.header("Análisis bivariado")

col3, col4 = st.columns(2)
with col3:
    st.subheader("Tiempo de visualización según plan")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x='subscription_plan', y='monthly_watch_time_mins', order=orden_plan,
                hue='subscription_plan', hue_order=orden_plan, palette='viridis', legend=False, ax=ax)
    ax.set_xlabel("Plan")
    ax.set_ylabel("Minutos / mes")
    st.pyplot(fig)
    med_plan = df.groupby('subscription_plan')['monthly_watch_time_mins'].median().reindex(orden_plan)
    st.caption(f"**Interpretación:** diferencia fuerte y clara — la mediana pasa de {med_plan['Básico']:.0f} "
               f"min (Básico) a {med_plan['Premium']:.0f} min (Premium), casi el doble. El plan es un fuerte "
               f"predictor del consumo.")

with col4:
    st.subheader("Tiempo de visualización según país")
    orden_pais = df.groupby('country')['monthly_watch_time_mins'].median().sort_values(ascending=False).index
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x='country', y='monthly_watch_time_mins', order=orden_pais,
                hue='country', hue_order=list(orden_pais), palette='crest', legend=False, ax=ax)
    ax.set_xlabel("País")
    ax.set_ylabel("Minutos / mes")
    plt.setp(ax.get_xticklabels(), rotation=30)
    st.pyplot(fig)
    med_pais = df.groupby('country')['monthly_watch_time_mins'].median()
    st.caption(f"**Interpretación:** diferencia mucho más chica — apenas entre {med_pais.min():.0f} y "
               f"{med_pais.max():.0f} min de mediana entre países (~5%). El país aporta poca variabilidad "
               f"por sí solo, comparado con el plan.")

st.divider()
st.header("Análisis multivariado")
st.subheader("Mediana de tiempo de visualización: país × plan")

tabla_pivot = df.pivot_table(values='monthly_watch_time_mins', index='country',
                              columns='subscription_plan', aggfunc='median').reindex(columns=orden_plan)
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(tabla_pivot, annot=True, fmt='.0f', cmap='YlGnBu', ax=ax, cbar_kws={'label': 'Mediana min/mes'})
st.pyplot(fig)
st.caption("**Interpretación:** el salto de consumo al subir de plan (entre 540 y 610 minutos) se repite de "
           "forma consistente en los 7 países — el efecto del plan no depende demasiado del país. No hay una "
           "interacción fuerte: el plan de suscripción es el factor dominante, y el país solo modula "
           "levemente ese efecto.")
