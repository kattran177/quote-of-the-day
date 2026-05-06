from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of tech quotes
quotes = [
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Programmes must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Code is like humour. When you have to explain it, it’s bad. – Cory House"
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)