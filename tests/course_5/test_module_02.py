"""Unit tests for Module 02: Deploying Puppet, Manifests & Rules."""

import unittest
from course_5_configuration_management_and_cloud.modules.module_02_deploying_puppet.practice import (
    example_function,
)


class TestModule02(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
