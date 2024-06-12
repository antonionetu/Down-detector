import os
from dotenv import load_dotenv

load_dotenv()


def recipient_numbers() -> list:
    list_stringfied = os.getenv('RECIPIENT_NUMBERS')
    cleaned_list = list_stringfied[1:-1].split(', ')
    return cleaned_list


def create_error_message(project_url, path_like, endpoint, status) -> str:
    return f"ERRO: {path_like} do projeto {project_url} apresentou um erro na rota {endpoint}. Ele retornou o status {status}!"
