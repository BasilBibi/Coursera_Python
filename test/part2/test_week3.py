import unittest
from coursera_python.module2.week3_assignment import get_sorted_unique_word_list, count_from_lines


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Week3Tests (unittest.TestCase):

    def test_get_unique_words(self):
        expected = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair',
                    'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what',
                    'window', 'with', 'yonder']
        romeo_file = get_file_path('romeo.txt')
        self.assertEqual(expected, get_sorted_unique_word_list(romeo_file))

    def test_get_from_line_count(self):
        mbox_short_file = get_file_path('mbox-short.txt')
        self.assertEqual(27, count_from_lines(mbox_short_file))


if __name__ == '__main__':
    unittest.main()