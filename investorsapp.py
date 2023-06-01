from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
import os

# Configurar o adaptador de eventos
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Configurar o cliente Slack
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_bot_token)

# Criar o objeto Flask
app = Flask(__name__)

# Rota para receber as solicitações do Slack
@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Verificar se a solicitação é válida
    slack_events_adapter.handle(request)

    return "", 200

# Manipulador de eventos
@slack_events_adapter.on("app_mention")
def handle_app_mention(event_data):
    event = event_data["event"]
    channel_id = event["channel"]

    # Adicionar mensagem de depuração
    print("Evento de menção do aplicativo recebido!")

    # Enviar a resposta
    client.chat_postMessage(channel=channel_id, text="Olá!")

if __name__ == "__main__":
    # Iniciar o servidor usando o Gunicorn
    app.run(host="0.0.0.0", port=3000, threaded=True)

