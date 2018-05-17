import unittest
from coursera_python.module3.week1_regex_assignment import sum_numbers_in_file, one_liner
from test.TestBase import *


class Week1RegexTests (unittest.TestCase):

    def test_regex_sum_42(self):
        regex_sum_42 = get_file_path('module3/resources/regex_sum_42.txt')
        self.assertEqual(445833, sum_numbers_in_file(regex_sum_42) )

    def test_regex_sum_85868(self):
        regex_sum_85868 = get_file_path('module3/resources/regex_sum_85868.txt')
        self.assertEqual(421784, sum_numbers_in_file(regex_sum_85868) )

    def test_regex_sum_85868_one_liner(self):
        regex_sum_85868 = get_file_path('module3/resources/regex_sum_85868.txt')
        self.assertEqual(421784, one_liner(regex_sum_85868) )


if __name__ == '__main__':
    unittest.main()
