import requests
import json

api_key = "AIzaSyB37zgDkQJq475ayeP5QN8JV2nDqBb3o7w"
model_id = "gemini-1.5-flash"
url = f"https://generativelanguage.googleapis.com/v1/models/{model_id}:generateContent?key={api_key}"

payload = {
    "contents": [{
        "role": "user",
        "parts": [{"text": "Hello from Gemini!"}]
    }]
}

response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))