from quandoo.QuandooModel import QuandooModel, urljoin, get_q_datetime
from quandoo.Reservation import Reservation, NewReservation
from quandoo.ErrorResponse import ErrorResponse
from quandoo.Customer import Customer
import json
import requests
from datetime import datetime, date


class Merchant(QuandooModel):

    def __init__(self, data, agent):
        self.id = data["id"]
        self.name = data["name"]

        self.agent = agent

        super().__init__(data)

    def get_customers(self):
        request = urljoin(self.agent.url, "merchants", self.id, "customers")
        response = requests.get(request, headers=self.agent.headers)

        if response.status_code == 200:
            return [Customer(i, self.agent) for i in json.loads(response.text)["result"]]

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def get_reservations(self):
        req = "{}/merchants/{}/reservations".format(self.agent.url, self.id)
        response = requests.get(req, headers=self.agent.headers)

        if response.status_code == 200:
            return [Reservation(i, self.agent) for i in json.loads(response.text)["reservations"]]

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def get_available_times(self, pax: int, date: date, time: str, duration=4):
        date = date.strftime("%Y-%m-%d")
        from_time = tuple(time.split(":"))
        to_time = str(int(time.split(":")[0]) + duration), time.split(":")[1]
        payload = "times?agentId={}&capacity={}&fromTime={}%3A{}&toTime={}%3A{}".format(
            self.agent.agent_id, pax, from_time[0], from_time[1], to_time[0], to_time[1])

        request = urljoin(self.agent.url, "merchants", self.id, "availabilities", date, payload)
        response = requests.get(request, headers=self.agent.headers)

        if response.status_code == 200:
            return json.dumps(json.loads(response.text), indent=2)

        raise ErrorResponse(response.status_code, json.loads(response.text))

    def create_reservation(self, customer, pax: int, date: date, time: str, duration=4):
        time = time.split(":")
        assert int(time[1]) % 15 == 0
        datetime_comb = datetime(date.year, date.month, date.day, int(time[0]), int(time[1]), 0)
        data = {
            "reservation": {
                "merchantId": self.id,
                "capacity": pax,
                "dateTime": get_q_datetime(datetime_comb)
            },
            "customer": customer.to_json(),
            "tracking": {
                "agent": {
                    "id": self.agent.agent_id
                }
            }
        }

        request = urljoin(self.agent.url, "reservations")
        response = requests.put(request, headers=self.agent.headers, json=data)

        if response.status_code == 200:
            return NewReservation(json.loads(response.text), self.agent)

        raise ErrorResponse(response.status_code, json.loads(response.text))

