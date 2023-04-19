from unittest import TestCase, main

import calculator


class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10, 15), 25)

    def test_add_with_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator.add("10", 15)
        self.assertEqual("Expected two integers", e.exception.args[0])


if __name__ == '__main__':
    main()