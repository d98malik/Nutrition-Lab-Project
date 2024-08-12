# app.py

from flask import Flask, request, jsonify
from chatbot import analyzer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    user_message = data.get('message', '')

    if user_message:
        response_message = analyzer(user_message)
        return jsonify({'response': response_message})
    else:
        return jsonify({'response': 'No message received'}), 400

if __name__ == '__main__':
    app.run(debug=True)