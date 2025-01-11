#ropsaisandbox

ropsaisandbox is a Streamlit-based AI application designed to leverage various Azure Cognitive Services, including speech-to-text, document translation, and form recognition. This project includes local development, Docker deployment, and Azure Web App hosting.

Features
Speech-to-Text: Convert audio files to text using Azure Speech Service.
Document Translation: Translate documents stored in Azure Blob Storage with Azure Document Translator.
Form Recognition: Extract structured data from forms with Azure Form Recognizer.
Text Analysis: Leverage Azure Text Analytics for language detection and text insights.
Prerequisites
Azure Cognitive Services:

Azure Form Recognizer
Azure Speech Service
Azure Translator
Azure Text Analytics
Azure Blob Storage:

Two containers: source-documents and translated-documents.
Python 3.12+

Docker (if deploying with containers).

Installation
1. Clone the Repository
git clone https://github.com/your-username/ropsaisandbox.git
cd ropsaisandbox
2. Set Up Environment Variables
Create a .env file in the project root with the following variables:

# Azure Cognitive Services
FORM_RECOGNIZER_ENDPOINT=<Your Azure Form Recognizer Endpoint>
FORM_RECOGNIZER_KEY=<Your Azure Form Recognizer Key>
SPEECH_ENDPOINT=<Your Azure Speech Endpoint>
SPEECH_KEY=<Your Azure Speech Key>
TRANSLATOR_ENDPOINT=<Your Azure Translator Endpoint>
DOCUMENT_TRANSLATOR_ENDPOINT=<Your Azure Document Translator Endpoint>
TRANSLATOR_KEY=<Your Azure Translator Key>
TEXT_ANALYTICS_ENDPOINT=<Your Azure Text Analytics Endpoint>
TEXT_ANALYTICS_KEY=<Your Azure Text Analytics Key>
TRANSLATOR_REGION=<Your Azure Region>

# Azure Storage
BLOB_STORAGE_CONNECTION_STRING=<Your Azure Blob Storage Connection String>
AZURE_SOURCE_CONTAINER_URL=<Your Source Container SAS URL>
AZURE_TARGET_CONTAINER_URL=<Your Target Container SAS URL>
3. Install Dependencies
pip install -r requirements.txt
Local Development
1. Run the App Locally
streamlit run app.py
Access the application at http://localhost:8501.

Docker Deployment
1. Build the Docker Image
docker build -t ropsaisandbox .
2. Run Locally in Docker
docker run -p 8501:8501 ropsaisandbox
Access the app at http://localhost:8501.

Azure Deployment
1. Publish Docker Image to Azure Container Registry (ACR)
Log in to Azure and ACR
az login
az acr login --name <Your-ACR-Name>
Tag and Push the Docker Image
docker tag ropsaisandbox <Your-ACR-Name>.azurecr.io/ropsaisandbox:latest
docker push <Your-ACR-Name>.azurecr.io/ropsaisandbox:latest
2. Deploy to Azure Web App
Create the Web App
az webapp create `
  --resource-group <Your-Resource-Group> `
  --plan <Your-App-Service-Plan> `
  --name <Your-Web-App-Name> `
  --deployment-container-image-name <Your-ACR-Name>.azurecr.io/ropsaisandbox:latest
Configure the Web App
az webapp config container set `
  --name <Your-Web-App-Name> `
  --resource-group <Your-Resource-Group> `
  --docker-custom-image-name <Your-ACR-Name>.azurecr.io/ropsaisandbox:latest `
  --docker-registry-server-url https://<Your-ACR-Name>.azurecr.io `
  --docker-registry-server-user <Your-ACR-Username> `
  --docker-registry-server-password <Your-ACR-Password>
3. Update Environment Variables in Azure
Add Environment Variables
You can add environment variables directly in the Azure Portal or by using the CLI:

az webapp config appsettings set `
  --resource-group <Your-Resource-Group> `
  --name <Your-Web-App-Name> `
  --settings FORM_RECOGNIZER_ENDPOINT=<Value> FORM_RECOGNIZER_KEY=<Value> ...
Uploading Files
Audio Files: Upload .wav or .mp3 files for speech transcription.
Documents: Upload files to the source-documents container in Azure Blob Storage for translation.
Troubleshooting
Ensure the .env file is correctly set up for local development.
Verify your Azure subscription and permissions for the resource group and storage account.
Check the Azure Web App logs for runtime issues using:
az webapp log tail --name <Your-Web-App-Name> --resource-group <Your-Resource-Group>
