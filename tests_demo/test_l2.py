import unittest
from calculator import calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = calculator(8,2)
        answer = calculation.get_sum()
        self.assertEqual(answer, 10, "The sum is wrong!")

    def test_minus(self):
        calculation = calculator(8,2)
        answer = calculation.get_minus()
        self.assertEqual(answer, 6, "The sum is wrong!")

    def test_multiple(self):
        calculation = calculator(8,2)
        answer = calculation.get_multiple()
        self.assertEqual(answer, 16, "The sum is wrong!")

    def test_division(self):
        calculation = calculator(8,2)
        answer = calculation.get_division()
        self.assertEqual(answer, 4, "The sum is wrong!")

if __name__ == "__main__":
    unittest.main()