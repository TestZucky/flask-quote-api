import random

from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different.",
    "Simplicity is the soul of efficiency.",
]


@app.route("/")
def home():
    """Return a random quote as JSON."""
    return jsonify({"quote": random.choice(QUOTES)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
