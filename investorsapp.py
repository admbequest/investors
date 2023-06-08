from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier

# Use o token do seu bot aqui
SLACK_BOT_TOKEN = "SLACK_BOT_TOKEN"
# Use o signing secret do seu aplicativo aqui
SLACK_SIGNING_SECRET = "SLACK_SIGNING_SECRET"

# Tokens do aplicativo Slack.
client = WebClient(token=SLACK_BOT_TOKEN)
signature_verifier = SignatureVerifier(SLACK_SIGNING_SECRET)

app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    # Verifique a assinatura do Slack.
    if not signature_verifier.is_valid(request.get_data(), request.headers):
        return make_response("invalid request", 403)

    # Pegue o evento do payload do Slack.
    slack_event = request.json
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        if event_type == "app_mention":
            channel_id = slack_event["event"]["channel"]
            client.chat_postMessage(channel=channel_id, text="Oi, tudo bem?")
            return make_response("", 200)
    
    # Caso contrário, se o evento não for tratado, retorne uma resposta de erro.
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids you're looking for.", 404, {"X-Slack-No-Retry": 1})

if __name__ == "__main__":
    app.run(port=3000)




