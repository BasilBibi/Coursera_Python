import unittest
import json

from test.TestBase import *


def get_json_dict_from_file(file_path):
    geocoding_data = get_file_contents(file_path).encode()
    j = json.loads(geocoding_data)
    return j


class JsonParsingExamples(unittest.TestCase):

    def test_length_results_list(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        addresses = json_dict['results']
        self.assertEqual(20, len(addresses))

    def test_number_of_attribs_in_address(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        addresses = json_dict['results']
        address = addresses[0]
        self.assertEqual(6, len(address.keys()))

    def test_number_of_attribs_in_address_components(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        addresses = json_dict['results']
        address = addresses[0]
        address_components = address['address_components']
        self.assertEqual(7, len(address_components))

    def test_number_of_long_names_in_address_component(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        addresses = json_dict['results']
        address = addresses[0]
        address_components = address['address_components']
        expected_long_names = ['Padua', 'Westpark', 'Irvine', 'Orange County', 'California', 'United States', '92614']
        actual_long_names = [ac['long_name'] for ac in address_components]
        self.assertEqual(expected_long_names,  actual_long_names)

    def test_formatted_address(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        addresses = json_dict['results']
        address = addresses[0]
        self.assertEqual( 'Padua, Irvine, CA 92614, USA', address['formatted_address'])

    def test_deep_attrib_fetch(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')
        nw_bounds_lat = json_dict['results'][0]['geometry']['bounds']['northeast']['lat']
        self.assertEqual( 33.678201, nw_bounds_lat)

    def test_iterate_deep_attrib_fetch(self):
        json_dict = get_json_dict_from_file('module3/resources/geocoding_data.json')

        def fetch_location_lat_lng(index):
            location = json_dict['results'][index]['geometry']['location']
            return ( location['lat'], location['lng'] )

        location_lat_lngs = [ fetch_location_lat_lng(i) for i in range(0, len(json_dict['results'])) ]

        self.assertEqual( 20, len(location_lat_lngs) )


if __name__ == '__main__':
    unittest.main()
