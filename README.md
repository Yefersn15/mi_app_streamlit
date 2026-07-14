# mi_app_streamlit

Esta es una aplicación desarrollada con Streamlit para explorar componentes básicos de interfaz, widgets interactivos, visualizaciones de datos y descarga de archivos desde una app web.

## ¿Qué hace la app?

La aplicación muestra:

- texto y contenido en Markdown.
- controles como sliders, select boxes y campos de texto.
- tablas y gráficos con pandas, matplotlib y seaborn.
- métricas y secciones desplegables.
- un botón para descargar un archivo CSV.

## Requisitos

Antes de ejecutar la app necesitas tener instalado:

- Python 3.9 o superior
- pip

## Instalación y ejecución en Windows PowerShell

Sigue estos pasos en orden exacto desde la carpeta del repositorio clonado:

1. Entrar a la carpeta del proyecto:

```powershell
cd .\mi_app_streamlit
```

2. Crear un entorno virtual:

```powershell
python -m venv .venv
```

3. Activar el entorno virtual:

Si PowerShell bloquea la ejecución del script, ejecuta esto una vez antes de activar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Actualizar pip e instalar dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install streamlit pandas matplotlib seaborn numpy
```

5. Ejecutar la aplicación:

```powershell
python -m streamlit run app.py
```

6. Abrir la app en el navegador:

```text
http://localhost:8501
```

> Si el comando `streamlit run app.py` no funciona en tu terminal, usa siempre `python -m streamlit run app.py`, que es la forma más fiable en Windows PowerShell.

## Estructura del proyecto

- app.py: archivo principal de la aplicación Streamlit.
- pages/: carpeta para futuras páginas adicionales.
- requirements.txt: dependencias necesarias para ejecutar la app.

## ¿Qué aprendí?

Al desarrollar esta app aprendí a:

- crear aplicaciones web rápidas con Streamlit.
- trabajar con widgets interactivos y formularios.
- mostrar tablas y gráficos en una interfaz simple.
- usar pandas y matplotlib para trabajar con datos.
- estructurar una app básica de forma ordenada y fácil de ejecutar.