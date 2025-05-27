from vertexai.preview.generative_models import GenerativeModel
import vertexai

# Step 1: Initialize Vertex AI
vertexai.init(
    project="my-first-project-robust-atrium-460918-b1",  # ✅ Correct
    location="us-central1"                               # ✅ Correct
)

# Step 2: Load Gemini Pro model
model = GenerativeModel("gemini-pro")                    # ✅ Correct

# Step 3: Call the model
response = model.generate_content("Hello, Gemini!")      # ✅ Correct
print(response.text)
