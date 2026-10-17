"""Tests for Module 03: Regular Expressions"""

import unittest
from course_2_python_with_operating_system.modules.module_03_regular_expressions import (
    practice,
)


class TestModule03(unittest.TestCase):
    def test_module_exists(self):
        self.assertIsNotNone(practice)


if __name__ == "__main__":
    unittest.main()
