# Module 01: Python Basics & Core Syntax

## 📖 Overview
This module covers fundamental Python syntax and basic control flow used in course problem solving.

## 🔑 Key Concepts
- **Data Types**: `int`, `float`, `str`, `bool`, `NoneType`
- **Control Flow**: `if`, `elif`, `else`
- **Loops**: `for ... in ...`, `while`, `break`, `continue`
- **Functions**: `def`, parameters, default values, return types

## 💡 Cheatsheet & Patterns
```python
# String formatting (f-strings)
name = "Python"
version = 3.11
print(f"Learning {name} version {version}")

# List comprehension with filtering
evens = [x for x in range(10) if x % 2 == 0]

# Safe type casting & validation
val = int("42") if "42".isdigit() else 0
```

## 📝 Practice Tasks
- [x] **Exercise 1**: FizzBuzz implementation ([practice.py](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/modules/module_01_basics/practice.py))
- [x] **Exercise 2**: Prime number checker ([practice.py](file:///home/itemplecristo/.gemini/antigravity/scratch/course_practice/modules/module_01_basics/practice.py))
