import streamlit as st
import fitz  # PyMuPDF
import pandas as pd

st.set_page_config(page_title="Extractor de PDFs", layout="wide")
st.title("📄 Extractor de texto desde múltiples archivos PDF")

st.markdown("""
Esta aplicación te permite subir varios archivos PDF y extraer el texto contenido en cada uno de ellos.
- Puedes subir múltiples archivos a la vez.
- El texto extraído se mostrará debajo de cada archivo.
- Al final puedes descargar un archivo CSV con todos los textos extraídos.
""")

uploaded_files = st.file_uploader("Selecciona uno o más archivos PDF", type=["pdf"], accept_multiple_files=True)

extracted_data = []

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
                extracted_data.append({"Archivo": uploaded_file.name, "Texto extraído": text})
            else:
                st.warning("No se pudo extraer texto de este archivo.")
        except Exception as e:
            st.error(f"Error al procesar el archivo {uploaded_file.name}: {e}")

    if extracted_data:
        df = pd.DataFrame(extracted_data)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar CSV con textos extraídos",
            data=csv,
            file_name="textos_extraidos.csv",
            mime="text/csv"
        )
else:
    st.info("Sube uno o más archivos PDF para comenzar.")

st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Streamlit. Listo para desplegar en [Streamlit Cloud](https://streamlit.io/cloud).")
