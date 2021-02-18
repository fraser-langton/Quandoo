import unittest

from quandoo import status_test


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(status_test(), 200)
