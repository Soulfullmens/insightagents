import requests

api_key = "AIzaSyB37zgDkQJq475ayeP5QN8JV2nDqBb3o7w"
url = f"https://generativelanguage.googleapis.com/v1/models?key={api_key}"

response = requests.get(url)
if response.status_code == 200:
    models = response.json().get('models', [])
    print("Available Models (with supported methods):")
    for model in models:
        name = model['name']
        methods = ', '.join(model.get('supportedGenerationMethods', []))
        print(f"- {name} (Supports: {methods})")
        
    # Find models that support generateContent
    content_models = [m for m in models if 'generateContent' in m.get('supportedGenerationMethods', [])]
    if content_models:
        print("\nModels that support generateContent:")
        for model in content_models:
            print(f"- {model['name']}")
    else:
        print("\nNo models found that support generateContent")
else:
    print(f"Error: {response.status_code}")
    print(response.text)