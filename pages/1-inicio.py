import streamlit as st

st.set_page_config(page_title="Mi App", layout="wide")

# ================= BARRA LATERAL =================
st.sidebar.title("🧭 Menú de Navegación")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ("Inicio", "Análisis de Datos","Configuración", "Ayuda")
)

st.divider()

# ================= PÁGINA: INICIO =================
if opcion == "Inicio":
    st.title("🏠 Página de Inicio")
    st.write("¡Bienvenido a la aplicación! Selecciona una opción del menú.")

# ================= PÁGINA: ANÁLISIS DE DATOS =================
elif opcion == "Análisis de Datos":
    st.title("📊 Análisis de Datos")
    
    tab1, tab2, tab3 = st.tabs(["🐱 Cat", "🐶 Dog", "🦉 Owl"])
    
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")



# ================= PÁGINA: CONFIGURACIÓN =================
elif opcion == "Configuración":
    st.title("⚙️ Configuración")
    
    with st.expander("📂 Sección 1"):
        option1 = st.checkbox("Opción 1.1")
        option2 = st.checkbox("Opción 1.2")
    
    with st.expander("📂 Sección 2"):
        option3 = st.radio("Selecciona", ["A", "B", "C"])

# ================= PÁGINA: AYUDA =================
elif opcion == "Ayuda":
    st.title("❓ Ayuda")
    st.write("Documentación y soporte de la aplicación.")