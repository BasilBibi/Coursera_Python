import unittest
from unittest.mock import MagicMock
from coursera_python.module3.SocketGETExample import get_url, UrlUtils
from test.TestBase import *


class Week3SocketTests(unittest.TestCase):

    @unittest.skip("Skipped because this test hits an external web service")
    def test_get_file(self):
        intro_short = strip_cr_lf( get_file_contents('module3/resources/intro-short.txt'))
        self.assertEqual(intro_short, get_url('data.pr4e.org', 80, 'http://data.pr4e.org/intro-short.txt'))

    def test_get_file_mocked(self):
        intro_short = strip_cr_lf( get_file_contents('module3/resources/intro-short.txt'))
        result = intro_short.encode()

        socket = MagicMock()
        socket.recv.side_effect = [result, b'']

        c = UrlUtils(socket)

        url = 'http://data.pr4e.org/intro-short.txt'
        actual = c.get_url('data.pr4e.org', 80, url)
        self.assertEqual(intro_short, actual)

        # Expectations
        socket.connect.assert_called_with( ('data.pr4e.org', 80) )
        socket.shutdown.assert_called()
        socket.close.assert_called()

        get = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        socket.send.assert_called_once_with( get.encode() )

    def test_get_file_failed_connect(self):
        with self.assertRaises(Exception) as context:

            socket = MagicMock()
            socket.connect.side_effect = Exception('Could Not Connect!')

            c = UrlUtils(socket)
            c.get_url('data.pr4e.org', 80, 'http://data.pr4e.org/intro-short.txt')
            self.assertTrue('Could Not Connect!' in context.exception)


if __name__ == '__main__':
    unittest.main()
