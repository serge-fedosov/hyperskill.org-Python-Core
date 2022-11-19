# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(6), True)

    def test_when_output_false(self):
        self.assertNotEqual(is_even(1), True)
        self.assertNotEqual(is_even(3), True)


if __name__ == '__main__':
    unittest.main()
