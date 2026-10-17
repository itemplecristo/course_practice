"""Unit tests for Module 03: Loops & Iterations."""

import unittest
from course_1_python_crash_course.modules.module_03_loops.practice import example_function


class TestModule03(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
