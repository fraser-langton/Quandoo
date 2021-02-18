import unittest

from quandoo.QuandooModel import QuandooDatetime


class TestMerchant(unittest.TestCase):
    def get_customers(self, offset=0, limit=100, modified_since: QuandooDatetime = None,
                      modified_until: QuandooDatetime = None):
        pass

    def get_available_times(self, pax: int, qdt: QuandooDatetime, duration=2, area_id=None):
        pass

    def is_available(self, pax: int, qdt: QuandooDatetime, duration=2, area_id=None):
        pass

    def get_reviews(self, offset=0, limit=10):
        pass

    def create_reservation(self, customer, pax: int, qdt: QuandooDatetime, area_id=None, order_id=None, extra_info=None,
                           reservation_tags=[]):
        pass

    def create_reservation_enquiry(self, customer, pax: int, start_qdt: QuandooDatetime, end_qdt: QuandooDatetime,
                                   message: str):
        pass

    def get_reservation_tags(self):
        pass

