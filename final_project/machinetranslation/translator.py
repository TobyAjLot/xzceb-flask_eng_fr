import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)
language_translator.set_service_url(url)


def englishToFrench(english_text):
    """Takes an English word or sentence and translate to French"""
    text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    print(json.dumps(text, indent=2, ensure_ascii=False))
    french_text = text["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    """Takes an French word or sentence and translate to English"""
    text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    print(json.dumps(text, indent=2, ensure_ascii=False))
    english_text = text["translations"][0]["translation"]
    return english_text
