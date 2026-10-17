"""Unit tests for Module 05: Testing in Python."""

import unittest
from course_2_python_with_operating_system.modules.module_05_testing_in_python.practice import example_function


class TestModule05(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
