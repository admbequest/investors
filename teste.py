from slack_sdk import WebClient
import os

# Configurar o token do bot do Slack
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_bot_token)

# ID do canal ou grupo onde a mensagem será enviada
channel_id = "C05ATA6JHDW"

# Enviar a mensagem
response = client.chat_postMessage(channel=channel_id, text="Oi")

# Verificar se a mensagem foi enviada com sucesso
if response["ok"]:
    print("Mensagem enviada com sucesso!")
else:
    print("Falha ao enviar mensagem:", response["error"])


