import unittest
from strings_calculator import StringsCalculator


class TestStringCalculator(unittest.TestCase):
    """
    Unit tests for the StringCalculator class.
    """

    def setUp(self):
        self.calculator = StringsCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)
        self.assertEqual(self.calculator.add("   "), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)
        self.assertEqual(self.calculator.add("10"), 10)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
        self.assertEqual(self.calculator.add("10,20"), 30)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)
        self.assertEqual(self.calculator.add("10,20,30,40"), 100)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("10\n20,30"), 60)

    def test_different_delimiters(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)
        self.assertEqual(self.calculator.add("//|\n10|20|30"), 60)
        self.assertEqual(self.calculator.add("//-\n10-20-30"), 60)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n1;-2;3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2,-3")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n-1;-2;3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -1,-2")


if __name__ == "__main__":
    unittest.main()