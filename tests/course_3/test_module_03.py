"""Unit tests for Module 03: Working with Remotes & GitHub."""

import unittest
from course_3_git_and_github.modules.module_03_working_with_remotes.practice import example_function


class TestModule03(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
