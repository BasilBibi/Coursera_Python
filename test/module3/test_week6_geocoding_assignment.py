import unittest
from unittest.mock import MagicMock
from coursera_python.module3.week6_geocoding_assignment import fetch_place_id

import urllib.request, urllib.parse, urllib.error

from test.TestBase import *


def make_mock(url):
    geocoding_data = get_file_contents('module3/geocoding_data.json').encode()
    url_lib_mock = MagicMock()
    url_lib_mock.parse.urlencode.side_effect = ['address=university+of+padua']
    full_url = url + 'address=university+of+padua'
    url_lib_mock.request.urlopen(full_url).read.side_effect = [geocoding_data]
    return url_lib_mock


class JsonParsingTests(unittest.TestCase):

    @unittest.skip("Hits the internet")
    def test_get_South_Federal_University_place_id(self):
        url = 'http://py4e-data.dr-chuck.net/geojson?'
        address = 'South Federal University'
        self.assertEqual('ChIJJ8oO7_B_bIcR2AlhC8nKlok', fetch_place_id(urllib, url, address))

    @unittest.skip("Hits the internet")
    def test_get_university_of_padua_place_id(self):
        url = 'http://py4e-data.dr-chuck.net/geojson?'
        address = 'university of padua'
        self.assertEqual('ChIJw5bZ88zd3IARk1MQ1I3DEN4', fetch_place_id(urllib, url, address))

    def test_get_university_of_padua_place_id_mocked(self):
        url = 'http://py4e-data.dr-chuck.net/geojson?'
        address = 'university of padua'
        url_lib_mock = make_mock(url)
        self.assertEqual('ChIJw5bZ88zd3IARk1MQ1I3DEN4', fetch_place_id(url_lib_mock, url, address))


if __name__ == '__main__':
    unittest.main()
