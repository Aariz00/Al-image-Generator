from flask import Blueprint, request, jsonify
from backend.image_generator import generate_image

# Create Blueprint
main = Blueprint("main", __name__)

# Test Route
@main.route("/", methods=["GET"])
def home():
    return "AI Image Generator API Running"

# Generate Image Route
@main.route("/generate", methods=["POST"])
def generate():

    try:
        # Receive JSON
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data received."
            }), 400

        # Extract prompt
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({
                "error": "Prompt is required."
            }), 400

        # Generate Image
        filename = generate_image(prompt)

        # Return JSON
        return jsonify({
            "success": True,
            "image": f"/outputs/{filename}"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500