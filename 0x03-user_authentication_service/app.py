#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    GET route that returns a JSON payload
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})
