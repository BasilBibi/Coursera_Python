import unittest
from coursera_python.module2.Ex_6_5 import extract_end_float


class Ex_6_5_tests(unittest.TestCase):

    def test_shouldExtractEndDataAsFloat(self):
        text = "X-DSPAM-Confidence:    0.8475"
        self.assertEqual(0.8475, extract_end_float(text))


if __name__ == '__main__':
    unittest.main()