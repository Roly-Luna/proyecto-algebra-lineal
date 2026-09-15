# Programación Lineal

Proyecto de Álgebra Lineal desarrollado con Python y Streamlit.

## Requisitos

- Python con pip.
- Git.

## 1. Instalar uv

En Windows:

```bash
py -m pip install uv
```

En macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Después de instalar, cierra y vuelve a abrir la terminal.

## 2. Descargar el proyecto

```bash
git clone https://github.com/Roly-Luna/proyecto-algebra-lineal
cd linear-algebra-project
```

## 3. Instalar las dependencias

```bash
uv sync
```

## 4. Ejecutar la aplicación

```bash
uv run streamlit run frontend/streamlit_app.py
```

Abre en el navegador la dirección que aparece en la terminal.

Para detener la aplicación, presiona **Ctrl + C**.

> No necesitas ejecutar `uv init`: el proyecto ya está configurado.