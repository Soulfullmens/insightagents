import google.generativeai as genai

genai.configure(api_key="AIzaSyB37zgDkQJq475ayeP5QN8JV2nDqBb3o7w")

# Use a model that exists in your account
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Hello from Gemini!")
print(response.text)