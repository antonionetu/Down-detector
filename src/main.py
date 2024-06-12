from sender import send_message
from utils import recipient_numbers
from endpoints import get_endpoints, get_all_errors


endpoints = get_endpoints()
errors = get_all_errors(endpoints)

for error in errors:
    for number in recipient_numbers():
        send_message(number, error)
