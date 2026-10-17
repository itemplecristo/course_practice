"""Unit tests for Module 02: Using Git Locally, Diffs & Branching."""

import unittest
from course_3_git_and_github.modules.module_02_using_git_locally.practice import example_function


class TestModule02(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
