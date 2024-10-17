import requests
import settings
import json

def obtener_Mensaje_whatsapp(menssage):
    if 'type' in menssage:
        text = 'Mensaje no reconocido'
        typeMenssage = menssage['type']
        if typeMenssage == 'text':
            text = menssage['body']
        return text

def enviar_Mensaje_whatsapp(data):
    try:
        whatsapp_token = settings.whatsapp_token
        whatsapp_url = settings.whatsapp_url
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + whatsapp_token
        }
        print("se envia ", data)
        response = requests.post(whatsapp_url, headers=headers, data=data)
        
        if response.status_code == 200:
            return 'mensaje enviado', 200
        else:
            return 'error al enviar mensaje', response.status_code
    except Exception as e:
        return e, 403

def Text_Menssage(number, text):
    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    })
    return data

def administrar_bot(text, number, messageId, name):
    text = text.lower()
    list = []  
    data = Text_Menssage(number, "Hola soy un maiz bot")
    enviar_Mensaje_whatsapp(data)
