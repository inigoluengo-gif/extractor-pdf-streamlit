import streamlit as st
import fitz  # PyMuPDF

# Título de la aplicación
st.set_page_config(page_title="Extractor de PDFs", layout="wide")
st.title("📄 Extractor de texto desde múltiples archivos PDF")

# Instrucciones
st.markdown("""
Esta aplicación te permite subir varios archivos PDF y extraer el texto contenido en cada uno de ellos.
- Puedes subir múltiples archivos a la vez.
- El texto extraído se mostrará debajo de cada archivo.
""")

# Subida de archivos
uploaded_files = st.file_uploader("Selecciona uno o más archivos PDF", type=["pdf"], accept_multiple_files=True)

# Procesamiento de archivos
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"📘 Texto extraído de: {uploaded_file.name}")
        try:
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            if text.strip():
                st.text_area("Contenido extraído", value=text, height=300)
            else:
                st.warning("No se pudo extraer texto de este archivo.")
        except Exception as e:
            st.error(f"Error al procesar el archivo {uploaded_file.name}: {e}")
else:
    st.info("Sube uno o más archivos PDF para comenzar.")

# Mensaje final
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Streamlit. Listo para desplegar en [Streamlit Cloud](https://streamlit.io/cloud).")
