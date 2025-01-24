import streamlit as st
import asyncio
from modules.document_intelligence_read import analyze_document_read

def page_read_demo():
    st.title("Document Intelligence - Read Demo (Extragere Text)")

    # File uploader
    uploaded_file = st.file_uploader(
        "Încărcați un fișier (PDF, JPG, PNG):",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.info("Fișier încărcat cu succes.")
        doc_bytes = uploaded_file.read()

        # Display a preview for image files
        if uploaded_file.type in ["image/jpeg", "image/png"]:
            st.subheader("Previzualizare Imagine")
            try:
                from PIL import Image
                image = Image.open(uploaded_file)
                st.image(image, caption="Previzualizare Document", use_container_width=True)
            except Exception as e:
                st.error(f"Eroare la previzualizarea imaginii: {e}")

        if st.button("Extrage Text"):
            st.info("Se procesează fișierul... vă rugăm să așteptați.")
            try:
                with st.spinner("Analiză în curs..."):
                    extracted_text = asyncio.run(analyze_document_read(doc_bytes))

                if extracted_text:
                    st.success("Analiză finalizată cu succes!")
                    st.text_area("Text Extras", value=extracted_text, height=300)

                    # Allow downloading of extracted text
                    st.download_button(
                        label="Descarcă Textul Extras",
                        data=extracted_text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Nu s-a putut extrage text din document.")
            except Exception as e:
                st.error(f"Eroare: {e}")

if __name__ == "__main__":
    page_read_demo()
