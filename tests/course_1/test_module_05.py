"""Unit tests for Module 05: Object-Oriented Programming."""

import unittest
from course_1_python_crash_course.modules.module_05_object_oriented_programming.practice import example_function


class TestModule05(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
