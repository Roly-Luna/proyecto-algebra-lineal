# importa streamlit para crear la interfaz
import streamlit as st

# configura el titulo de la pagina y el ancho
st.set_page_config(page_title="programacion lineal", layout="wide")

# crea las restricciones iniciales y las conserva durante la sesion
if "constraints" not in st.session_state:
    st.session_state.constraints = [
        {"a": 1.0, "b": 0.0, "operator": "<=", "c": 4.0, "label": "recurso a"},
        {"a": 0.0, "b": 2.0, "operator": "<=", "c": 12.0, "label": "recurso b"},
        {"a": 3.0, "b": 2.0, "operator": "<=", "c": 18.0, "label": "recurso c"},
    ]

# muestra el titulo y las instrucciones
st.title("programacion lineal, metodo grafico")
st.caption("ingresa la funcion objetivo y las restricciones del problema")

# permite configurar los nombres y registrar la no negatividad
with st.sidebar:
    st.subheader("configuracion")
    var1_name = st.text_input("nombre variable x1", value="x1")
    var2_name = st.text_input("nombre variable x2", value="x2")
    obj_label = st.text_input("nombre de la funcion objetivo", value="z")
    non_negative = st.checkbox(
        "variables no negativas, x1 y x2 mayores o iguales a cero",
        value=True,
    )

# organiza la funcion objetivo en tres columnas
st.subheader("1. funcion objetivo")
col1, col2, col3 = st.columns(3)

# recibe el coeficiente de la primera variable
with col1:
    obj_a = st.number_input(f"coeficiente de {var1_name}", value=3.0)

# recibe el coeficiente de la segunda variable
with col2:
    obj_b = st.number_input(f"coeficiente de {var2_name}", value=5.0)

# permite elegir maximizar o minimizar
with col3:
    mode = st.selectbox(
        "modo",
        ["max", "min"],
        format_func=lambda m: "maximizar" if m == "max" else "minimizar",
    )

# muestra la funcion objetivo con formato matematico
st.latex(
    rf"{obj_label} = {obj_a:g}\,{var1_name}"
    rf" + {obj_b:g}\,{var2_name} \quad ({mode})"
)

# prepara la seccion de restricciones
st.subheader("2. restricciones")
to_delete = None

# recorre las restricciones y crea sus campos
for i, con in enumerate(st.session_state.constraints):
    c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 2, 0.5])

    # recibe los coeficientes de las dos variables
    con["a"] = c1.number_input(
        f"coeficiente de {var1_name}", value=con["a"], key=f"a_{i}"
    )
    con["b"] = c2.number_input(
        f"coeficiente de {var2_name}", value=con["b"], key=f"b_{i}"
    )

    # permite elegir el signo de la restriccion
    con["operator"] = c3.selectbox(
        "operador",
        ["<=", ">=", "="],
        index=["<=", ">=", "="].index(con["operator"]),
        key=f"op_{i}",
    )

    # recibe el limite y la descripcion de la restriccion
    con["c"] = c4.number_input(
        "lado derecho", value=con["c"], key=f"c_{i}"
    )
    con["label"] = c5.text_input(
        "descripcion", value=con["label"], key=f"label_{i}"
    )

    # identifica la fila que se desea eliminar
    if c6.button("✕", key=f"del_{i}"):
        to_delete = i

# elimina la restriccion seleccionada
if to_delete is not None:
    st.session_state.constraints.pop(to_delete)

    # limpia los campos para evitar mezclar los datos de las filas
    for i in range(len(st.session_state.constraints) + 1):
        for field in ("a", "b", "op", "c", "label"):
            st.session_state.pop(f"{field}_{i}", None)

    # actualiza la interfaz despues de eliminar
    st.rerun()

# agrega una nueva restriccion
if st.button("+ agregar restriccion"):
    st.session_state.constraints.append(
        {
            "a": 1.0,
            "b": 1.0,
            "operator": "<=",
            "c": 10.0,
            "label": "nueva restriccion",
        }
    )

    # actualiza la interfaz para mostrar la nueva fila
    st.rerun()