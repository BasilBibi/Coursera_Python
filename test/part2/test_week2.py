import unittest
from coursera_python.module2.week2_assignment1 import print_file_contents
from coursera_python.module2.week2_assignment2 import calc_avg_spam_confidence


def get_file_handle(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class week2_tests (unittest.TestCase):

    def test_uppercase_wole_file(self):
        words = get_file_handle('words.txt')
        print_file_contents( words )

    def test_spam_confidence(self):
        mbox_short = get_file_handle('mbox-short.txt')
        self.assertEqual(0.7507185185185187, calc_avg_spam_confidence(mbox_short))


if __name__ == '__main__':
    unittest.main()