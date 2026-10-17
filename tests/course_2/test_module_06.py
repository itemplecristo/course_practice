"""Unit tests for Module 06: Bash Scripting & Pipelines."""

import unittest
from course_2_python_with_operating_system.modules.module_06_bash_scripting.practice import example_function


class TestModule06(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
