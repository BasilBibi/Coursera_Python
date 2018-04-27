import unittest
from unittest.mock import MagicMock
from coursera_python.module3.week5_xml_assignment import crawl_xml


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def get_file_contents(fn):
    f = get_file_path(fn)
    fh = open(f)
    data = fh.read()
    fh.close()
    return data


def strip_cr_lf(s): return s.replace("\n", "").replace("\r", "")


class Week3SocketTests(unittest.TestCase):

    def test_comments_42_xml(self):
        comments_42_xml_contents = get_file_contents('comments_42.xml')
        url = 'NONSENSE'

        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_42_xml_contents]

        self.assertEqual(2553, crawl_xml(url_lib_mock, url))

    def test_comments_85872_xml(self):
        comments_85872_xml_contents = get_file_contents('comments_85872.xml')
        url = 'NONSENSE'

        url_lib_mock = MagicMock()
        url_lib_mock.request.urlopen(url).read.side_effect = [comments_85872_xml_contents]

        self.assertEqual(2214, crawl_xml(url_lib_mock, url))


if __name__ == '__main__':
    unittest.main()
