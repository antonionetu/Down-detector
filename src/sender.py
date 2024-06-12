import requests, json, os
from dotenv import load_dotenv

load_dotenv()

URL = f"https://graph.facebook.com/v20.0/{os.getenv('SENDER_NUMBER')}/messages"


def create_json(recipient, text):
    return json.dumps({
        "messaging_product": "whatsapp",
        "preview_url": False,
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {
            "body": text
        }
    })


def send_message(recipient, message):
    response = requests.post(URL, headers={
        "Content-type": "application/json",
        "Authorization": f"Bearer {os.getenv('CLIENT_SECRET')}",
    }, data=create_json(recipient, message))

    print(response.status_code)
    print(response.json())
