from dotenv import load_dotenv
import os
from google.cloud import storage

# ✅ Load the environment variables from .env
load_dotenv()

# ✅ Get the credentials path
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print("Using credentials from:", credentials_path)

# ✅ Check if file exists and print first line
if not os.path.exists(credentials_path):
    print("❌ Credentials file not found!")
else:
    with open(credentials_path, 'r') as f:
        first_line = f.readline()
        print("✅ Found credentials file. Starts with:", first_line[:50])

def test_auth():
    try:
        # ✅ Explicitly specify the project
        client = storage.Client(project="robust-atrium-460918-b1")
        buckets = list(client.list_buckets())
        print("✅ Credentials are valid!")
        print("Buckets in project:")
        for bucket in buckets:
            print("-", bucket.name)
    except Exception as e:
        print("❌ Something went wrong:", e)

test_auth()
