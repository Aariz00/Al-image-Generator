from flask import Flask
from flask_cors import CORS
from backend.routes import main

# Create Flask App
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load Routes
app.register_blueprint(main)

# Run Server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )