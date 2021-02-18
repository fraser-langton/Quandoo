import unittest

from quandoo import Agent, Merchant, Customer
from .conftest import AUTH_TOKEN, AGENT_ID, MERCHANT_ID, CUSTOMER_ID


class TestAgent(unittest.TestCase):
    agent = Agent(AUTH_TOKEN, AGENT_ID, test=True)

    def test_get_merchant(self):
        merchant = self.agent.get_merchant(MERCHANT_ID)
        self.assertIsInstance(merchant, Merchant)
        return merchant

    def test_get_customer(self):
        customer = self.agent.get_customer(CUSTOMER_ID)
        self.assertIsInstance(customer, Customer)
        return customer

    def test_get_reservation(self):
        pass

    def test_get_reservation_enquiry(self):
        pass

    def test_merchants(self):
        pass

