from flask import Flask, render_template, request, jsonify
import json
import random
from chatbot import get_response, predict_class

app = Flask(__name__)

# Load intents in app.py
intents = json.loads(open('intent.json').read())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    ints = predict_class(message)
    res = get_response(ints, intents)
    return jsonify({'response': res})

# API endpoint
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    message = data['message']
    ints = predict_class(message)
    res = get_response(ints, intents)
    return jsonify({'response': res})

if __name__ == '__main__':
    app.run(debug=True)
