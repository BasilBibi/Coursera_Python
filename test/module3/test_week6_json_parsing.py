import unittest
import json

from test.TestBase import *


class JsonParsingExamples(unittest.TestCase):

    def test_length_results_list(self):
        geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
        j = json.loads(geocoding_data)
        self.assertEqual(20, len( j['results'] ))

    def test_number_of_attribs_in_address(self):
        geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
        j = json.loads(geocoding_data)
        addresses = j['results']
        addr = addresses[0]
        self.assertEqual(6, len(addr.keys()) )

    def test_number_of_attribs_in_address_components(self):
        geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
        j = json.loads(geocoding_data)
        addresses = j['results']
        addr = addresses[0]
        addr_comp = addr['address_components']
        self.assertEqual(7, len(addr_comp) )

    def test_number_of_attribs_in_address_components(self):
        geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
        j = json.loads(geocoding_data)
        addresses = j['results']
        addr = addresses[0]
        addr_comps = addr['address_components']
        for address_component in addr_comps:
            long_name = address_component['long_name']
            print(long_name)

    def test_formatted_address(self):
        geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
        j = json.loads(geocoding_data)
        addresses = j['results']
        for address in addresses:
            print(address['formatted_address'])


if __name__ == '__main__':
    unittest.main()
