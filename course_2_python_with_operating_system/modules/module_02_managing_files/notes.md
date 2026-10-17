# Module 02: Managing Files & CSVs

## 📖 Overview
Focuses on reading and writing files, working with CSV datasets, and Python's primary collections (`list`, `dict`, `set`, `tuple`) and high-performance container datatypes from the `collections` module.

## 🔑 Key Concepts
- **File Management & CSVs**: Reading lines, `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`.
- **List (`list`)**: Ordered, mutable sequence with $O(1)$ append/pop from end, $O(n)$ search.
- **Dictionary (`dict`)**: Hash map key-value store with average $O(1)$ lookup, insertion, and deletion.
- **Set (`set`)**: Unordered collection of unique items. Great for membership checks and deduplication ($O(1)$ average).
- **Tuple (`tuple`)**: Immutable sequence, useful for fixed records, multi-value returns, and dictionary keys.
- **Collections Module**:
  - `Counter`: Tallying element counts easily.
  - `defaultdict`: Dictionary that auto-creates missing keys with a default factory.
  - `deque`: Double-ended queue with $O(1)$ append/pop on both left and right sides.

## 💡 Cheatsheet & Patterns
```python
from collections import Counter, defaultdict

# 1. Frequency counting
words = ["python", "code", "python", "task"]
freq = Counter(words)  # {'python': 2, 'code': 1, 'task': 1}

# 2. Grouping with defaultdict
grouped = defaultdict(list)
grouped["even"].append(2)

# 3. Fast lookup & deduplication with sets
unique_ids = set([1, 2, 2, 3])  # {1, 2, 3}
if 2 in unique_ids:
    print("Found in O(1) time")

# 4. Reading CSV files
import csv

with open("csv_file.txt", "r", encoding="utf-8") as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        name, phone, role = row
        print(f"Name: {name}, Phone: {phone}, Role: {role}")
```

## 📝 Practice Tasks
- [x] **Exercise 1**: [`word_frequencies`](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/course_2_python_with_operating_system/modules/module_02_managing_files/practice.py#L11) (Text analysis & word frequency map)
- [x] **Exercise 2**: [`two_sum`](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/course_2_python_with_operating_system/modules/module_02_managing_files/practice.py#L20) (Target sum indices using a dictionary hash map)
- [x] **Exercise 3**: [`read_csv_employees`](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/course_2_python_with_operating_system/modules/module_02_managing_files/practice.py#L33) (Parsing CSV records with `csv.reader` from [csv_file.txt](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/course_2_python_with_operating_system/modules/module_02_managing_files/csv_file.txt))

