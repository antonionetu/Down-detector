import requests, json, os
from dotenv import load_dotenv

load_dotenv()

def send_message(recipient, message):
    response = requests.post(os.getenv('WHATSAPP_API_URL'), headers={
        "Content-type": "application/json",
        "Authorization": f"Bearer {os.getenv('CLIENT_SECRET')}",
    }, json={
        "number": recipient,
        "body": message,
        "whatsappId": os.getenv('WHATSAPP_API_ID')
    })
