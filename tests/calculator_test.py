from unittest import TestCase, main

import calculator


class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10, 15), 25)


if __name__ == '__main__':
    main()