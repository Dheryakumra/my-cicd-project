
import unittest

from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtract(9, 4), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
