import os
import uuid
import requests

from backend.config import API_URL, HEADERS


# Output folder
OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_image(prompt):
    """
    Generate an image using Hugging Face FLUX.1-dev.

    Args:
        prompt (str): Text prompt describing the image.

    Returns:
        str: Generated image filename.
    """

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload,
        timeout=300
    )

    if response.status_code != 200:
        raise Exception(
            f"Hugging Face Error {response.status_code}: {response.text}"
        )

    # Create unique filename
    filename = f"{uuid.uuid4().hex}.png"

    filepath = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    # Save image
    with open(filepath, "wb") as image:
        image.write(response.content)

    return filename