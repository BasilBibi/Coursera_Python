import unittest
from coursera_python.module2.week5_assignment import get_most_sender


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Week5Tests (unittest.TestCase):

    def test_get_from_line_count(self):
        mbox_short_file = get_file_path('mbox-short.txt')
        self.assertEqual("cwen@iupui.edu 5", get_most_sender(mbox_short_file))


if __name__ == '__main__':
    unittest.main()
