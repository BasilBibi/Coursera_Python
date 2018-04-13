import unittest
from coursera_python.module2.week6_assignment_10_2 import get_hr_histo


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Week6Tests (unittest.TestCase):

    def test_get_hr_histo(self):
        mbox_short_file = get_file_path('mbox-short.txt')
        expected = [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6),
                    ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]
        self.assertEqual(expected, get_hr_histo(mbox_short_file))


if __name__ == '__main__':
    unittest.main()
