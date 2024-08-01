import os
import sys
sys.path.append("../..")
import unittest
from unittest import TestCase
import shutil
from unittest import TestCase

# NB: avoid relative imports when you will write your code:
from dal.sales_api import get_sales


class GetSalesTestCase(TestCase):
    """
    Test sales_api.get_sales function.
    """
    def test_get_sales(self):
        response = get_sales("2023-18-12")
        self.assertEqual(response[0]['data'], '')
        self.assertEqual(response[1], 403)

if __name__ == '__main__':
    unittest.main()   