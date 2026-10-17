"""Unit tests for Module 07: Working with Log Files & Reporting."""

import unittest
from course_2_python_with_operating_system.modules.module_07_final_project.practice import example_function


class TestModule07(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
