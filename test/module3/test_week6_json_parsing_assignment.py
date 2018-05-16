import unittest
from unittest.mock import MagicMock
from coursera_python.module3.week6_json_assignment import crawl_comments_json

from test.TestBase import *


class JsonParsingTests(unittest.TestCase):

    def test_comments_42_json(self):
        comments_42_contents = get_file_contents('module3/comments_42.json')
        url = 'NONSENSE'
        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_42_contents]
        self.assertEqual(2553, crawl_comments_json(url_lib_mock, url))

    def test_comments_85873_json(self):
        comments_85873_contents = get_file_contents('module3/comments_85873.json')
        url = 'NONSENSE'
        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_85873_contents]
        self.assertEqual(2850, crawl_comments_json(url_lib_mock, url))


if __name__ == '__main__':
    unittest.main()
