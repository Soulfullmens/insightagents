from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel
import os

project_id = "robust-atrium-460918-b1"
location = "us-central1"

aiplatform.init(project=project_id, location=location)

try:
    model = GenerativeModel("gemini-1.0-pro-001")
    response = model.generate_content("Hello world")
    print("✅ Success! Response:", response.text)
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("Troubleshooting steps:")
    print("1. Check billing status")
    print("2. Verify project number:", aiplatform.global_config.project_number)
    print("3. Try different region")