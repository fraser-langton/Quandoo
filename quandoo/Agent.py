import json

import requests

from . import config
from .QuandooModel import PrettyClass
from .Merchant import Merchant
from .Error import PoorResponse
from .Customer import Customer
from .Reservation import Reservation
from .ReservationEnquiry import ReservationEnquiry


class Agent(PrettyClass):
    headers = {
        "accept": "application/json",
        "X-Quandoo-AuthToken": None
    }

    def __init__(self, oauth_token=None, agent_id=None, test=False):
        self.oauth_token = oauth_token
        self.agent_id = agent_id

        self.url = f'{config.base_url_test if test else config.base_url}/{config.version}'

        self.headers["X-Quandoo-AuthToken"] = oauth_token

    def get_merchant(self, merchant_id):
        request = f"{self.url}/merchants/{merchant_id}"
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Merchant(json.loads(response.text), self)

        raise PoorResponse(response.status_code, json.loads(response.text), request)

    def get_customer(self, customer_id):
        request = f"{self.url}/customers/{customer_id}"
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Customer(json.loads(response.text), self)

        raise PoorResponse(response.status_code, json.loads(response.text), request)

    def get_reservation(self, reservation_id):
        request = f"{self.url}/reservations/{reservation_id}"
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return Reservation(json.loads(response.text), self)

        raise PoorResponse(response.status_code, json.loads(response.text), request)

    def get_reservation_enquiry(self, reservation_enquiry_id):
        request = f"{self.url}/reservation-enquiries/{reservation_enquiry_id}"
        response = requests.get(request, headers=self.headers)

        if response.status_code == 200:
            return ReservationEnquiry(json.loads(response.text), self)

        raise PoorResponse(response.status_code, json.loads(response.text), request)

    def merchants(self, params=None):
        request = f"{self.url}/merchants"
        response = requests.get(request, headers=self.headers, params=params)

        if response.status_code == 200:
            return [Merchant(i, self) for i in json.loads(response.text)['merchants']]

        raise PoorResponse(response.status_code, json.loads(response.text), request)
