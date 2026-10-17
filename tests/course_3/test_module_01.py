"""Unit tests for Module 01: Introduction to Version Control."""

import unittest
from course_3_git_and_github.modules.module_01_intro_to_version_control.practice import example_function


class TestModule01(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
