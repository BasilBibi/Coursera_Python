import unittest
from coursera_python.module2.Ex_8_5 import count_from_lines
from test.TestBase import *


class Ex_8_4_tests(unittest.TestCase):

    def test_get_from_line_count(self):
        mbox_short_file = get_file_path('module2/mbox-short.txt')
        self.assertEqual(27, count_from_lines(mbox_short_file))


if __name__ == '__main__':
    unittest.main()
