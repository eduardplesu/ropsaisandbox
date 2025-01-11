import streamlit as st
import asyncio
from modules.document_intelligence_id import analyze_identity_document
from PIL import Image
import json

def serialize_field_value(field_value):
    """
    Serializes field values to make them JSON-compatible.
    """
    if hasattr(field_value, "as_dict"):
        return field_value.as_dict()
    elif isinstance(field_value, (str, int, float, bool, type(None))):
        return field_value
    else:
        return str(field_value)

def page_id_demo():
    st.title("Document Intelligence - ID Demo (Analiză Document Identitate)")
    st.write("DEBUG: Page loaded successfully")

    uploaded_file = st.file_uploader(
        "Încarcă un document de identitate (PDF, JPG, JPEG, PNG)",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.write("DEBUG: File uploaded successfully")
        doc_bytes = uploaded_file.read()

        if uploaded_file.type in ["image/jpeg", "image/png"]:
            st.subheader("Previzualizare Imagine")
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="Identity Document Preview", use_container_width=True)
            except Exception as e:
                st.error(f"Unable to preview image: {e}")

        if st.button("Analizează Documentul de Identitate"):
            st.info("Se procesează documentul... vă rugăm să așteptați.")

            try:
                with st.spinner("Analiză în curs..."):
                    result = asyncio.run(analyze_identity_document(doc_bytes))
                if "error" in result:
                    st.error(f"Eroare la analiza documentului: {result['error']}")
                else:
                    st.success("Analiză finalizată cu succes!")
                    st.write("DEBUG: Analysis successful")

                    documents = result.get("documents", [])
                    for idx, doc_data in enumerate(documents, start=1):
                        st.subheader(f"Document #{idx}")
                        for field_name, field_value in doc_data.items():
                            st.write(f"**{field_name}**: {field_value}")

                    serialized_documents = [
                        {field_name: serialize_field_value(field_value) for field_name, field_value in doc.items()}
                        for doc in documents
                    ]
                    json_result = json.dumps(serialized_documents, indent=2, ensure_ascii=False)

                    st.download_button(
                        label="Descarcă Rezultate (JSON)",
                        data=json_result,
                        file_name="identity_document_results.json",
                        mime="application/json"
                    )
            except Exception as e:
                st.error(f"Eroare: {e}")
                st.write(f"DEBUG: Exception: {e}")

if __name__ == "__main__":
    page_id_demo()
