"""Unit tests for Module 01: Automation at Scale with Config Management."""

import unittest
from course_5_configuration_management_and_cloud.modules.module_01_automation_at_scale.practice import (
    example_function,
)


class TestModule01(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
