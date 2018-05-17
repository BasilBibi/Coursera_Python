import unittest
from coursera_python.module2.Ex_7_1 import uppercase_file_contents
from test.TestBase import *


class Ex_7_1_tests(unittest.TestCase):

    def test_uppercase_whole_file(self):
        words = get_file_path('module2/resources/words.txt')
        self.assertEqual("WRITING PROGRAMS", uppercase_file_contents(words)[0:16])


if __name__ == '__main__':
    unittest.main()
