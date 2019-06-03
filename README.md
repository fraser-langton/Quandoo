# Quandoo for Python

This is a fairly lightwieght SDK for interacting with the Quandoo API, it is a work in progress.


## Installation

Install using pip :
```sh
$ pip install Quandoo
```

## Include Quandoo in your application
```python
import quandoo
```

## Get API Key + Agent ID

These are obtained directly from a Quandoo representative. [Quandoo docs on authentication.](https://docs.quandoo.com/specs/documentation/authentication.html)

```python
oauth_token = "<oauth_token>"
agent_id = "<agent_id>"
```

## Get Quandoo Agent instance

To get an [Agent](#agent) instance to Quandoo just provide the X-Quandoo-AuthToken and your Agent ID. 


```python
agent = quandoo.Agent(oauth_token, agent_id)
```

To get a test [Agent](#agent) instance be sure to use your test credentials

```python
agent_test = quandoo.Agent(oauth_token_test, agent_id_test, test=True)
```

# Usage

## Agent

[Quandoo Docs](https://docs.quandoo.com/specs/domain/agent.html): *"For Quandoo to attribute reservations correctly, we implement something called agent id (aid) tracking. This will be issued to you at the same time as you receive your Auth token. On urls to the portal or widget the aid is set on the given url automatically (based on the authtoken) and is stored for the duration of the browsing session only. When a reservation is made, the aid will be passed and stored with the reservation. With direct API reservations, agent_id must be specified in the request body."*

#### Get Merchant

Takes a Merchant ID:

```python
merchant = agent.get_merchant("123456")
print(merchant)
```
Returns a [Merchant](#merchant) object:
```commandline
Merchant(
	id: 123456,
	name: The Best Restaurant
)
```

#### Get Customer

Takes a Customer ID:

```python
customer = agent.get_customer("0bd07451-0c0e-40e9-8429-8a589f59e254")
print(customer)
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
reservation = agent.get_reservation("77f9dd33-9b24-4a66-a58c-7a059cecba5f")
print(reservation)
```
Returns a [Reservation](#reservation) object:
```commandline
Reservation(
	id: 77f9dd33-9b24-4a66-a58c-7a059cecba5f,
	status: AUTOMATIC_CONFIRMED,
	startTime: 2019-07-01T12:00:00+10:00,
	endTime: 2019-07-01T13:30:00+10:00,
	capacity: 2,
	merchantId: 123456,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
)
```

## Merchant

[Quandoo Docs](https://docs.quandoo.com/specs/domain/merchant.html): *"Internally this is how we refer to our partner restaurants. Every merchant has an ID or merchant ID assigned to them."*

#### Get Customers

Takes nothing:

```python
merchant = agent.get_merchant(merchant_id)

customers = merchant.get_customers()
print(customers)
```
Returns a list of [Customer](#customer) objects:
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

Takes nothing

```python
reservations = merchant.get_reservations()
print(reservations)
```

Returns a list of [Reservation](#reservation) objects:

```commandline
[
	Reservation(
		id: f140dcb3-a318-400c-9767-6a6bd93c5e69,
		status: AUTOMATIC_CONFIRMED,
		startTime: 2019-06-01T10:00:00+10:00,
		endTime: 2019-06-01T11:30:00+10:00,
		capacity: 4,
		merchantId: 123456,
		customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
	), 
	Reservation(
		id: 886021e2-5202-42a4-aaba-c6c83c520600,
		status: AUTOMATIC_CONFIRMED,
		startTime: 2019-06-01T12:00:00+10:00,
		endTime: 2019-06-01T13:30:00+10:00,
		capacity: 2,
		merchantId: 123456,
		customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
	)]
```

#### Get Available Times

Takes a capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime)

```python
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

avail_times = merchant.get_available_times(capacity, res_datetime)
print(avail_times)
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

Takes a capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime)

```python
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

avail_times = merchant.is_available(capacity, res_datetime)
print(avail_times)
```

Returns a boolean

```commandline
True
```

#### Create Reservation

Takes a [Customer](#customer) and capacity for the reservation as well as the [QuandooDatetime](#quandoodatetime)

```python
customer = agent.get_customer(customer_id)
capacity = 2
res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)

new_res = merchant.create_reservation(customer, capacity, res_datetime)
print(new_res)
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

## Customer

[Quandoo Docs](https://docs.quandoo.com/specs/domain/guest.html) (referred to as "Guests"): *"These are the people attending the reservation."*

Customers (Guests) are not able to be created explcitly with Quandoo's current API implementation, new Customers are created when creating a new Reservation, if the Customer does not exist (indexed by email) a new Customer will be created.

## Reservation

[Quandoo Docs](https://docs.quandoo.com/specs/domain/reservation.html): *"A reservation ‘belongs’ to both a merchant and a guest. Reservations can go through multiple states. The current functionality of the API only allows creation."*

#### Cancel

Takes nothing:

```python
reservation_id = "f140dcb3-a318-400c-9767-6a6bd93c5e69"

reservation = agent.get_reservation(reservation_id)
reservation.cancel()
```
Returns nothing:
```commandline

```

#### Reconfirm

Takes nothing:

```python
reservation_id = "f140dcb3-a318-400c-9767-6a6bd93c5e69"

reservation = agent.get_reservation(reservation_id)
reservation.reconfirm()
```
Returns nothing:
```commandline

```


#### Change Capacity

Takes the new capacity:

```python
reservation_id = "f140dcb3-a318-400c-9767-6a6bd93c5e69"
new_capacity = 2

reservation = agent.get_reservation(reservation_id)
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
new_reservation_full = new_reservation.get_reservation()
print(new_reservation_full)
```
Returns a [Reservation](#reservation) object:
```commandline
Reservation(
	id: a1584003-bb70-451c-aa52-0ad58454faf8,
	status: AUTOMATIC_CONFIRMED,
	startTime: 2019-06-01T12:00:00+10:00,
	endTime: 2019-06-01T13:30:00+10:00,
	capacity: 2,
	merchantId: 123456,
	customerId: 0bd07451-0c0e-40e9-8429-8a589f59e254
)
```

## QuandooDatetime

A datetime class with extra functionality useful to Quandoo, ie a time resolution of 15 minutes

#### Get specfic time

Takes usual [datetime](https://docs.python.org/3/library/datetime.html) paramters, but has a time resolution of 15 minutes

```python
qdt = res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
print(qdt)
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

Takes nothing:

```python
qdt = QuandooDatetime.now()
print(qdt)
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

Takes a string:

```python
qdt = QuandooDatetime.parse_str_qdt("2019-07-01T12:00:00+10:00")
print(qdt)
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
qdt = res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
print(qdt.get_qdt())
```

Returns a Quandoo formatted datetime string

```commandline
2019-07-01T12:00:00+10:00
```

#### Get formatted datetime string that reads well

Takes nothing:

```python
qdt = res_datetime = QuandooDatetime(year=2019, month=7, day=1, hour=12, minute=0)
print(qdt.pretty_date())
```

Returns a formatted datetime string that reads well

```commandline
12:00 PM, Mon 1 July 2019
```
