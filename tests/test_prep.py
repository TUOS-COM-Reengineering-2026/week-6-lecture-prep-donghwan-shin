import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    def test_strange_function2(self):
        self.assertEqual(
            first=strange_function(2, 1, 1, 4),
            second='behaviour 5'
        )

    # TODO: Can you write more test cases below to increase the test coverage of `strange_function`?