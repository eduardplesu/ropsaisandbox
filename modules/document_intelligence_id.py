import os
from azure.ai.formrecognizer.aio import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FORM_RECOGNIZER_ENDPOINT = os.getenv("FORM_RECOGNIZER_ENDPOINT")
FORM_RECOGNIZER_KEY = os.getenv("FORM_RECOGNIZER_KEY")

async def analyze_identity_document(document_bytes: bytes):
    """
    Analyzes an identity document using Azure Form Recognizer's prebuilt ID model.
    """
    try:
        # Initialize the Document Analysis Client
        document_analysis_client = DocumentAnalysisClient(
            endpoint=FORM_RECOGNIZER_ENDPOINT,
            credential=AzureKeyCredential(FORM_RECOGNIZER_KEY)
        )

        # Start the analysis operation
        async with document_analysis_client:  # Ensures the session is closed after use
            poller = await document_analysis_client.begin_analyze_document(
                model_id="prebuilt-idDocument",
                document=document_bytes
            )
            result = await poller.result()

        # Process the results
        extracted_data = []
        for document in result.documents:
            fields = {}
            for field_name, field in document.fields.items():
                if field.value:  # Include only non-empty fields
                    fields[field_name.replace("_", " ").title()] = field.value
            extracted_data.append(fields)

        return {"documents": extracted_data}

    except Exception as e:
        return {"error": str(e)}
