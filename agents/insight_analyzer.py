import os
import vertexai
from vertexai.preview.generative_models import GenerativeModel

class InsightAnalyzerAgent:
    def __init__(self):
        print("✅ InsightAnalyzerAgent initialized")
        vertexai.init(
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location=os.getenv("LOCATION") or "us-central1"
        )

    def analyze(self, data):
        print("🧠 Analyzing data with Gemini...")
        model = GenerativeModel("gemini-pro")  # ✅ Changed to a public-access model
        prompt = f"Extract useful insights from this data: {data}"
        response = model.generate_content(prompt)
        return {"insight": response.text.strip()}
