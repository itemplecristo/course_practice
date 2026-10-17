"""Unit tests for Module 01: Getting Started with Python & OS."""

import unittest
from course_2_python_with_operating_system.modules.module_01_getting_started_with_python.practice import example_function


class TestModule01(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
