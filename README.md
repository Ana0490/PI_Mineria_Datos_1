# PI_Mineria_Datos_1

## Información general

Proyecto Integrador de la materia Minería de Datos 1. Analiza un dataset de usuarios de una plataforma de
streaming para estudiar patrones de consumo.

- **Integrante:** _Ana Santillan_
- **Comisión:** _Sede Central_
- **Fecha de entrega:** _07/07/2026_
- **Repositorio:** https://github.com/Ana0490/PI_Mineria_Datos_1
- **Aplicación Streamlit:** https://pimineriadatos1-thkworzmafqvz3smjrnrpm.streamlit.app/

## Objetivo del proyecto

Analizar cómo se relaciona el tiempo mensual de visualización con el tipo de plan de suscripción y el país
de los usuarios, para identificar patrones de consumo en la plataforma de streaming. El trabajo cubre
inspección inicial, calidad y limpieza de datos, análisis exploratorio (univariado, bivariado y
multivariado), y reducción de dimensionalidad mediante PCA, con decisiones documentadas y justificadas en
cada etapa. No incluye modelado predictivo ni despliegue de modelos.

## Dataset

El dataset (`data/raw/streaming_users_dirty.json`) contiene 8160 registros de usuarios con las variables:
`user_id`, `age`, `subscription_plan`, `monthly_watch_time_mins`, `country`, `favorite_genre`,
`last_login_date` y `customer_support_tickets`. Corresponde a un recorte provisto por la cátedra, con
problemas de calidad intencionales (duplicados, inconsistencias de texto, valores inválidos y formatos de
fecha mixtos) para trabajar el proceso de limpieza. El detalle completo de la inspección inicial está en
`notebooks/01_inspeccion_inicial.ipynb`, y el dataset ya procesado en `data/processed/streaming_users_clean.csv`.

## Estructura del repositorio

```
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                  # dataset original, sin modificar
│   └── processed/            # dataset limpio, resultado del pipeline ETL
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/                      # aplicación Streamlit
│   ├── Home.py
│   └── pages/
├── reports/
│   └── informe_final.pdf
└── logs/
    └── pipeline_log.csv      # registro de transformaciones ETL
```

## Preparación y calidad de datos

La inspección inicial (`01_inspeccion_inicial.ipynb`) detectó duplicados, variantes de texto en las
variables categóricas, valores numéricos imposibles (edad, tiempo de visualización, tickets de soporte) y
formatos de fecha mixtos. Cada decisión de limpieza (`02_calidad_y_limpieza.ipynb`) se tomó a partir de esa
evidencia: se documentó qué se observó, qué acción se aplicó y qué impacto tuvo en el dataset. Se priorizó
no perder información en las variables centrales del objetivo (`monthly_watch_time_mins`,
`subscription_plan`, `country`): por ejemplo, los valores inválidos de tiempo de visualización se
imputaron con la mediana según plan y país, en vez de eliminar filas o usar un promedio global. Todas las
transformaciones quedaron registradas fila por fila en `logs/pipeline_log.csv`, permitiendo comparar el
estado inicial (8160 filas) y final (8000 filas) del dataset.

## Resumen del análisis exploratorio

El análisis exploratorio (`03_eda.ipynb`) se desarrolló en tres niveles —univariado, bivariado y
multivariado— con interpretaciones vinculadas al objetivo del proyecto. Se estudió la distribución del
tiempo de visualización y de los usuarios por plan; luego su relación con plan de suscripción y con país
por separado; y finalmente su relación conjunta mediante una tabla cruzada. El detalle completo de cada
visualización, con su interpretación, está en la notebook y se resume de forma visual e interactiva en la
aplicación Streamlit (sección EDA), evitando duplicar aquí los mismos gráficos y números.

## Reducción de dimensionalidad

En `04_pca.ipynb` se aplicó escalamiento (`StandardScaler`) y PCA sobre las variables numéricas `age`,
`monthly_watch_time_mins` y `customer_support_tickets`, documentando variables utilizadas, varianza
explicada por componente y la interpretación de los resultados en relación con los hallazgos del EDA. El
detalle numérico y las visualizaciones están en la notebook y en la sección PCA de la aplicación
Streamlit.

## Visualización interactiva

La aplicación pública en Streamlit Cloud comunica los resultados para público general, en 4 secciones:
Dataset, EDA (5 visualizaciones con interpretación), PCA y Conclusiones. No reemplaza la evidencia técnica
del repositorio. Enlace: https://pimineriadatos1-thkworzmafqvz3smjrnrpm.streamlit.app/

## Cómo ejecutar localmente

```bash
git clone <URL-del-repositorio>
cd PI_Mineria_Datos_1
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# Notebooks
jupyter notebook notebooks/

# Aplicación Streamlit
streamlit run app/Home.py
```

## Conclusiones

El plan de suscripción está fuertemente asociado al tiempo de visualización: la mediana de consumo casi se
duplica entre Básico y Premium. El país aporta una variación mucho menor y consistente entre planes, sin
una interacción fuerte con el plan. El detalle completo de hallazgos, limitaciones y próximos pasos está
desarrollado en `notebooks/05_conclusiones.ipynb`, en `reports/informe_final.pdf` y en la sección
Conclusiones de la aplicación Streamlit.
