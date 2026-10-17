"""Unit tests for Module 04: Strings, Lists & Dictionaries."""

import unittest
from course_1_python_crash_course.modules.module_04_strings_lists_dictionaries.practice import example_function


class TestModule04(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
