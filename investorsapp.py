from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from slack_sdk.errors import SlackApiError
import json

app = Flask(__name__)

# Substitua pelo seu token
slack_token = 'SLACK_BOT_TOKEN'
client = WebClient(token=slack_token)

# Substitua pela sua signing secret
signing_secret = 'SLACK_SIGNING_SECRET'
signature_verifier = SignatureVerifier(signing_secret)

@app.route('/slack/events', methods=['POST'])
def slack_events():
    if not signature_verifier.is_valid_request(request.get_data().decode('utf-8'), request.headers):
        return make_response("Invalid request", 403)

    data = json.loads(request.data.decode('utf-8'))

    # Responda ao desafio HTTP do Slack
    if 'challenge' in data:
        return make_response(data['challenge'], 200, {"content_type": "application/json"})

    if 'event' in data:
        event_data = data['event']

        # Responda a menções com "Oi, tudo bem?"
        if 'type' in event_data and event_data['type'] == 'app_mention':
            channel = event_data['channel']
            try:
                response = client.chat_postMessage(channel=channel, text='Oi, tudo bem?')
            except SlackApiError as e:
                print(f"Error: {e}")

    return make_response("", 200)

if __name__ == "__main__":
    app.run(port=3000)



