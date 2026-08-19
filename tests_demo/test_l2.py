import unittest
import pandas as pd

from csv_cleaner import calculate_days_difference

class TestBookFunctions(unittest.TestCase):
    def test_calculate_days_difference(self):
        row = pd.Series({
            'Book Returned': pd.Timestamp('2026-08-15'),
            'Book checkout': pd.Timestamp('2026-08-01')
        })

        result = calculate_days_difference(row)

        self.assertEqual(result, 14)

    def test_book_is_on_time(self):
        days_borrowed = 14

        result = 'Overdue' if days_borrowed > 14 else 'On time'

        self.assertEqual(result, 'On time')

    def test_book_is_overdue(self):
        days_borrowed = 15

        result = 'Overdue' if days_borrowed > 14 else 'On time'

        self.assertEqual(result, 'Overdue')

if __name__ == '__main__':
    unittest.main()