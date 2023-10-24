import requests

# Die URL deines Flask-Webdienstes
url = 'http://127.0.0.1:3000/send-prompt' 

# Der Prompt, den du senden möchtest
prompt = "What is the Data about?"

# Die Daten, die du in der POST-Anfrage senden möchtest (im JSON-Format)
data = {'prompt': prompt}

# Sende die POST-Anfrage
response = requests.post(url, json=data)

# Überprüfe die Antwort
if response.status_code == 200:
    # Die Antwort des Servers (die Antwort des Chatbots) als JSON
    chatbot_response = response.json()
    print("Chatbot-Antwort:", chatbot_response["response"])
else:
    print("Fehler bei der Anfrage:", response.status_code)
