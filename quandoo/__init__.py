"""
Unofficial library, still in progress

Version:
 1.2.0

Author(s):
    Fraser Langton <fraserbasil@gmail.com>

GitHub:
    github.com/fraser-langton/Quandoo

Quandoo API docs:
    docs.quandoo.com (/swagger.html for better docs)
"""

from quandoo.Resources.Customer import Customer
from quandoo.Resources.ErrorResponse import ErrorResponse
from quandoo.Resources.Merchant import Merchant
from quandoo.Resources.QuandooModel import QuandooModel, urljoin
from quandoo.Resources.Reservation import Reservation

import requests
import json
from quandoo import config


class Agent:
    headers = {
        "accept": "application/json",
        "X-Quandoo-AuthToken": None
    }

    def __init__(self, oauth_token, agent_id):
        self.oauth_token = oauth_token
        self.agent_id = agent_id

        self.url = urljoin(config.url, config.version)
        self.headers["X-Quandoo-AuthToken"] = oauth_token

    def get_merchant(self, merchant_id):
        request = urljoin(self.url, "merchants", merchant_id)
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Merchant(json.loads(response.text), self)

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def get_customer(self, customer_id):
        request = urljoin(self.url, "customers", customer_id)
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Customer(json.loads(response.text), self)

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def get_reservation(self, reservation_id):
        request = urljoin(self.url, "reservations", reservation_id)
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Reservation(json.loads(response.text), self)

        raise ErrorResponse(response.status_code, json.loads(response.text))
