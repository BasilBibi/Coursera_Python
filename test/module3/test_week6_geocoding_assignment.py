import unittest
from coursera_python.module3.week6_geocoding_assignment import fetch_place_id


class JsonParsingTests(unittest.TestCase):

    @unittest.skip("Hits the internet")
    def test_get_South_Federal_University_place_id(self):
        url = 'http://py4e-data.dr-chuck.net/geojson?'
        address = 'South Federal University'
        self.assertEqual('ChIJJ8oO7_B_bIcR2AlhC8nKlok', fetch_place_id(url, address))

    @unittest.skip("Hits the internet")
    def test_get_university_of_padua_place_id(self):
        url = 'http://py4e-data.dr-chuck.net/geojson?'
        address = 'university of padua'
        self.assertEqual('ChIJw5bZ88zd3IARk1MQ1I3DEN4', fetch_place_id(url, address))


if __name__ == '__main__':
    unittest.main()
