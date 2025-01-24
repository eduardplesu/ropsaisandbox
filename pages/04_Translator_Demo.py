import streamlit as st
import os
import tempfile
import uuid
from modules.document_translator import upload_file_to_blob, translate_document, reset_translation_containers, SUPPORTED_FILE_TYPES

def page_translator_demo():
    st.title("Azure Translator Demo - Document Translation")

    # File translation
    st.subheader("Upload a File for Translation")
    uploaded_file = st.file_uploader(
        "Upload a document (DOCX, PDF, JPEG, PNG, TXT):",
        type=list(SUPPORTED_FILE_TYPES.keys())
    )
    target_language = st.selectbox(
        "Select target language:",
        ["ro", "en", "de", "fr", "es", "it"],
        index=1
    )

    if uploaded_file is not None:
        # Validate file type
        file_extension = os.path.splitext(uploaded_file.name.lower())[1]
        if file_extension not in SUPPORTED_FILE_TYPES:
            st.error("Unsupported file type!")
            return

        # Generate a unique file name to avoid conflicts
        unique_name = f"{uuid.uuid4()}_{uploaded_file.name}"
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        # Upload and Translate
        if st.button("Translate File"):
            st.info("Processing the file...")

            try:
                # Upload file to Blob Storage
                container_name = "source-documents"
                blob_url = upload_file_to_blob(temp_file_path, container_name, unique_name)
                st.success(f"File successfully uploaded: {blob_url}")

                # Translate file
                with st.spinner("Translating..."):
                    translated_files = translate_document(target_language)

                st.success("Translation completed!")
                for translated_url in translated_files:
                    st.markdown(f"[Download Translated Document]({translated_url})", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")

    # Reset containers
    st.subheader("Reset Translations")
    if st.button("Reset Files"):
        try:
            result = reset_translation_containers()
            st.success(result)
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    page_translator_demo()
