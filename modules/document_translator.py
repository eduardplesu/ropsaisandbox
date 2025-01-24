import os
import datetime
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DOCUMENT_TRANSLATOR_ENDPOINT = os.getenv("DOCUMENT_TRANSLATOR_ENDPOINT")
TRANSLATOR_KEY = os.getenv("TRANSLATOR_KEY")
BLOB_STORAGE_CONNECTION_STRING = os.getenv("BLOB_STORAGE_CONNECTION_STRING")
AZURE_SOURCE_CONTAINER_URL = os.getenv("AZURE_SOURCE_CONTAINER_URL")
AZURE_TARGET_CONTAINER_URL = os.getenv("AZURE_TARGET_CONTAINER_URL")

# Mapping for supported file types and MIME types
SUPPORTED_FILE_TYPES = {
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".png": "image/png"
}

def upload_file_to_blob(file_path: str, container_name: str, blob_name: str) -> str:
    """
    Upload a file to Azure Blob Storage and return the blob URL with SAS token.
    """
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(container_name)

        # Create container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()

        # Upload the file
        blob_client = container_client.get_blob_client(blob_name)
        with open(file_path, "rb") as file:
            blob_client.upload_blob(file, overwrite=True)

        # Generate SAS token
        sas_token = generate_blob_sas(
            account_name=blob_service_client.account_name,
            container_name=container_name,
            blob_name=blob_name,
            account_key=blob_service_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        )
        blob_url = f"{blob_client.url}?{sas_token}"
        return blob_url

    except Exception as e:
        raise Exception(f"Failed to upload file to Blob Storage: {e}")

def translate_document(target_language: str) -> list:
    """
    Translate documents in a Blob Storage container using Azure Document Translator.
    """
    try:
        # Initialize the translation client
        client = DocumentTranslationClient(
            endpoint=DOCUMENT_TRANSLATOR_ENDPOINT,
            credential=AzureKeyCredential(TRANSLATOR_KEY),
        )

        # Start the translation
        poller = client.begin_translation(
            source_url=AZURE_SOURCE_CONTAINER_URL,
            target_url=AZURE_TARGET_CONTAINER_URL,
            target_language=target_language,
        )
        result = poller.result()

        # Fetch translation results
        translations = []
        for document in result:
            if document.status == "Succeeded":
                translations.append(document.translated_document_url)
            elif document.error:
                raise Exception(f"Document translation error: {document.error.code} - {document.error.message}")

        return translations

    except Exception as e:
        raise Exception(f"Failed to translate document: {e}")

def reset_translation_containers():
    """
    Delete all blobs in the source and target containers to reset the state.
    """
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)

        # Clear the source container
        source_container_client = blob_service_client.get_container_client("source-documents")
        for blob in source_container_client.list_blobs():
            source_container_client.delete_blob(blob.name)

        # Clear the target container
        target_container_client = blob_service_client.get_container_client("translated-documents")
        for blob in target_container_client.list_blobs():
            target_container_client.delete_blob(blob.name)

        return "Source and translated containers have been reset successfully."

    except Exception as e:
        raise Exception(f"Failed to reset containers: {e}")
