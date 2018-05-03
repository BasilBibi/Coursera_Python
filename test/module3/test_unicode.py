import unittest


class Week4_UTF8Tests (unittest.TestCase):

    def test_print_machione_encodings(self):
        import sys
        print(sys.getdefaultencoding())
        print(sys.stdout.encoding)

    def test_size_of_hokke_character_as_bytes(self):
        s = 'abc𩸽z'
        s_as_UTF8_bytes = s.encode()
        print('s_as_bytes', type(s_as_UTF8_bytes))
        self.assertEqual(8, len(s_as_UTF8_bytes))

    def test_size_of_hokke_character_as_str(self):
        s = 'abc𩸽z'
        print('s', type(s))
        self.assertEqual(5, len(s))

    def test_encode_and_decode_of_hokke_character(self):
        s = 'abc𩸽z'
        s_as_UTF8_bytes = s.encode()

        decoded_str = s_as_UTF8_bytes.decode()
        print('decoded_str', type(decoded_str))

        self.assertEqual(8, len(s_as_UTF8_bytes))
        self.assertEqual(5, len(decoded_str))


if __name__ == '__main__':
    unittest.main()
