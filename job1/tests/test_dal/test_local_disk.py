import os
import sys
sys.path.append("../..")
import unittest
from unittest import TestCase
import shutil

from dal.local_disk import save_to_disk


class SaveToDiskTestCase(TestCase):
    """
    Test dal.local_disk.save_to_disk function.
    """

    def test_save_to_disk(self):

        json_content = [{"data": "for testing"}, {0: 1}]
        test_path = "data/test_data"

        save_to_disk(json_content=json_content, path=test_path)
        self.assertEqual(os.listdir("data"), ["test_data.json"])

        shutil.rmtree('data')


if __name__ == '__main__':
    unittest.main()  
