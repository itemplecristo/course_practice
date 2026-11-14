"""Unit tests for Module 03: Cloud Concepts, VMs & Automation."""

import unittest
from course_5_configuration_management_and_cloud.modules.module_03_automation_in_the_cloud.practice import (
    example_function,
)


class TestModule03(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
