import unittest
from coursera_python.module1.Ex_3_1 import compute_normalpay,compute_overtime,computepay


class Ex_3_1_tests(unittest.TestCase):

    def test_zero_overtime(self):
        self.assertEqual(0, compute_overtime(0, 10.5))

    def test_one_hour_overtime(self):
        self.assertEqual(15.75, compute_overtime(41, 10.5))

    def test_5_hours_overtime(self):
        self.assertEqual(78.75, compute_overtime(45, 10.5))

    def test_zero_normalpay(self):
        self.assertEqual(0, compute_normalpay(0, 10.5))

    def test_one_hour_normalpay(self):
        self.assertEqual(10.5, compute_normalpay(1, 10.5))

    def test_normalpay_with_5_hours_extra(self):
         self.assertEqual(420, compute_normalpay(45, 10.5))

    def test_45_hours_totalpay(self):
        self.assertEqual(498.75, computepay(45, 10.5))


if __name__ == '__main__':
    unittest.main()
