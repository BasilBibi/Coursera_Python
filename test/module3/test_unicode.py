import unittest


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def get_file_contents(fn):
    f = get_file_path(fn)
    fh = open(f)
    data = fh.read().replace("\n", "").replace("\r", "")
    fh.close()
    return data


class Week4_UTF8Tests (unittest.TestCase):

    def test_print_machione_encodings(self):
        import sys
        print(sys.getdefaultencoding())
        print(sys.stdout.encoding)

    def test_size_of_hokke_character_as_bytes(self):
        s = '𩸽'
        s_as_UTF8_bytes = s.encode()
        print('s_as_bytes', type(s_as_UTF8_bytes))
        self.assertEqual(4, len(s_as_UTF8_bytes))

    def test_size_of_hokke_character_as_str(self):
        s = '𩸽'
        print('s', type(s))
        self.assertEqual(1, len(s))

    def test_encode_and_decode_of_hokke_character(self):
        s = '𩸽'
        s_as_UTF8_bytes = s.encode()

        decoded_str = s_as_UTF8_bytes.decode()
        print('decoded_str', type(decoded_str))

        self.assertEqual(4, len(s_as_UTF8_bytes))
        self.assertEqual(1, len(decoded_str))


if __name__ == '__main__':
    unittest.main()
