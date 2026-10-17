"""Unit tests for Module 06: Writing a Script from the Ground Up."""

import unittest
from course_1_python_crash_course.modules.module_06_final_project.practice import example_function


class TestModule06(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
