import unittest
from unittest.mock import MagicMock
from coursera_python.module3.SocketGETExample import get_url_using_bs4, crawl_hrefs


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


def make_mock_socket_with_recv_values(s):
    sock = MagicMock()
    sock.recv.side_effect = [s, b'']
    # if you don't need to control multiple calls on a
    # mock method you can also mock with a return value
    # e.g. sock.connect.return_value = None
    return sock


class Week3SocketTests(unittest.TestCase):

    def test_comments_42(self):
        comments_42 = get_file_contents('comments_42.html')
        url = 'http://py4e-data.dr-chuck.net/comments_42.html'

        ulib = MagicMock()
        ulib.request.urlopen(url).read.side_effect = [comments_42]
        self.assertEqual(2553, get_url_using_bs4( ulib, url ) )

    def test_comments_85870(self):
        comments_85870 = get_file_contents('comments_85870.html')
        url = 'http://py4e-data.dr-chuck.net/comments_85870.html'

        ulib = MagicMock()
        ulib.request.urlopen(url).read.side_effect = [comments_85870]
        self.assertEqual(2063, get_url_using_bs4( ulib, url ) )

    @unittest.skip("Skipped because this test hits an external web service")
    def test_crawl_fikret(self):
        url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
        r = 4
        p = 3
        self.assertEqual("Anayah", crawl_hrefs( url, r, p ))

    @unittest.skip("Skipped because this test hits an external web service")
    def test_crawl_Rybecca(self):
        url = 'http://py4e-data.dr-chuck.net/known_by_Rybecca.html'
        r = 7
        p = 18
        self.assertEqual("Lotta", crawl_hrefs( url, r, p ))

if __name__ == '__main__':
    unittest.main()
