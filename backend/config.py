import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MAGIC_HOUR_API_KEY = os.getenv("MAGIC_HOUR_API_KEY")

IMAGE_MODEL = os.getenv(
    "IMAGE_MODEL",
    "flux-schnell"
)

if not MAGIC_HOUR_API_KEY:
    raise ValueError("MAGIC_HOUR_API_KEY not found in .env")

print("✓ Magic Hour configuration loaded")
print(f"✓ Model: {IMAGE_MODEL}")