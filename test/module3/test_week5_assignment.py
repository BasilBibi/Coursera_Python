import unittest
from unittest.mock import MagicMock
from coursera_python.module3.week5_xml_assignment import crawl_xml

from test.TestBase import *


class XmlWebcrawlTests(unittest.TestCase):

    def test_comments_42_xml(self):
        comments_42_xml_contents = get_file_contents('module3/resources/comments_42.xml')
        url = 'NONSENSE'

        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_42_xml_contents]

        self.assertEqual(2553, crawl_xml(url_lib_mock, url))

    def test_comments_85872_xml(self):
        comments_85872_xml_contents = get_file_contents('module3/resources/comments_85872.xml')
        url = 'NONSENSE'

        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_85872_xml_contents]

        self.assertEqual(2214, crawl_xml(url_lib_mock, url))


if __name__ == '__main__':
    unittest.main()
