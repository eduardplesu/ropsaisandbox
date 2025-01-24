import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TRANSLATOR_KEY = os.getenv("TRANSLATOR_KEY")
TRANSLATOR_ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")
TRANSLATOR_REGION = os.getenv("TRANSLATOR_REGION")
TEXT_ANALYTICS_ENDPOINT = os.getenv("TEXT_ANALYTICS_ENDPOINT")
TEXT_ANALYTICS_KEY = os.getenv("TEXT_ANALYTICS_KEY")


def detect_language(text: str) -> str:
    """
    Detects the language of the input text using Azure Text Analytics.
    """
    endpoint = f"{TEXT_ANALYTICS_ENDPOINT}/text/analytics/v3.1/languages"
    headers = {
        "Ocp-Apim-Subscription-Key": TEXT_ANALYTICS_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }
    body = {"documents": [{"id": "1", "text": text}]}

    try:
        response = requests.post(endpoint, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        detected_language = data["documents"][0]["detectedLanguage"]["iso6391Name"]
        return detected_language
    except Exception as e:
        raise Exception(f"Failed to detect language: {e}")


async def translate_text(text: str, from_language: str, to_language: str) -> str:
    """
    Translate text using Azure Translator Text API.
    """
    if from_language == "auto":
        from_language = ""  # Azure API interprets empty 'from' as auto-detect.

    endpoint = f"{TRANSLATOR_ENDPOINT}/translate?api-version=3.0"
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }
    params = {"from": from_language, "to": to_language}
    body = [{"text": text}]

    try:
        response = requests.post(endpoint, headers=headers, params=params, json=body)
        response.raise_for_status()
        translations = response.json()
        return translations[0]["translations"][0]["text"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error in translation request: {e}")
