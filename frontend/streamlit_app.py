# importa streamlit para crear la interfaz
import streamlit as st

# configura el titulo de la pagina y el ancho
st.set_page_config(page_title="Programación Lineal", layout="wide")

# crea y conserva las restricciones iniciales
if "constraints" not in st.session_state:
    st.session_state.constraints = [
        {"a": 1.0, "b": 0.0, "operator": "<=", "c": 4.0, "label": "Recurso A"},
        {"a": 0.0, "b": 2.0, "operator": "<=", "c": 12.0, "label": "Recurso B"},
        {"a": 3.0, "b": 2.0, "operator": "<=", "c": 18.0, "label": "Recurso C"},
    ]

# muestra el titulo y las instrucciones
st.title("Programación Lineal — Método Gráfico")
st.caption("Ingresa la función objetivo y las restricciones del problema.")

# permite configurar los nombres y registrar la no negatividad
with st.sidebar:
    st.subheader("Configuración")
    var1_name = st.text_input("Nombre variable x1", value="x1")
    var2_name = st.text_input("Nombre variable x2", value="x2")
    obj_label = st.text_input("Nombre de la función objetivo", value="Z")
    non_negative = st.checkbox("Variables no negativas (x1, x2 ≥ 0)", value=True)

# organiza los campos de la funcion objetivo
st.subheader("1. Función objetivo")
col1, col2, col3 = st.columns(3)

# recibe el coeficiente de la primera variable
with col1:
    obj_a = st.number_input(f"Coeficiente de {var1_name}", value=3.0)

# recibe el coeficiente de la segunda variable
with col2:
    obj_b = st.number_input(f"Coeficiente de {var2_name}", value=5.0)

# permite elegir maximizar o minimizar
with col3:
    mode = st.selectbox(
        "Modo", ["max", "min"],
        format_func=lambda m: "Maximizar" if m == "max" else "Minimizar"
    )

# muestra la funcion objetivo con formato matematico
st.latex(rf"{obj_label} = {obj_a:g}{var1_name} + {obj_b:g}{var2_name} \quad ({mode})")

# prepara la seccion de restricciones
st.subheader("2. Restricciones")
to_delete = None

# recorre las restricciones y crea sus campos
for i, con in enumerate(st.session_state.constraints):
    c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 2, 0.5])

    # recibe los coeficientes de las variables
    con["a"] = c1.number_input(f"Coef. {var1_name}", value=con["a"], key=f"a_{i}")
    con["b"] = c2.number_input(f"Coef. {var2_name}", value=con["b"], key=f"b_{i}")

    # permite elegir el signo de la restriccion
    con["operator"] = c3.selectbox(
        "Op.", ["<=", ">=", "="],
        index=["<=", ">=", "="].index(con["operator"]), key=f"op_{i}"
    )

    # recibe el limite y la descripcion
    con["c"] = c4.number_input("Lado derecho", value=con["c"], key=f"c_{i}")
    con["label"] = c5.text_input("Descripción", value=con["label"], key=f"label_{i}")

    # identifica la fila que se desea eliminar
    if c6.button("✕", key=f"del_{i}"):
        to_delete = i

# elimina la restriccion seleccionada
if to_delete is not None:
    st.session_state.constraints.pop(to_delete)

    # limpia los campos para evitar mezclar las filas
    for i in range(len(st.session_state.constraints) + 1):
        for field in ("a", "b", "op", "c", "label"):
            st.session_state.pop(f"{field}_{i}", None)

    # actualiza la interfaz
    st.rerun()

# agrega una nueva restriccion
if st.button("+ Agregar restricción"):
    st.session_state.constraints.append(
        {"a": 1.0, "b": 1.0, "operator": "<=", "c": 10.0, "label": "Nueva restricción"}
    )

    # actualiza la interfaz
    st.rerun()