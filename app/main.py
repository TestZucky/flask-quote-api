from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Fix the cause, not the symptom.",
    "First, solve the problem. Then, write the code."
]

@app.route('/')
def home():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == '__main__':
    app.run(debug=True)
