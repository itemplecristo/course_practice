"""Unit tests for Module 04: Managing Cloud Instances & Scalability."""

import unittest
from course_5_configuration_management_and_cloud.modules.module_04_managing_cloud_instances.practice import (
    example_function,
)


class TestModule04(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
