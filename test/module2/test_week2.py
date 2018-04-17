import unittest
from coursera_python.module2.week2_assignment1 import uppercase_file_contents
from coursera_python.module2.week2_assignment2 import calc_avg_spam_confidence


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Week2Tests (unittest.TestCase):

    def test_uppercase_whole_file(self):
        words = get_file_path('words.txt')
        self.assertEqual("WRITING PROGRAMS", uppercase_file_contents(words)[0:16])

    def test_spam_confidence(self):
        mbox_short = get_file_path('mbox-short.txt')
        self.assertEqual(0.7507185185185187, calc_avg_spam_confidence(mbox_short))


if __name__ == '__main__':
    unittest.main()