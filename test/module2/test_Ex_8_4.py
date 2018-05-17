import unittest
from coursera_python.module2.Ex_8_4 import get_sorted_unique_word_list
from test.TestBase import *


class Ex_8_4_tests(unittest.TestCase):

    def test_get_unique_words(self):
        expected = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair',
                    'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what',
                    'window', 'with', 'yonder']
        romeo_file = get_file_path('module2/resources/romeo.txt')
        self.assertEqual(expected, get_sorted_unique_word_list(romeo_file))


if __name__ == '__main__':
    unittest.main()
