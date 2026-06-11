import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Productos", page_icon="📦")

st.title("📦 Catálogo de Productos")

st.image(
    "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=1200&q=80",
    caption="Productos disponibles",
    width=800,
)

productos = pd.DataFrame([
    {"Nombre": "Altavoz inalámbrico", "Categoría": "Electrónica", "Precio": 249000, "Stock": 32},
    {"Nombre": "Cámara instantánea", "Categoría": "Electrónica", "Precio": 179000, "Stock": 18},
    {"Nombre": "Mochila urbana", "Categoría": "Accesorios", "Precio": 95000, "Stock": 45},
    {"Nombre": "Botella térmica", "Categoría": "Hogar", "Precio": 42000, "Stock": 60},
    {"Nombre": "Auriculares deportivos", "Categoría": "Electrónica", "Precio": 129000, "Stock": 27},
])

categorias = productos["Categoría"].unique().tolist()
seleccionadas = st.multiselect(
    "Filtrar por categoría",
    options=categorias,
    default=categorias,
)

filtro = productos[productos["Categoría"].isin(seleccionadas)]

st.dataframe(filtro, use_container_width=True)

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(filtro["Nombre"], filtro["Precio"], color="#185FA5")
ax.set_xlabel("Producto")
ax.set_ylabel("Precio (COP)")
ax.set_title("Precio por producto")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.metric(label="Total de productos", value=len(productos))
