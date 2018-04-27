import unittest
from coursera_python.module2.Ex_8_5 import count_from_lines


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Ex_8_4_tests(unittest.TestCase):

    def test_get_from_line_count(self):
        mbox_short_file = get_file_path('mbox-short.txt')
        self.assertEqual(27, count_from_lines(mbox_short_file))


if __name__ == '__main__':
    unittest.main()
