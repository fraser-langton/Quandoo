# Quandoo for Python

A Python library to access the [Quandoo API (v1)](https://docs.quandoo.com/). Base functionality is covered and more peripheral features are being covered in due course.


## Installation

Install using pip :
```sh
$ pip install Quandoo
```

## Include Quandoo in your application
```python
import quandoo
```

## Check API status

```python
quandoo.status()
quandoo.status_test()
```

```commandline
200
200
```

## Get API Key + Agent ID

These are obtained directly from a Quandoo representative. [Quandoo docs on authentication.](https://docs.quandoo.com/authentication-and-attribution/)

```python
oauth_token = "<oauth_token>"
agent_id = "<agent_id>"
```

## Get Quandoo Agent instance

To get an [Agent](#agent) instance to Quandoo just provide the X-Quandoo-AuthToken and your Agent ID. 


```python
import quandoo.Agent
agent = quandoo.Agent.Agent(oauth_token, agent_id)
```

To get a test [Agent](#agent) instance be sure to use your test credentials

```python
import quandoo.Agent
agent_test = quandoo.Agent.Agent(oauth_token_test, agent_id_test, test=True)
```

# Usage
## Agent

See [Quandoo Docs](https://docs.quandoo.com/quandoo-terminology/)

#### Get Merchant

Takes a Merchant ID:

```python
agent.get_merchant("123456")
```
Returns a [Merchant](#merchant) object:
```commandline
Merchant(
	id: 123456,
	name: The Best Restaurant
)
```

#### Merchant search

Takes a dictionary of parameters, as outlined in [Quandoo docs](https://docs.quandoo.com/interactive-api/)

```python
search_params = {
    'centerPoint': '-34.9284989,138.6007456',
    'date': '2019-09-01',
    'fromTime': '20:00',
    'limit': '3',
    'bookable': 'true'
}
merchants = agent.merchants(params=search_params)
```

Returns a list of [Merchants](#merchant)

```commandline
[
	Merchant(
		id: 15733,
		name: House Of Chow,
		address: number, city, country
	), 
	Merchant(
		id: 16446,
		name: Namaste Nepalese,
		address: number, city, country
	), 
	Merchant(
		id: 18652,
		name: Phonatic,
		address: number, city, country
	)]
```

#### Get Customer

Takes a Customer ID:

```python
agent.get_customer("0bd07451-0c0e-40e9-8429-8a589f59e254")
```
Returns a [Customer](#customer) object:
```commandline
Customer(
	id: 0bd07451-0c0e-40e9-8429-8a589f59e254,
	firstName: Fraser,
	lastName: Basil,
	email: fraserbasil@mail.com,
	phoneNumber: +614111222333
)

```

#### Get Reservation

Takes a Reservation ID:

```python
agent.get_reservation("77f9dd33-9b24-4a66-a58c-7a059cecba5f")
```
Returns a [Reservation](#reservation) object:
```commandline
Reservation(
    id: 1e346889-7819-4648-85c3-500a075bd470,
    status: MERCHANT_CANCELED,
    date: Mon 20 January 2020,
    startTime: 12:00 PM,
    endTime: 3:00 PM,
    capacity: 2,
    merchantId: 49295,
    customerId: 4d3f588b-3dc7-4a9c-bcf2-399cb8dcce68
)
```

#### Get ReservationEnquiry

Takes a ReservationEnquiry ID:

```python
agent.get_reservation_enquiry("a4711a61-2282-4dc8-8229-99b526bdf0b6")
```
Returns a [ReservationEnquiry](#reservationenquiry) object:
```commandline
ReservationEnquiry(
	id: a4711a61-2282-4dc8-8229-99b526bdf0b6,
	merchantId: 33226,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254,
	capacity: 2,
	startTime: 2019-09-01T02:00+10:00[Australia/Sydney],
	endTime: 2019-09-01T04:00+10:00[Australia/Sydney],
	status: NEW
)
```

## Merchant

See [Quandoo Docs](https://docs.quandoo.com/quandoo-terminology/)

#### Get Customers

Takes optional: offset, limit, modified_since and modified_until

```python
merchant.get_customers()
```

Returns list of [Customers](#customer)

```commandline
[
    Customer(
        id: 0bd07451-0c0e-40e9-8429-8a589f59e254,
        firstName: Fraser,
        lastName: Basil,
        email: fraserbasil@mail.com,
        phoneNumber: +61466920029
    ), 
    Customer(
        id: 2b2a541b6-e352-414d-j62f-71ad9fb695d,
        firstName: Carmen,
        lastName: Test,
        email: carmen.test@mail.com,
        phoneNumber: +123456789
    )]
```

#### Get Reservations

Takes optional: offset, limit, earliest and latest

```python
merchant.get_reservations(limit=2, earliest=QuandooDatetime(2020, 1, 20), latest=QuandooDatetime(2020, 2, 2))
```

Returns a list of [Reservation](#reservation) objects:

```commandline
[
	Reservation(
		id: 1e346889-7819-4648-85c3-500a075bd470,
		status: MERCHANT_CANCELED,
		date: Mon 20 January 2020,
		startTime: 12:00 PM,
		endTime: 3:00 PM,
		capacity: 2,
		merchantId: 49295,
		customerId: 4d3f588b-3dc7-4a9c-bcf2-399cb8dcce68
	), 
	Reservation(
		id: 2af875ba-a01e-4721-8988-96bbcc5f4863,
		status: MERCHANT_CANCELED,
		date: Mon 20 January 2020,
		startTime: 12:00 PM,
		endTime: 3:00 PM,
		capacity: 6,
		merchantId: 49295,
		customerId: e4f5d267-6891-4e48-9632-b8de038bbd45
	)]
```

#### Get Available Times

Takes a capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime).
Optional: duration=2, area_id

```python
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

merchant.get_available_times(capacity, res_datetime)
```

Returns list of [QuandooDatetime](#quandoodatetime) objects

```commandline
[
	QuandooDatetime(
		datetime: 2019-07-01 12:00:00+10:00,
		q_datetime: 2019-07-01T12:00:00+10:00,
		pretty_date: 12:00 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 12:15:00+10:00,
		q_datetime: 2019-07-01T12:15:00+10:00,
		pretty_date: 12:15 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 12:30:00+10:00,
		q_datetime: 2019-07-01T12:30:00+10:00,
		pretty_date: 12:30 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 12:45:00+10:00,
		q_datetime: 2019-07-01T12:45:00+10:00,
		pretty_date: 12:45 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 13:00:00+10:00,
		q_datetime: 2019-07-01T13:00:00+10:00,
		pretty_date: 1:00 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 13:15:00+10:00,
		q_datetime: 2019-07-01T13:15:00+10:00,
		pretty_date: 1:15 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 13:30:00+10:00,
		q_datetime: 2019-07-01T13:30:00+10:00,
		pretty_date: 1:30 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 13:45:00+10:00,
		q_datetime: 2019-07-01T13:45:00+10:00,
		pretty_date: 1:45 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 14:00:00+10:00,
		q_datetime: 2019-07-01T14:00:00+10:00,
		pretty_date: 2:00 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 14:15:00+10:00,
		q_datetime: 2019-07-01T14:15:00+10:00,
		pretty_date: 2:15 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 14:30:00+10:00,
		q_datetime: 2019-07-01T14:30:00+10:00,
		pretty_date: 2:30 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 14:45:00+10:00,
		q_datetime: 2019-07-01T14:45:00+10:00,
		pretty_date: 2:45 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 15:00:00+10:00,
		q_datetime: 2019-07-01T15:00:00+10:00,
		pretty_date: 3:00 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 15:15:00+10:00,
		q_datetime: 2019-07-01T15:15:00+10:00,
		pretty_date: 3:15 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 15:30:00+10:00,
		q_datetime: 2019-07-01T15:30:00+10:00,
		pretty_date: 3:30 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 15:45:00+10:00,
		q_datetime: 2019-07-01T15:45:00+10:00,
		pretty_date: 3:45 PM, Mon 1 July 2019
	), 
	QuandooDatetime(
		datetime: 2019-07-01 16:00:00+10:00,
		q_datetime: 2019-07-01T16:00:00+10:00,
		pretty_date: 4:00 PM, Mon 1 July 2019
	)]
```

#### Check if specific time is available

Takes a capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime).
Optional: duration=2, area_id

```python
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

merchant.is_available(capacity, res_datetime)
```

Returns a boolean

```commandline
True
```

#### Get reviews
Takes optional: offset and limit

```python
merchant.get_reviews()
```

Returns json dump

```commandline
{
  "reviews": [
    {
      "customer": {
        "firstName": "Kotaro",
        "lastName": "F"
      },
      "rating": 3,
      "description": "We felt a cheap atmosphere and couldn't receive a kind service at all.  ",
      "locale": "en_GB",
      "date": "2019-03-28"
    }
  ],
  "size": 1,
  "offset": 0,
  "limit": 10
}
```

#### Create Reservation

Takes a [Customer](#customer), capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime). 
Optional: area_id, order_id, extra_info

```python
customer = agent.get_customer(customer_id)
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

merchant.create_reservation(customer, capacity, res_datetime)
```

Returns a [NewReservation](#newreservation) object:

```commandline
NewReservation(
	id: b97d9da6-b38f-4089-8456-514201dc94d5,
	number: 13096703,
	status: AUTOMATIC_CONFIRMED,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
)
```

#### Create Reservation Enquiry

Takes a [Customer](#customer), capacity for the reservation, start and end times as a [QuandooDatetime](#quandoodatetime) and a message. 

```python
customer = agent.get_customer(customer_id)
capacity = 2
start_qdt, end_qdt = QuandooDatetime(year, month, day, 12), QuandooDatetime(year, month, day, 14)
message = "Looking for a table please!"

merchant.create_reservation_enquiry(customer, capacity, start_qdt, end_qdt, message)
```

Returns a [NewReservationEnquiry](#newreservationenquiry) object:

```commandline
New ReservationEnquiry(
	id: a869da69-939a-416a-afa4-eb875ae4575e,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
)
```

## Customer

See [Quandoo Docs](https://docs.quandoo.com/quandoo-terminology/)

Customers (Guests) are not able to be created explcitly with Quandoo's current API implementation, new Customers are created when creating a new Reservation, if the Customer does not exist (referenced by email) a new Customer will be created.

## Reservation

See [Quandoo Docs](https://docs.quandoo.com/quandoo-terminology/)

#### Cancel

Takes nothing:

```python
reservation.cancel()
```
Returns nothing:
```commandline

```

#### Reconfirm

Takes nothing:

```python
reservation.reconfirm()
```
Returns nothing:
```commandline

```

#### Change Capacity

Takes the new capacity:

```python
new_capacity = 2
reservation.change_capacity(new_capacity)
```
Returns nothing:
```commandline

```

## NewReservation

Similar to Reservation, it is what is returned on Reservation creation.

#### Get Full Reservation

Takes nothing:

```python
customer = agent.get_customer(customer_id)
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

new_reservation = merchant.create_reservation(customer, capacity, res_datetime)
new_reservation.get_reservation()
```
Returns a [Reservation](#reservation) object:
```commandline
Reservation(
	id: 5da65435-3654-4627-8526-f544d4b9abef,
	status: AUTOMATIC_CONFIRMED,
	date: Mon 1 July 2019,
	startTime: 12:00 PM,
	endTime: 3:00 PM,
	capacity: 2,
	merchantId: 49295,
	customerId: fa78b27a-e050-4c7e-83c1-1e14e1506fda
)
```

## ReservationEnquiry

See [Quandoo Docs](https://docs.quandoo.com/quandoo-terminology/)

#### Get messages
Takes nothing

## NewReservationEnquiry

Similar to ReservationEnquiry, it is what is returned on ReservationEnquiry creation.

#### Get Full ReservationEnquiry

Takes nothing:

```python
customer = agent.get_customer(customer_id)
capacity = 2
start_qdt, end_qdt = QuandooDatetime(year, month, day, 12), QuandooDatetime(year, month, day, 14)

new_res_enq = merchant.create_reservation_enquiry(customer, capacity, start_qdt, end_qdt, "Looking for a table please!")
new_res_enq.get_reservation_enquiry()
```
Returns a [ReservationEnquiry](#reservationenquiry) object:
```commandline
ReservationEnquiry(
	id: e0d87523-46ac-4159-b146-8119f567b58f,
	merchantId: 33226,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254,
	capacity: 2,
	startTime: 2019-09-01T02:00+10:00[Australia/Sydney],
	endTime: 2019-09-01T04:00+10:00[Australia/Sydney],
	status: NEW
)
``` 

## QuandooDatetime

A datetime class with extra functionality useful to Quandoo, ie a time resolution of 15 minutes

#### Get specfic time

Takes usual [datetime](https://docs.quandoo.com/quandoo-terminology/) paramters, but has a time resolution of 15 minutes

```python
QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
```

Returns a [QuandooDatetimeObject](#quandoodatetime)

```commandline
QuandooDatetime(
	datetime: 2019-07-01 12:00:00+10:00,
	q_datetime: 2019-07-01T12:00:00+10:00,
	pretty_date: 12:00 PM, Mon 1 July 2019
)
```

#### Get current time

Static. Takes nothing:

```python
QuandooDatetime.now()
```

Returns a [QuandooDatetimeObject](#quandoodatetime)

```commandline
QuandooDatetime(
	datetime: 2019-06-03 22:45:00+10:00,
	q_datetime: 2019-06-03T22:45:00+10:00,
	pretty_date: 10:45 PM, Mon 3 June 2019
)
```

#### Parse time returned by Quandoo API

Static. Takes a string:

```python
QuandooDatetime.parse_str_qdt("2019-07-01T12:00:00+10:00")
```

Returns a [QuandooDatetimeObject](#quandoodatetime)

```commandline
QuandooDatetime(
	datetime: 2019-07-01 12:00:00+10:00,
	q_datetime: 2019-07-01T12:00:00+10:00,
	pretty_date: 12:00 PM, Mon 1 July 2019
)
```

#### Get Quandoo formatted datetime string

Takes nothing:

```python
qdt = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
qdt.get_qdt()
```

Returns a Quandoo formatted datetime string

```commandline
2019-07-01T12:00:00+10:00
```

#### Get formatted datetime string that reads well

Takes nothing:

```python
qdt = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
qdt.pretty_date()
```

Returns a formatted datetime string that reads well

```commandline
12:00 PM, Mon 1 July 2019
```
