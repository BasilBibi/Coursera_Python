import unittest
from coursera_python.module2.Ex_7_1 import uppercase_file_contents


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


class Ex_7_1_tests(unittest.TestCase):

    def test_uppercase_whole_file(self):
        words = get_file_path('words.txt')
        self.assertEqual("WRITING PROGRAMS", uppercase_file_contents(words)[0:16])


if __name__ == '__main__':
    unittest.main()
