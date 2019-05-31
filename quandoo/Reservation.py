from quandoo.Error import ErrorResponse
from quandoo.QuandooModel import urljoin, QuandooModel
import json
import requests


class Reservation(QuandooModel):

    def __init__(self, data, agent):
        self.id = data["id"]
        self.status = data["status"]
        self.startTime = data["startTime"]
        self.endTime = data["endTime"]
        self.capacity = data["capacity"]
        self.merchantId = data["merchantId"]
        self.customerId = data["customerId"]

        self.agent = agent

        super().__init__(data)

    def cancel(self):
        data = {
            "reservation": {
                "status": "CUSTOMER_CANCELED"
            }
        }

        request = urljoin(self.agent.url, "reservations", self.id)
        response = requests.patch(request, headers=self.agent.headers, json=data)

        if response.status_code == 200:
            self.status = "CUSTOMER_CANCELED"
            return

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def reconfirm(self):
        data = {
            "reservation": {
                "status": "RECONFIRMED"
            }
        }

        request = urljoin(self.agent.url, "reservations", self.id)
        response = requests.patch(request, headers=self.agent.headers, json=data)

        if response.status_code == 200:
            self.status = "RECONFIRMED"
            return

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def change_capacity(self, new_capacity):
        data = {
            "reservation": {
                "capacity": new_capacity,
            }
        }

        request = urljoin(self.agent.url, "reservations", self.id)
        response = requests.patch(request, headers=self.agent.headers, json=data)

        if response.status_code == 200:
            self.capacity = new_capacity
            return

        raise ErrorResponse(response.status_code, json.loads(response.text))


class NewReservation(QuandooModel):

    def __init__(self, data, agent):
        self.id = data["reservation"]["id"]
        self.number = data["reservation"]["number"]
        self.status = data["reservation"]["status"]
        self.customerId = data["customer"]["id"]

        self.agent = agent

        super().__init__(data)

    def get_reservation(self):
        return self.agent.get_reservation(self.id)

