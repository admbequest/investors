from slack_sdk import WebClient

# Defina o token de autenticação do seu aplicativo do Slack
slack_token = "xoxb-1666887890084-5336678265829-YaKNeHXpRxk2QXrPAvidxHp6"

# Crie uma nova instância do cliente Slack
client = WebClient(token=slack_token)

# Envie uma mensagem no canal desejado
channel_id = "C05ATA6JHDW" 
message = "Oi! Tudo bem?"
response = client.chat_postMessage(channel=channel_id, text=message)


