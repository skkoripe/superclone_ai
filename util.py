from google.cloud import language_v1
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

def generate_style_suggestions_with_openai(text, profession, target_audience):
    prompt = f"{text}\n\nProfession: {profession}\nTarget Audience: {target_audience}\n\nSuggest improvements:"
    completion = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=7,
        temperature=0
    )
    suggestions = completion['choices'][0]['text'].strip()
    return suggestions


def analyze_text_with_google(text):
    client = language_v1.LanguageServiceClient()
    document = {"content": text, "type": language_v1.Document.Type.PLAIN_TEXT}
    response = client.analyze_sentiment(request={'document': document})
    sentiment_score = response.document_sentiment.score
    return sentiment_score

