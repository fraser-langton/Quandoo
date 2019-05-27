import requests
import json
from datetime import datetime, date, timedelta

TEST = True
# TEST = False

base_url = "https://api.quandoo.com"
base_url_test = "https://test-api.quandoo.com"
url = base_url_test * int(TEST) + base_url * int(not TEST)

oauth_token = "30d6f5ef-0b46-4b36-a187-1ad7c4491f99"
agent_id = "94"

merchant_id_test = "33226"

headers = {
            "accept": "application/json",
            "X-Quandoo-AuthToken": oauth_token
        }


def main():
    customer = Customer(
        {
            "id": 1,
            "firstName": "Fraser",
            "lastName": "Basil",
            "email": "fraserbasil@mail.com",
            "phoneNumber": "0466920029",
            "locale": "en_AU",
            "country": "AU"
        }
    )
    # for i in get_merchant(merchant_id_test).get_reservations():
    #     print(i)
    #     print(get_customer(i.customerId))
    #     print()
    # exit()
    # print(get_reservation("be11e28c-b7e9-4667-8067-739bcbfb47ad"))
    # exit()
    # print(get_merchant(merchant_id_test).create_reservation(customer, 2, date.today() + timedelta(days=1), "12:00"))
    # exit()
    print(get_merchant(merchant_id_test).get_available_times(2, date.today() + timedelta(days=1), "12:00"))
    exit()
    for i in get_merchant(merchant_id_test).get_customers():
        print(i)
    exit()


def get_merchant(merchant_id):
    headers = {
        "accept": "application/json",
        "X-Quandoo-AuthToken": oauth_token
    }
    response = requests.get("{}/v1/merchants/{}".format(url, merchant_id), headers=headers)
    if response.status_code == 200:
        return Merchant(json.loads(response.text))
    return ErrorResponse(json.loads(response.text))


def get_customer(customer_id):
    headers = {
        "accept": "application/json",
        "X-Quandoo-AuthToken": oauth_token
    }
    response = requests.get("{}/v1/customers/{}".format(url, customer_id), headers=headers)
    if response.status_code == 200:
        return Customer(json.loads(response.text))
    return ErrorResponse(json.loads(response.text))


def get_reservation(reservation_id):
    headers = {
        "accept": "application/json",
        "X-Quandoo-AuthToken": oauth_token
    }
    response = requests.get("{}/v1/reservations/{}".format(url, reservation_id), headers=headers)
    if response.status_code == 200:
        return Reservation(json.loads(response.text))
    return ErrorResponse(json.loads(response.text))


class Merchant:

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

    def __str__(self):
        return "Merchant({}, {}".format(
            self.id,
            self.name
        )

    def get_customers(self):
        r = requests.get("{}/v1/merchants/{}/customers".format(url, self.id), headers=headers)
        r = json.loads(r.text)["result"]
        return [Customer(i) for i in r]

    def get_available_times(self, pax, date, time, duration=4):
        date = date.strftime("%Y-%m-%d")
        from_time = tuple(time.split(":"))
        to_time = str(int(time.split(":")[0]) + duration), time.split(":")[1]

        req = "{}/v1/merchants/{}/availabilities/{}/times?agentId={}&capacity={}&fromTime={}%3A{}&toTime={}%3A{}".format(url, self.id, date, agent_id, pax, from_time[0], from_time[1], to_time[0], to_time[1])
        response = requests.get(req, headers=headers)
        if response.status_code == 200:
            return json.dumps(json.loads(response.text), indent=2)
        return ErrorResponse(json.loads(response.text))

    def create_reservation(self, customer, pax, date: date, time, duration=4):
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
                    "id": agent_id
                }
            }
        }

        req = "{}/v1/reservations".format(url)
        response = requests.put(req, headers=headers, json=data)
        if response.status_code == 200:
            return response.text
        return ErrorResponse(json.loads(response.text))

    def get_reservations(self):
        req = "{}/v1/merchants/{}/reservations".format(url, self.id)
        response = requests.get(req, headers=headers)
        if response.status_code == 200:
            return [Reservation(i) for i in json.loads(response.text)["reservations"]]
        return ErrorResponse(json.loads(response.text))


class Customer:

    def __init__(self, data):
        self.id = data["id"]
        self.firstName = data["firstName"]
        self.lastName = data["lastName"]
        self.email = data["email"]
        self.phoneNumber = data["phoneNumber"]

    def __str__(self):
        return "Customer({}, {}, {}, {}, {})".format(
            self.id,
            self.firstName,
            self.lastName,
            self.email,
            self.phoneNumber,
        )

    def to_json(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "emailAddress": self.email,
            "phoneNumber": self.phoneNumber,
            "locale": "en_AU",
            "country": "AU"
        }


class Reservation:

    def __init__(self, data):
        self.id = data["id"]
        self.status = data["status"]
        self.startTime = data["startTime"]
        self.endTime = data["endTime"]
        self.capacity = data["capacity"]
        self.merchantId = data["merchantId"]
        self.customerId = data["customerId"]

    def __str__(self):
        return "Reservation({}, {}, {}, {}, {}, {}, {})".format(
            self.id,
            self.status,
            self.startTime,
            self.endTime,
            self.capacity,
            self.merchantId,
            self.customerId,
        )


class ErrorResponse:

    def __init__(self, data):
        self.errorType = data["errorType"]
        self.errorMessage = data["errorMessage"]

    def __str__(self):
        return "{}: {}".format(self.errorType, self.errorMessage)


def get_datetime(data):
    return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S%z")


def get_q_datetime(data):
    return datetime.strftime(data, "%Y-%m-%dT%H:%M:%S%z") + "+10:00"


if __name__ == '__main__':
    main()
