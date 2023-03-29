import unittest
from app.calculator import calculate
from tools.testrunner import testrunner


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(3, calculate('+', 1, 2))

    def test_subtraction(self):
        self.assertEqual(1, calculate('-', 2, 1))

    def test_raises_an_exception_for_illegal_operator(self):
        with self.assertRaises(TypeError):
            calculate('x', 1, 2)


if __name__ == '__main__':
    testrunner.testrunner(TestCalculate)
