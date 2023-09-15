from datetime import datetime

import requests
from app.api.consts import URL


def convert(from_c: str, to_c: str) -> int:
    req_url = URL + from_c
    response = requests.get(req_url).json()
    return response["conversion_rates"][to_c]


def form_payload(value: int, from_c: str, to_c: str):
    res = convert(from_c, to_c) * value
    data = {'from_currency': from_c,
            'to_currency': to_c,
            'value': value,
            'converted_value': res,
            'datetime': str(datetime.utcnow()),
            }
    return data
