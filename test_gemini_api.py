import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ GOOGLE_API_KEY not found in .env file")
    exit(1)

print(f"Using API Key: {api_key[:5]}...{api_key[-5:]}")

# Corrected URL
url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"
headers = {"Content-Type": "application/json"}
params = {"key": api_key}
payload = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "Hello from Gemini REST API! What's 2+2?"}]
        }
    ]
}

print("Testing Gemini API connection...")
try:
    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload,
        timeout=10
    )
    
    if response.status_code == 200:
        result = response.json()
        try:
            print("✅ Success!")
            print("Response:", result['candidates'][0]['content']['parts'][0]['text'])
        except (KeyError, IndexError):
            print("❌ Unexpected response format")
            print("Full response:", json.dumps(result, indent=2))
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        
except Exception as e:
    print(f"❌ Request failed: {str(e)}")