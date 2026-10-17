import unittest
from course_2_python_with_operating_system.modules.module_02_managing_files.practice import (
    word_frequencies,
    two_sum,
    read_csv_employees,
)


class TestModule02(unittest.TestCase):
    def test_word_frequencies(self):
        counts = word_frequencies("Hello world! Hello python.")
        self.assertEqual(counts["hello"], 2)
        self.assertEqual(counts["world"], 1)
        self.assertEqual(counts["python"], 1)

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))
        self.assertEqual(two_sum([3, 3], 6), (0, 1))
        self.assertIsNone(two_sum([1, 2, 3], 10))

    def test_read_csv_employees(self):
        records = read_csv_employees()
        self.assertEqual(len(records), 4)
        self.assertEqual(records[0]["name"], "Sabrina Green")
        self.assertEqual(records[0]["phone"], "802-867-5309")
        self.assertEqual(records[0]["role"], "System Administrator")
        self.assertEqual(records[1]["name"], "Eli Jones")
        self.assertEqual(records[2]["name"], "Melody Daniels")
        self.assertEqual(records[3]["name"], "Charlie Rivera")


if __name__ == "__main__":
    unittest.main()
