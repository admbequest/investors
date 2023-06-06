import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request, jsonify

# Criar o objeto de aplicativo Flask
flask_app = Flask(__name__)

# Criar o objeto de aplicativo Slack Bolt
app = App(token=os.environ["SLACK_BOT_TOKEN"], signing_secret=os.environ["SLACK_SIGNING_SECRET"], process_before_response=True)

# Configurar o adaptador de solicitações do Slack para Flask
handler = SlackRequestHandler(app)

# Rota para receber as solicitações do Slack
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    # Obter a solicitação do Slack
    slack_request = handler.handle(request)

    # Verificar se a solicitação contém um challenge
    if slack_request.body.get("challenge"):
        challenge = slack_request.body["challenge"]
        return jsonify({"challenge": challenge})

    # Confirmar o recebimento do evento
    return jsonify(), 200

# Manipulador de eventos
@app.event("app_mention")
def handle_app_mention(event, say):
    channel_id = event["channel"]

    # Enviar a resposta
    say("Olá! Tudo bem?")

if __name__ == "__main__":
    # Iniciar o servidor do Flask
    flask_app.run(host="0.0.0.0", port=3000)



