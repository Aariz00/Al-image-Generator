import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hugging Face Configuration
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "black-forest-labs/FLUX.1-dev")

# Hugging Face Inference API URL
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

# Request Headers
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

# Validate Configuration
if not HF_API_TOKEN:
    raise ValueError("HF_API_TOKEN not found. Please add it to your .env file.")

print("✓ Configuration Loaded")
print(f"✓ Model: {HF_MODEL}")