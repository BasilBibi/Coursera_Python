import unittest
from coursera_python.module2.Ex_7_2 import calc_avg_spam_confidence


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Ex_7_2_tests(unittest.TestCase):

    def test_spam_confidence(self):
        mbox_short = get_file_path('mbox-short.txt')
        self.assertEqual(0.7507185185185187, calc_avg_spam_confidence(mbox_short))


if __name__ == '__main__':
    unittest.main()
