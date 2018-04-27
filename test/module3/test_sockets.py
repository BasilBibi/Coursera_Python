import unittest
from unittest.mock import MagicMock
from coursera_python.module3.SocketGETExample import get_url, UrlUtils


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

    @unittest.skip("Skipped because this test hits an external web service")
    def test_get_file(self):
        intro_short = strip_cr_lf( get_file_contents('intro-short.txt'))
        self.assertEqual(intro_short, get_url('data.pr4e.org', 80, 'http://data.pr4e.org/intro-short.txt'))

    def test_get_file_mocked(self):
        intro_short = strip_cr_lf( get_file_contents('intro-short.txt'))
        intro_short_encoded = intro_short.encode()
        socket = make_mock_socket_with_recv_values(intro_short_encoded)

        c = UrlUtils(socket)

        url = 'http://data.pr4e.org/intro-short.txt'
        self.assertEqual(intro_short, c.get_url('data.pr4e.org', 80, url) )

        socket.connect.assert_called_with( ('data.pr4e.org', 80) )
        socket.shutdown.assert_called()
        socket.close.assert_called()

        get = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        socket.send.assert_called_once_with( get.encode() )

    def test_get_file_failed_connect(self):
        with self.assertRaises(Exception) as context:
            socket = make_mock_socket_with_recv_values("")
            socket.connect.side_effect = Exception('Could Not Connect!')
            c = UrlUtils(socket)
            c.get_url('data.pr4e.org', 80, 'http://data.pr4e.org/intro-short.txt')
            self.assertTrue('Could Not Connect!' in context.exception)


if __name__ == '__main__':
    unittest.main()
