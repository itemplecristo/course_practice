#!/usr/bin/env python3
"""Scaffold a new course module with code templates and test suite.

Supports all Google IT Automation with Python certificate courses
as well as custom course directories.

Usage:
    python scripts/new_module.py <course_number> <module_number> <module_name>

Examples:
    python scripts/new_module.py 1 03 loops_and_functions
    python scripts/new_module.py 2 01 os_interaction
    python scripts/new_module.py 3 01 intro_to_vcs

To scaffold an entire new course with subfolders, use:
    python scripts/new_course.py
"""

import re
import sys
from pathlib import Path

DEFAULT_COURSES = {
    "1": {
        "folder": "course_1_python_crash_course",
        "title": "Course 1: Python Crash Course",
        "test_dir": "course_1",
    },
    "2": {
        "folder": "course_2_python_with_operating_system",
        "title": "Course 2: Python with Operating System",
        "test_dir": "course_2",
    },
    "3": {
        "folder": "course_3_git_and_github",
        "title": "Course 3: Introduction to Git and GitHub",
        "test_dir": "course_3",
    },
    "4": {
        "folder": "course_4_troubleshooting_and_debugging",
        "title": "Course 4: Troubleshooting and Debugging Techniques",
        "test_dir": "course_4",
    },
    "5": {
        "folder": "course_5_configuration_management_and_cloud",
        "title": "Course 5: Configuration Management and the Cloud",
        "test_dir": "course_5",
    },
    "6": {
        "folder": "course_6_automating_real_world_tasks",
        "title": "Course 6: Automating Real-World Tasks with Python",
        "test_dir": "course_6",
    },
}

MODULE_TEMPLATE = '''"""Module {module_num}: {title}
Course practice implementation and solutions.
"""


def example_function():
    """Sample starting function."""
    return True
'''

MANUAL_TEMPLATE = '''"""Module {module_num}: {title} (Manual Practice / Scratchpad)
Run directly: python {course_folder}/modules/module_{module_num}_{slug}/practice_manually.py
"""

print("--> Module {module_num}: {title} manual experiments")
'''

NOTES_TEMPLATE = """# Module {module_num}: {title}

## Overview
Key concepts and notes for {title}.

## Quick Reference
- Concept 1: ...
- Concept 2: ...

## Summary
- ...
"""

TEST_TEMPLATE = '''"""Unit tests for Module {module_num}: {title}."""

import unittest
from {course_folder}.modules.module_{module_num}_{slug}.practice import example_function


class TestModule{module_num}(unittest.TestCase):
    def test_example(self):
        self.assertTrue(example_function())


if __name__ == "__main__":
    unittest.main()
'''


def get_available_courses(root_dir: Path):
    courses = dict(DEFAULT_COURSES)
    for p in root_dir.glob("course_*"):
        if p.is_dir():
            match = re.match(r"^course_(\d+)_(.*)$", p.name)
            if match:
                c_num = match.group(1)
                c_slug = match.group(2)
                if c_num not in courses:
                    courses[c_num] = {
                        "folder": p.name,
                        "title": f"Course {c_num}: {c_slug.replace('_', ' ').title()}",
                        "test_dir": f"course_{c_num}",
                    }
                else:
                    courses[c_num]["folder"] = p.name
    return courses


def print_usage(root_dir: Path):
    courses = get_available_courses(root_dir)
    print(
        "Usage: python scripts/new_module.py <course_number> <module_number> <module_name>"
    )
    print("\nAvailable courses:")
    for key in sorted(courses.keys(), key=lambda x: int(x) if x.isdigit() else 999):
        c = courses[key]
        status = " [active on disk]" if (root_dir / c["folder"]).exists() else ""
        print(f"  {key}: {c['title']}{status}")
    print("\nExamples:")
    print("  python scripts/new_module.py 1 03 loops")
    print("  python scripts/new_module.py 2 01 os_basics")
    print("  python scripts/new_module.py 3 01 git_basics")
    print(
        "\nTip: To create an entire new course with subfolders, run: python scripts/new_course.py"
    )


def main():
    root_dir = Path(__file__).resolve().parent.parent

    if len(sys.argv) < 4:
        print_usage(root_dir)
        sys.exit(1)

    course_key = (
        sys.argv[1]
        .lower()
        .replace("course_", "")
        .replace("course", "")
        .replace("c", "")
    )
    courses = get_available_courses(root_dir)

    if course_key not in courses:
        print(f"Error: Unknown course '{sys.argv[1]}'.")
        print_usage(root_dir)
        sys.exit(1)

    course_info = courses[course_key]
    course_folder = course_info["folder"]
    test_sub_dir = course_info["test_dir"]

    num = sys.argv[2].zfill(2)
    name_slug = sys.argv[3].lower().replace("-", "_").replace(" ", "_")
    title = name_slug.replace("_", " ").title()

    module_dir = root_dir / course_folder / "modules" / f"module_{num}_{name_slug}"
    tests_dir = root_dir / "tests" / test_sub_dir

    module_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    # Ensure parent package __init__.py files
    (root_dir / course_folder / "__init__.py").touch()
    (root_dir / course_folder / "modules" / "__init__.py").touch()
    (root_dir / "tests" / "__init__.py").touch()
    (tests_dir / "__init__.py").touch()

    # 1. module __init__.py
    (module_dir / "__init__.py").touch()

    # 2. practice.py
    practice_file = module_dir / "practice.py"
    if not practice_file.exists():
        practice_file.write_text(MODULE_TEMPLATE.format(module_num=num, title=title))

    # 3. practice_manually.py
    manual_file = module_dir / "practice_manually.py"
    if not manual_file.exists():
        manual_file.write_text(
            MANUAL_TEMPLATE.format(
                module_num=num,
                title=title,
                slug=name_slug,
                course_folder=course_folder,
            )
        )

    # 4. notes.md
    notes_file = module_dir / "notes.md"
    if not notes_file.exists():
        notes_file.write_text(NOTES_TEMPLATE.format(module_num=num, title=title))

    # 5. test_module_XX.py
    test_file = tests_dir / f"test_module_{num}.py"
    if not test_file.exists():
        test_file.write_text(
            TEST_TEMPLATE.format(
                module_num=num,
                title=title,
                slug=name_slug,
                course_folder=course_folder,
            )
        )

    print(f"Created module_{num}_{name_slug} under {course_info['title']}:")
    print(f"  - {module_dir.relative_to(root_dir)}/practice.py")
    print(f"  - {module_dir.relative_to(root_dir)}/practice_manually.py")
    print(f"  - {module_dir.relative_to(root_dir)}/notes.md")
    print(f"  - {test_file.relative_to(root_dir)}")


if __name__ == "__main__":
    main()
