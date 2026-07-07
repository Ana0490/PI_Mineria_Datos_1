import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="PCA", page_icon="🧭", layout="wide")
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "streaming_users_clean.csv"
sns.set_style("whitegrid")

df = pd.read_csv(DATA_PATH)
variables_pca = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']

st.title("🧭 Escalamiento y PCA")

st.subheader("Variables utilizadas")
st.markdown("""
Se usaron las tres variables numéricas del dataset relevantes para el objetivo: **`age`**,
**`monthly_watch_time_mins`** (variable central del proyecto) y **`customer_support_tickets`**.
Se excluyó `user_id` (identificador sin significado analítico) y `last_login_date` (no es numérica ni central
para el objetivo).
""")

st.subheader("Escalamiento aplicado")
st.markdown("""
Las tres variables están en escalas muy distintas (edad en años, minutos en cientos/miles, tickets en unidades).
Se aplicó **`StandardScaler`** (media 0, desvío 1) para que ninguna domine artificialmente el análisis solo por
tener números más grandes.
""")

X = df[variables_pca]
X_scaled = StandardScaler().fit_transform(X)
pca = PCA()
componentes = pca.fit_transform(X_scaled)
var_exp = pca.explained_variance_ratio_

st.subheader("Varianza explicada")
c1, c2, c3 = st.columns(3)
c1.metric("PC1", f"{var_exp[0]*100:.1f}%")
c2.metric("PC2", f"{var_exp[1]*100:.1f}%")
c3.metric("PC3", f"{var_exp[2]*100:.1f}%")
st.caption("Las tres componentes explican una proporción muy pareja de la varianza (~33% cada una), "
           "porque las tres variables originales están prácticamente sin correlación entre sí.")

st.subheader("Visualización")
df_pca = pd.DataFrame(componentes[:, :2], columns=['PC1', 'PC2'])
df_pca['subscription_plan'] = df['subscription_plan'].values

fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='subscription_plan',
                 hue_order=['Básico', 'Estándar', 'Premium'], alpha=0.4, palette='viridis', ax=ax)
ax.set_title("Usuarios proyectados en PC1 y PC2, por plan")
st.pyplot(fig)

st.subheader("Interpretación")
st.markdown("""
La proyección **no muestra clusters separados por plan de suscripción**. Esto no contradice lo encontrado en
el EDA: el fuerte efecto del plan es específico de `monthly_watch_time_mins`, y no se refleja en `age` ni en
`customer_support_tickets` (que no varían con el plan). En otras palabras, **el plan predice bien el tiempo de
visualización, pero no define un "perfil numérico" distinto de usuario** en el resto de las variables.
""")
