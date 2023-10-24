import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from chatbot_url import initialize_chatbot, conversational_chat

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
port = int(os.environ.get('PORT', 5000))

data_file_path = "Data/Retail_synthetic_data.csv"
chatbot_chain = initialize_chatbot(data_file_path)

@app.route('/send-prompt', methods=['POST'])
@cross_origin()
def send_prompt():
    prompt = request.json.get('prompt')

    if prompt:
        response = conversational_chat(chatbot_chain, prompt)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Ungültige JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)


