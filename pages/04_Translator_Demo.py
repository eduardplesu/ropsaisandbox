import streamlit as st
import os
import tempfile
import uuid
from modules.document_translator import upload_file_to_blob, translate_document, reset_translation_containers

def page_translator_demo():
    st.title("Azure Translator Demo - Document Translation")

    # File translation
    st.subheader("Traducere Fișier din Blob Storage")
    uploaded_file = st.file_uploader(
        "Încărcați un fișier pentru traducere (TXT, HTML):",
        type=["txt", "html"]
    )
    target_language = st.selectbox(
        "Selectați limba de destinație",
        ["ro", "en", "de", "fr", "es", "it"],
        index=1
    )

    if uploaded_file is not None:
        # Generate a unique file name to avoid conflicts
        unique_name = f"{uuid.uuid4()}_{uploaded_file.name}"
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        # Upload and Translate
        if st.button("Tradu Fișierul"):
            st.info("Se procesează fișierul...")

            try:
                # Upload file to Blob Storage
                container_name = "source-documents"
                blob_url = upload_file_to_blob(temp_file_path, container_name, unique_name)
                st.success(f"Fișier încărcat cu succes: {blob_url}")

                # Translate file
                with st.spinner("Traducere în curs..."):
                    translated_files = translate_document(target_language)

                st.success("Traducere finalizată!")
                for translated_url in translated_files:
                    st.markdown(f"[Descarcă documentul tradus]({translated_url})", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Eroare: {e}")

    # Reset containers
    st.subheader("Resetare Fișiere Traduse și Surse")
    if st.button("Resetare Traduceri și Surse"):
        try:
            result = reset_translation_containers()
            st.success(result)
        except Exception as e:
            st.error(f"Eroare: {e}")


if __name__ == "__main__":
    page_translator_demo()
