from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')


from google.oauth2 import service_account
from flask import request
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession

PROJECT_ID = "honbu-datamarketing-training"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route('/chat', methods=['POST'])
def chat_with_model():
    prompt = request.json['prompt']
    response = chat.send_message(prompt)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)