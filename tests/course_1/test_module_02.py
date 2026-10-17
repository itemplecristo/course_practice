"""Unit tests for Module 02: Data Structures & Collections."""

import unittest
from course_1_python_crash_course.modules.module_02_data_structures.practice import example_function


class TestModule02(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
