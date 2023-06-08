from flask import Flask, request, make_response, Response
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from slack_sdk.errors import SlackSignatureVerificationError

# Use o token do seu bot aqui
SLACK_BOT_TOKEN = "SEU_TOKEN_BOT_SLACK"
# Use o signing secret do seu aplicativo aqui
SLACK_SIGNING_SECRET = "SUA_SIGNING_SECRET"

# Inicializa o cliente Slack
slack_client = WebClient(token=SLACK_BOT_TOKEN)

# Inicializa o verificador de assinatura Slack
signature_verifier = SignatureVerifier(SLACK_SIGNING_SECRET)

app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Verifica se a requisição vem do Slack
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("Invalid request", 403)

    # Carrega o corpo da requisição JSON
    data = request.json

    # Slack envia um evento 'url_verification' quando configuramos o Event Subscription
    if data["type"] == "url_verification":
        return make_response(data.get("challenge"), 200)

    # Verifica se é um evento de mensagem com menção
    if "event" in data and data["event"]["type"] == "app_mention":
        event = data["event"]
        channel_id = event["channel"]
        # Responde à menção com a mensagem "Oi, tudo bem?"
        slack_client.chat_postMessage(channel=channel_id, text="Oi, tudo bem?")
        
    return make_response("", 200)


if __name__ == "__main__":
    # Executa o aplicativo Flask
    app.run(host='0.0.0.0', port=3000)



