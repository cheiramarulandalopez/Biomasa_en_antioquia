
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general de la página
st.set_page_config(page_title="Biomasa en Antioquia", page_icon="🌿", layout="wide")

# Estilos
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("Greens_r")

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("biomasa_antioquia_sample.csv")

data = cargar_datos()

st.title("🌿 Biomasa en Antioquia")
st.markdown("Visualización de datos sobre residuos agrícolas y potencial energético en municipios de Antioquia.")


# Mostrar tabla general
with st.expander("📋 Ver datos originales"):
    st.dataframe(data)

#  GRÁFICO 1: Top municipios con más residuos agrícolas ---
if "municipio" in data.columns and "residuos_agricolas_ton_año" in data.columns:
    st.subheader("🌾 Top 10 municipios con más residuos agrícolas por año")

    top_municipios = data.nlargest(10, "residuos_agricolas_ton_año")

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=top_municipios,
        x="residuos_agricolas_ton_año",
        y="municipio",
        ax=ax1
    )
    ax1.set_xlabel("Toneladas/año")
    ax1.set_ylabel("Municipio")
    ax1.set_title("Top 10 municipios con más residuos agrícolas")
    st.pyplot(fig1)

# GRÁFICO 2: Relación entre población y residuos agrícolas ---
if "poblacion" in data.columns and "residuos_agricolas_ton_año" in data.columns:
    st.subheader("👥 Relación entre población y residuos agrícolas (con líneas)")

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=data,
        x="poblacion",
        y="residuos_agricolas_ton_año",
        s=70,
        color="#2E7D32",
        alpha=0.8,
        ax=ax2
    )
    # 🔹 Agregamos líneas que conectan los puntos
    ax2.plot(
        data["poblacion"],
        data["residuos_agricolas_ton_año"],
        color="#66BB6A",
        linewidth=1.5,
        alpha=0.7
    )
    ax2.set_xlabel("Población")
    ax2.set_ylabel("Residuos agrícolas (ton/año)")
    ax2.set_title("Relación entre población y residuos agrícolas")
    st.pyplot(fig2)

# 6️⃣ Información adicional
st.markdown("---")
st.markdown("📊 *Hecho con ❤️ usando Streamlit, Matplotlib, Pandas y Seaborn.*")
