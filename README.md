# ropsaisandbox

1. Clone the Repository
2. Set Up Environment Variables

Create a .env file in the project root with the following:
# Azure Keys
FORM_RECOGNIZER_ENDPOINT=<Your Azure Form Recognizer Endpoint>
FORM_RECOGNIZER_KEY=<Your Azure Form Recognizer Key>
SPEECH_ENDPOINT=<Your Azure Speech Endpoint>
SPEECH_KEY=<Your Azure Speech Key>
TRANSLATOR_ENDPOINT=<Your Azure Translator Endpoint>
DOCUMENT_TRANSLATOR_ENDPOINT=<Your Azure Document Translator Endpoint>
TRANSLATOR_KEY=<Your Azure Translator Key>
TEXT_ANALYTICS_ENDPOINT=<Your Azure Text Analytics Endpoint>
TEXT_ANALYTICS_KEY=<Your Azure Text Analytics Key>
TRANSLATOR_REGION=<Your region>

# Azure Storage
BLOB_STORAGE_CONNECTION_STRING=<Your Azure Blob Storage Connection String>
AZURE_SOURCE_CONTAINER_URL=<Your Source Container SAS URL>
AZURE_TARGET_CONTAINER_URL=<Your Target Container SAS URL>

3. Install Dependencies

pip install -r requirements.txt

4. Test Locally
Run the app locally to verify everything is set up:

streamlit run app.py

Docker Deployment

1. Build the Docker Image

docker build -t streamlit-ai-sandbox .

2. Run Locally in Docker

docker run -p 8501:8501 streamlit-ai-sandbox

Access the app at http://localhost:8501.

Deploy to Azure
1. Publish Docker Image to Azure Container Registry (ACR)

# Log in to Azure
az login

# Log in to ACR
az acr login --name <Your-ACR-Name>

# Tag the Docker image

docker tag streamlit-ai-sandbox <Your-ACR-Name>.azurecr.io/streamlit-ai-sandbox:latest

# Push to ACR
docker push <Your-ACR-Name>.azurecr.io/streamlit-ai-sandbox:latest

2. Deploy to Azure Web App

# Create Web App
az webapp create \
  --resource-group <Your-Resource-Group> \
  --plan <Your-App-Service-Plan> \
  --name <Your-Web-App-Name> \
  --deployment-container-image-name <Your-ACR-Name>.azurecr.io/streamlit-ai-sandbox:latest

# Configure Docker container
az webapp config container set \
  --name <Your-Web-App-Name> \
  --resource-group <Your-Resource-Group> \
  --docker-custom-image-name <Your-ACR-Name>.azurecr.io/streamlit-ai-sandbox:latest \
  --docker-registry-server-url https://<Your-ACR-Name>.azurecr.io \
  --docker-registry-server-user <Your-ACR-Username> \
  --docker-registry-server-password <Your-ACR-Password>

3. Update Environment Variables in Azure
Add environment variables in the Azure Portal or use:

az webapp config appsettings set \
  --resource-group <Your-Resource-Group> \
  --name <Your-Web-App-Name> \
  --settings "FORM_RECOGNIZER_ENDPOINT=<Value>" "FORM_RECOGNIZER_KEY=<Value>" ...
