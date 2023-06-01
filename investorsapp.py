

#!pip install slack_sdk

#!pip install slackeventsapi

#!pip install pydo

#RESPONDER MENÇÃO COM OLÁ

from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
import os
from pydo import wsgi

# Configurar o adaptador de eventos
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Configurar o cliente Slack
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_bot_token)

# Manipulador de eventos
@slack_events_adapter.on("app_mention")
def handle_app_mention(event_data):
    event = event_data["event"]
    channel_id = event["channel"]
    user_id = event["user"]

    # Enviar a resposta
    client.chat_postMessage(channel=channel_id, text="Olá!")

# Iniciar o servidor de eventos usando a biblioteca pydo
if __name__ == "__main__":
    wsgi.server(slack_events_adapter, port=3000)
