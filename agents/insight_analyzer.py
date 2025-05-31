import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class InsightAnalyzerAgent:
    def __init__(self):
        print("✅ InsightAnalyzerAgent initialized")
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            print("❌ GOOGLE_API_KEY not found in .env")
        # Using gemini-1.5-flash model which supports generateContent
        self.model_id = "gemini-1.5-flash"

    def analyze(self, data):
        print("🧠 Analyzing data with Gemini via REST API...")
        if not self.api_key:
            return {"error": "API key missing"}
        
        url = f"https://generativelanguage.googleapis.com/v1/models/{self.model_id}:generateContent?key={self.api_key}"
        headers = {'Content-Type': 'application/json'}
        
        prompt = f"""
        Analyze this user feedback data and extract key insights:
        {json.dumps(data, indent=2)}
        
        Provide:
        1. Summary of main themes
        2. Positive feedback highlights
        3. Critical issues to address
        4. Suggested action items
        """
        
        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "topP": 0.8,
                "maxOutputTokens": 1024
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and result['candidates']:
                    return {"insight": result['candidates'][0]['content']['parts'][0]['text']}
                return {"error": "No response from model", "full_response": result}
            return {"error": f"API Error {response.status_code}", "response": response.text}
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}