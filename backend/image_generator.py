import os
import uuid
import shutil

from magic_hour import Client

from backend.config import MAGIC_HOUR_API_KEY, IMAGE_MODEL

# Output folder
OUTPUT_FOLDER = os.path.join(os.getcwd(), "outputs")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize Magic Hour client
client = Client(token=MAGIC_HOUR_API_KEY)


def generate_image(prompt):
    """
    # Generate an image using Magic Hour AI.
    """

    try:
        result = client.v1.ai_image_generator.generate(
            image_count=1,
            model=IMAGE_MODEL,
            aspect_ratio="1:1",
            style={
                "prompt": prompt
            },
            wait_for_completion=True,
            download_outputs=True,
            download_directory=OUTPUT_FOLDER
        )

    except Exception as e:
        raise Exception(f"Magic Hour Error: {e}")

    # Ensure an image was downloaded
    if not hasattr(result, "downloaded_paths") or len(result.downloaded_paths) == 0:
        raise Exception("No image returned from Magic Hour.")

    downloaded_file = result.downloaded_paths[0]

    filename = f"{uuid.uuid4().hex}.png"

    destination = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    shutil.move(downloaded_file, destination)

    return filename