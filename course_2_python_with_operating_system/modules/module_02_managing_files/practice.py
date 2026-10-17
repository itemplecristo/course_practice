"""
Module 02: Managing Files & CSVs - Practice Tasks
"""

import csv
from pathlib import Path
import re
from collections import Counter


def word_frequencies(text: str) -> dict[str, int]:
    """
    Count word occurrences in text (case-insensitive, basic punctuation stripped).
    """
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    words = cleaned.split()
    return dict(Counter(words))


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Find indices of two numbers that add up to target.
    Returns (index1, index2) or None if no pair exists.
    """
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None


def read_csv_employees(file_path: str | Path | None = None) -> list[dict[str, str]]:
    """
    Reads the employee CSV file and returns a list of dictionaries with name, phone, and role.
    Demonstrates the csv.reader pattern.
    """
    if file_path is None:
        file_path = Path(__file__).parent / "csv_file.txt"

    records = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            if not row:
                continue
            name, phone, role = row
            print(f"Name: {name}, Phone: {phone}, Role: {role}")
            records.append(
                {"name": name.strip(), "phone": phone.strip(), "role": role.strip()}
            )
    return records


if __name__ == "__main__":
    sample_text = "Python is great, and Python practice is essential!"
    print("--- Word frequencies ---")
    print(word_frequencies(sample_text))

    nums = [2, 7, 11, 15]
    target = 9
    print(f"\n--- Two sum for {nums} target {target} ---")
    print(two_sum(nums, target))

    print("\n--- Reading CSV Employees ---")
    read_csv_employees()
