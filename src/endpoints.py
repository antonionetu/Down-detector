import os
import requests, json
from dotenv import load_dotenv

from utils import create_error_message

load_dotenv()
SERVICES_STATUS_URL = os.getenv('SERVICES_STATUS_URL')


def get_endpoints() -> list:
    response = requests.get(f'{SERVICES_STATUS_URL}/v1.0/endpoints')
    response_json = response.json()
    return response_json


def get_all_errors(endpoints) -> list:
    errors = []

    for project in endpoints:
        for path in project.get('Paths'):
            if path.get('Status') == 200:
                url = project.get('ProjectUrl')
                path_like = path.get('PathAKA')
                endpoint = path.get('Path')
                status = path.get('Status')

                error_message = create_error_message(url, path_like, endpoint, status)
                errors.append(error_message)

    return errors
