from flask import Flask, request
import settings
import services  

app = Flask(__name__)

# Verificación de conexión con Flask
@app.route('/bienvenido', methods=['GET'])
def bienvenido():
    return 'Hola, soy tu chatbot'

# Verificación de conexión con Webhook
@app.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('get_webhook_token')
        challenge = request.args.get('hub.challenge')

        if token == settings.token and challenge is not None:
            return challenge
        else:
            return 'Error', 403
    except Exception as e:
        return str(e), 403

# Manejo de mensajes del webhook
@app.route('/webhook', methods=['POST'])
def mensaje():
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]

        number = message['from']
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = services.obtener_Mensaje_whatsapp(message)

        services.administrar_bot(text, number, messageId, name)
        return 'enviado'
    
    except Exception as e:
        return 'no enviado: ' + str(e)

if __name__ == '__main__':
    app.run()
