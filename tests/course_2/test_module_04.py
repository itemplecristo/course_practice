"""Unit tests for Module 04: Managing Data & Processes."""

import unittest
from course_2_python_with_operating_system.modules.module_04_managing_data_and_processes.practice import example_function


class TestModule04(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
