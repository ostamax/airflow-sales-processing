"""
Tests json_to_avro_converter.py module.
"""
import os
import json
import shutil
import unittest
from unittest import TestCase
import sys
sys.path.append("../..")

from dal.json_to_avro_converter import convert_and_save

class JsonToAvroTestCase(TestCase):

    def test_json_to_avro_converter(self):
        json_content = [{"client": "Maksym", "purchase_date": "2023-12-18", "product": "something", "price": 8}]

        test_json_path = "data/json_data/1.json"
        test_avro_path = "data/avro_data/"

        os.makedirs(os.path.dirname(test_json_path), exist_ok=True)
        with open(test_json_path, 'w') as json_file:
            json.dump(json_content, json_file,
                            indent=4,
                            separators=(',',': '))
        
        convert_and_save(raw_dir="data/json_data", stg_dir=test_avro_path)

        self.assertEqual(os.listdir(test_avro_path), ["1.avro"])
        shutil.rmtree('data')
if __name__ == '__main__':
    unittest.main()  

