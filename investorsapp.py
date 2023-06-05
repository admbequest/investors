from flask import Flask, request, jsonify
from slack_bolt import App
import os

# Configurar o adaptador de eventos
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
app = App(signing_secret=slack_signing_secret)

# Rota para receber as solicitações do Slack
@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    if "challenge" in data:
        # Responder ao desafio do Slack
        challenge = data["challenge"]
        return jsonify({"challenge": challenge})
    else:
        # Verificar se a solicitação é válida
        app.dispatch(request.data)

    return "", 200

# Manipulador de eventos
@app.event("app_mention")
def handle_app_mention(event, say):
    channel_id = event["channel"]

    # Enviar a resposta
    say(f"Olá! Tudo bem?")

if __name__ == "__main__":
    # Iniciar o servidor Flask
    app.start(port=3000)


