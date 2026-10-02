import unittest
from modules.module_01_basics.practice import fizz_buzz, is_prime


class TestModule01(unittest.TestCase):
    def test_fizz_buzz(self):
        output = fizz_buzz(15)
        self.assertEqual(output[0], "1")
        self.assertEqual(output[2], "Fizz")
        self.assertEqual(output[4], "Buzz")
        self.assertEqual(output[14], "FizzBuzz")

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))


if __name__ == "__main__":
    unittest.main()
