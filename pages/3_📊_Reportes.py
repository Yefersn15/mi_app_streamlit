import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reportes", page_icon="📊")

st.title("📊 Dashboards y Reportes")

ventas_totales = 125000
clientes_activos = 3200
productos_vendidos = 540

col1, col2, col3 = st.columns(3)
col1.metric("Ventas totales", f"${ventas_totales:,}")
col2.metric("Clientes activos", f"{clientes_activos}")
col3.metric("Productos vendidos", f"{productos_vendidos}")

fechas = pd.date_range(start="2024-01-01", periods=12, freq="MS")
ventas = [8500, 9200, 10400, 11500, 13200, 13900, 12800, 14500, 15200, 16000, 17200, 18000]
reporte = pd.DataFrame({"Fecha": fechas, "Ventas": ventas})

st.subheader("Ventas mensuales")

rango_fechas = st.date_input(
    "Selecciona un rango de fechas",
    value=(fechas.min().date(), fechas.max().date()),
    min_value=fechas.min().date(),
    max_value=fechas.max().date(),
)

if isinstance(rango_fechas, tuple) and len(rango_fechas) == 2:
    inicio, fin = rango_fechas
    reporte_filtrado = reporte[(reporte["Fecha"].dt.date >= inicio) & (reporte["Fecha"].dt.date <= fin)]
else:
    reporte_filtrado = reporte

st.line_chart(reporte_filtrado.set_index("Fecha")["Ventas"])

csv_data = reporte_filtrado.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Descargar reporte",
    data=csv_data,
    file_name="reporte_ventas.csv",
    mime="text/csv",
)
