import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
# Initializing the LanguageTranslatorV3 model
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Initializing the Language model with url
language_translator.set_service_url(url)

# The method translates English text to French
def englishToFrench(english_text):
    """The method translates English text to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print("translation : ",translation)
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    french_text = translation["translations"][0]["translation"]
    #print("french_text : ",french_text)
    return french_text


# The method translates French text to English
def frenchToEnglish(french_text):
    """The method translates French text to English"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
