import os
from azure.ai.formrecognizer.aio import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FORM_RECOGNIZER_ENDPOINT = os.getenv("FORM_RECOGNIZER_ENDPOINT")
FORM_RECOGNIZER_KEY = os.getenv("FORM_RECOGNIZER_KEY")

async def analyze_document_read(document_bytes: bytes) -> str:
    """
    Analyzes a document using Azure Form Recognizer's 'read' model.
    """
    try:
        client = DocumentAnalysisClient(
            endpoint=FORM_RECOGNIZER_ENDPOINT,
            credential=AzureKeyCredential(FORM_RECOGNIZER_KEY)
        )

        async with client:
            poller = await client.begin_analyze_document(
                model_id="prebuilt-read",
                document=document_bytes
            )
            result = await poller.result()

        # Extract text
        extracted_lines = []
        for page in result.pages:
            for line in page.lines:
                extracted_lines.append(line.content)

        return "\n".join(extracted_lines)
    except Exception as e:
        raise Exception(f"Error in reading document: {e}")
