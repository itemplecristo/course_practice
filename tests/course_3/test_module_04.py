"""Unit tests for Module 04: Collaboration, Pull Requests & Rebasing."""

import unittest
from course_3_git_and_github.modules.module_04_collaboration.practice import example_function


class TestModule04(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
