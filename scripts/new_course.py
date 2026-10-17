#!/usr/bin/env python3
"""Scaffold a new course directory with module subfolders, tests, and documentation.

Supports the Google IT Automation with Python certificate syllabus (Courses 1-6)
as well as custom courses.

Usage:
    python scripts/new_course.py                      # Interactive mode
    python scripts/new_course.py <course_number>      # CLI mode with syllabus defaults
    python scripts/new_course.py <course_number> <course_slug> --modules <all|N|list>

Examples:
    python scripts/new_course.py 3
    python scripts/new_course.py 3 --modules all
    python scripts/new_course.py 3 --modules 1,2
    python scripts/new_course.py 4 troubleshooting_and_debugging --modules all
    python scripts/new_course.py 7 custom_automation_course --modules 3
"""

import argparse
import re
import sys
from pathlib import Path

# Google IT Automation with Python Certificate Syllabus Presets
SYLLABUS = {
    1: {
        "slug": "python_crash_course",
        "title": "Course 1: Python Crash Course",
        "modules": [
            {"num": "01", "slug": "basics", "title": "Basics & Core Syntax"},
            {
                "num": "02",
                "slug": "data_structures",
                "title": "Data Structures & Collections",
            },
            {"num": "03", "slug": "loops", "title": "Loops & Iterations"},
            {
                "num": "04",
                "slug": "strings_lists_dictionaries",
                "title": "Strings, Lists & Dictionaries",
            },
            {
                "num": "05",
                "slug": "object_oriented_programming",
                "title": "Object-Oriented Programming",
            },
            {
                "num": "06",
                "slug": "final_project",
                "title": "Writing a Script from the Ground Up",
            },
        ],
    },
    2: {
        "slug": "python_with_operating_system",
        "title": "Course 2: Using Python to Interact with the Operating System",
        "modules": [
            {
                "num": "01",
                "slug": "getting_started_with_python",
                "title": "Getting Started with Python & OS",
            },
            {"num": "02", "slug": "managing_files", "title": "Managing Files & CSVs"},
            {
                "num": "03",
                "slug": "regular_expressions",
                "title": "Regular Expressions",
            },
            {
                "num": "04",
                "slug": "managing_data_and_processes",
                "title": "Managing Data & Processes",
            },
            {"num": "05", "slug": "testing_in_python", "title": "Testing in Python"},
            {
                "num": "06",
                "slug": "bash_scripting",
                "title": "Bash Scripting & Pipelines",
            },
            {
                "num": "07",
                "slug": "final_project",
                "title": "Working with Log Files & Reporting",
            },
        ],
    },
    3: {
        "slug": "git_and_github",
        "title": "Course 3: Introduction to Git and GitHub",
        "modules": [
            {
                "num": "01",
                "slug": "intro_to_version_control",
                "title": "Introduction to Version Control",
            },
            {
                "num": "02",
                "slug": "using_git_locally",
                "title": "Using Git Locally, Diffs & Branching",
            },
            {
                "num": "03",
                "slug": "working_with_remotes",
                "title": "Working with Remotes & GitHub",
            },
            {
                "num": "04",
                "slug": "collaboration",
                "title": "Collaboration, Pull Requests & Rebasing",
            },
        ],
    },
    4: {
        "slug": "troubleshooting_and_debugging",
        "title": "Course 4: Troubleshooting and Debugging Techniques",
        "modules": [
            {
                "num": "01",
                "slug": "troubleshooting_concepts",
                "title": "Troubleshooting Concepts & Problem-Solving",
            },
            {
                "num": "02",
                "slug": "slowness",
                "title": "Slowness, Profiling & Concurrency",
            },
            {
                "num": "03",
                "slug": "crashing_programs",
                "title": "Crashing Programs, Core Dumps & Memory",
            },
            {
                "num": "04",
                "slug": "managing_resources",
                "title": "Managing System Resources & Bottlenecks",
            },
        ],
    },
    5: {
        "slug": "configuration_management_and_cloud",
        "title": "Course 5: Configuration Management and the Cloud",
        "modules": [
            {
                "num": "01",
                "slug": "automation_at_scale",
                "title": "Automation at Scale with Config Management",
            },
            {
                "num": "02",
                "slug": "deploying_puppet",
                "title": "Deploying Puppet, Manifests & Rules",
            },
            {
                "num": "03",
                "slug": "automation_in_the_cloud",
                "title": "Cloud Concepts, VMs & Automation",
            },
            {
                "num": "04",
                "slug": "managing_cloud_instances",
                "title": "Managing Cloud Instances & Scalability",
            },
        ],
    },
    6: {
        "slug": "automating_real_world_tasks",
        "title": "Course 6: Automating Real-World Tasks with Python",
        "modules": [
            {
                "num": "01",
                "slug": "manipulating_images",
                "title": "Manipulating Images with PIL / Pillow",
            },
            {
                "num": "02",
                "slug": "web_services",
                "title": "Interacting with Web Services & REST APIs",
            },
            {
                "num": "03",
                "slug": "automatic_emailing",
                "title": "Automating Email Delivery & PDF Generation",
            },
            {
                "num": "04",
                "slug": "final_project",
                "title": "Automating a Complete Pipeline from Data to Report",
            },
        ],
    },
}

MODULE_PRACTICE_TEMPLATE = '''"""Module {module_num}: {title}
Course practice implementation and solutions.
"""


def example_function():
    """Sample starting function for Module {module_num}."""
    return True
'''

MODULE_MANUAL_TEMPLATE = '''"""Module {module_num}: {title} (Manual Practice / Scratchpad)
Run directly: python {course_folder}/modules/module_{module_num}_{slug}/practice_manually.py
"""

print("--> Module {module_num}: {title} manual experiments")
'''

MODULE_NOTES_TEMPLATE = """# Module {module_num}: {title}

## 📖 Overview
Key concepts, course lecture notes, and practical takeaways for {title}.

## 🔑 Key Concepts
- Concept 1: Description
- Concept 2: Description

## 💡 Cheatsheet & Patterns
```python
# Code snippets and syntax patterns
```

## 📝 Practice Tasks
- [ ] **Exercise 1**: Description
- [ ] **Exercise 2**: Description
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

COURSE_README_TEMPLATE = """# {course_title}

Google IT Automation with Python Professional Certificate practice repository.

## Modules

| Module | Topic | Practice | Scratchpad | Notes |
|:---:|:---|:---:|:---:|:---:|
{module_table_rows}

## Running Tests
```bash
# Run tests for this course only
pytest tests/{test_dir}
```
"""


def get_root_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def get_existing_courses(root_dir: Path) -> dict[int, Path]:
    courses = {}
    for p in root_dir.glob("course_*"):
        if p.is_dir():
            match = re.match(r"^course_(\d+)_(.*)$", p.name)
            if match:
                course_num = int(match.group(1))
                courses[course_num] = p
    return courses


def scaffold_module(
    root_dir: Path,
    course_folder: str,
    test_dir: str,
    mod_num: str,
    mod_slug: str,
    mod_title: str,
) -> None:
    num_str = mod_num.zfill(2)
    mod_dir = root_dir / course_folder / "modules" / f"module_{num_str}_{mod_slug}"
    test_file = root_dir / "tests" / test_dir / f"test_module_{num_str}.py"

    mod_dir.mkdir(parents=True, exist_ok=True)
    (mod_dir / "__init__.py").touch()

    practice_file = mod_dir / "practice.py"
    if not practice_file.exists():
        practice_file.write_text(
            MODULE_PRACTICE_TEMPLATE.format(module_num=num_str, title=mod_title)
        )

    manual_file = mod_dir / "practice_manually.py"
    if not manual_file.exists():
        manual_file.write_text(
            MODULE_MANUAL_TEMPLATE.format(
                module_num=num_str,
                title=mod_title,
                slug=mod_slug,
                course_folder=course_folder,
            )
        )

    notes_file = mod_dir / "notes.md"
    if not notes_file.exists():
        notes_file.write_text(
            MODULE_NOTES_TEMPLATE.format(module_num=num_str, title=mod_title)
        )

    if not test_file.exists():
        test_file.write_text(
            TEST_TEMPLATE.format(
                module_num=num_str,
                title=mod_title,
                slug=mod_slug,
                course_folder=course_folder,
            )
        )


def create_course(
    course_num: int,
    course_slug: str | None = None,
    course_title: str | None = None,
    selected_modules: list[dict] | None = None,
) -> Path:
    root_dir = get_root_dir()

    # Determine slug & title
    if course_num in SYLLABUS:
        default_slug = SYLLABUS[course_num]["slug"]
        default_title = SYLLABUS[course_num]["title"]
    else:
        default_slug = f"course_{course_num}"
        default_title = f"Course {course_num}"

    slug = course_slug or default_slug
    slug = slug.lower().replace("-", "_").replace(" ", "_")
    title = course_title or default_title
    course_folder_name = f"course_{course_num}_{slug}"
    test_sub_dir = f"course_{course_num}"

    course_path = root_dir / course_folder_name
    modules_path = course_path / "modules"
    data_path = course_path / "data"
    test_path = root_dir / "tests" / test_sub_dir

    # Create directories
    modules_path.mkdir(parents=True, exist_ok=True)
    data_path.mkdir(parents=True, exist_ok=True)
    test_path.mkdir(parents=True, exist_ok=True)

    # Package init files
    (course_path / "__init__.py").touch()
    (modules_path / "__init__.py").touch()
    (data_path / ".gitkeep").touch()
    (root_dir / "tests" / "__init__.py").touch()
    (test_path / "__init__.py").touch()

    # Modules to create
    modules_to_create = selected_modules or []
    table_rows = []

    for mod in modules_to_create:
        mod_num = str(mod["num"]).zfill(2)
        m_slug = mod["slug"]
        m_title = mod["title"]
        scaffold_module(
            root_dir=root_dir,
            course_folder=course_folder_name,
            test_dir=test_sub_dir,
            mod_num=mod_num,
            mod_slug=m_slug,
            mod_title=m_title,
        )
        table_rows.append(
            f"| `{mod_num}` | **{m_title}** | [practice.py](modules/module_{mod_num}_{m_slug}/practice.py) | [practice_manually.py](modules/module_{mod_num}_{m_slug}/practice_manually.py) | [notes.md](modules/module_{mod_num}_{m_slug}/notes.md) |"
        )

    # Course README
    readme_file = course_path / "README.md"
    if not readme_file.exists():
        table_content = (
            "\n".join(table_rows)
            if table_rows
            else "| - | No modules created yet | - | - | - |"
        )
        readme_file.write_text(
            COURSE_README_TEMPLATE.format(
                course_title=title,
                module_table_rows=table_content,
                test_dir=test_sub_dir,
            )
        )

    return course_path


def interactive_mode():
    root_dir = get_root_dir()
    existing = get_existing_courses(root_dir)

    print("\n=======================================================")
    print(" 🎓 Google IT Automation with Python - Course Creator  ")
    print("=======================================================\n")
    print("Available Certificate Courses:")
    for num in range(1, 7):
        preset = SYLLABUS[num]
        status = " (✅ Already Created)" if num in existing else ""
        print(f"  [{num}] {preset['title']}{status}")
    print("  [C] Custom Course (provide your own name)\n")

    while True:
        choice = input("Enter course number (1-6) or 'C' for custom: ").strip().lower()
        if choice in ["c", "custom"]:
            while True:
                num_input = input("Enter custom course number (e.g. 7): ").strip()
                if num_input.isdigit():
                    course_num = int(num_input)
                    break
                print("Please enter a valid integer.")
            course_slug = input(
                "Enter course name slug (e.g. advanced_python): "
            ).strip()
            course_title = input(
                f"Enter course display title [Course {course_num}: {course_slug}]: "
            ).strip()
            if not course_title:
                course_title = (
                    f"Course {course_num}: {course_slug.replace('_', ' ').title()}"
                )
            syllabus_modules = []
            break
        elif choice.isdigit() and int(choice) in SYLLABUS:
            course_num = int(choice)
            preset = SYLLABUS[course_num]
            course_slug = preset["slug"]
            course_title = preset["title"]
            syllabus_modules = preset["modules"]
            if course_num in existing:
                print(
                    f"\n⚠️  Note: {course_title} directory already exists at {existing[course_num].name}."
                )
                confirm = (
                    input("Do you want to add/ensure modules in this course? [y/N]: ")
                    .strip()
                    .lower()
                )
                if confirm not in ["y", "yes"]:
                    print("Aborted.")
                    sys.exit(0)
            break
        else:
            print("Invalid selection, please try again.")

    # Modules selection
    selected_modules = []
    if syllabus_modules:
        print(f"\nSyllabus modules for {course_title}:")
        for idx, m in enumerate(syllabus_modules, start=1):
            print(f"  {m['num']}: {m['title']} ({m['slug']})")

        print("\nModule generation options:")
        print("  [A] All syllabus modules")
        print(
            "  [1-N] Comma-separated module numbers or count (e.g. '1,2' or '2' for first 2)"
        )
        print("  [N] None (empty modules folder)")
        mod_choice = input("Choose option [A]: ").strip().lower() or "a"

        if mod_choice in ["a", "all"]:
            selected_modules = syllabus_modules
        elif mod_choice in ["n", "none", "0"]:
            selected_modules = []
        elif (
            mod_choice.isdigit()
            and int(mod_choice) <= len(syllabus_modules)
            and int(mod_choice) > 0
        ):
            # First N modules
            count = int(mod_choice)
            selected_modules = syllabus_modules[:count]
        else:
            # Comma-separated list of numbers
            parts = [p.strip() for p in mod_choice.split(",") if p.strip()]
            for p in parts:
                p_num = p.zfill(2)
                found = next((m for m in syllabus_modules if m["num"] == p_num), None)
                if found:
                    selected_modules.append(found)
    else:
        # Custom course module count prompt
        mod_count_str = (
            input("\nHow many module subfolders to create initially? [0]: ").strip()
            or "0"
        )
        if mod_count_str.isdigit() and int(mod_count_str) > 0:
            count = int(mod_count_str)
            for i in range(1, count + 1):
                num_str = str(i).zfill(2)
                mod_name = input(
                    f"Name for module {num_str} (leave blank for 'module_{num_str}'): "
                ).strip()
                m_slug = (
                    mod_name.lower().replace("-", "_").replace(" ", "_")
                    if mod_name
                    else f"module_{num_str}"
                )
                m_title = (
                    mod_name.replace("_", " ").title()
                    if mod_name
                    else f"Module {num_str}"
                )
                selected_modules.append(
                    {"num": num_str, "slug": m_slug, "title": m_title}
                )

    print(f"\nScaffolding {course_title}...")
    course_path = create_course(
        course_num=course_num,
        course_slug=course_slug,
        course_title=course_title,
        selected_modules=selected_modules,
    )

    print(f"✨ Successfully created {course_path.name}!")
    print(f"  - Course Directory: {course_path.relative_to(root_dir)}/")
    print(f"  - Modules Directory: {course_path.relative_to(root_dir)}/modules/")
    print(f"  - Data Directory: {course_path.relative_to(root_dir)}/data/")
    print(f"  - Test Suite: tests/course_{course_num}/")
    if selected_modules:
        print(f"  - Created {len(selected_modules)} modules:")
        for m in selected_modules:
            print(f"      • module_{m['num']}_{m['slug']}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scaffold a new course directory with modules, tests, and documentation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python scripts/new_course.py                    # Interactive wizard
  python scripts/new_course.py 3                  # Course 3 with interactive module picker
  python scripts/new_course.py 3 --modules all    # Course 3 with all syllabus modules
  python scripts/new_course.py 3 --modules 1,2    # Course 3 with modules 01 and 02
  python scripts/new_course.py 4 --modules all    # Course 4 with all modules
  python scripts/new_course.py 7 my_custom_course --modules 2
""",
    )
    parser.add_argument(
        "course_num", nargs="?", type=str, help="Course number (e.g. 3, 4, 5, 6)"
    )
    parser.add_argument(
        "course_slug", nargs="?", type=str, help="Optional custom course slug"
    )
    parser.add_argument(
        "--modules",
        type=str,
        default=None,
        help="Modules to generate: 'all', count (e.g. '2'), or comma-separated list (e.g. '1,2')",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.course_num:
        interactive_mode()
        return

    clean_num = (
        args.course_num.lower()
        .replace("course_", "")
        .replace("course", "")
        .replace("c", "")
    )
    if not clean_num.isdigit():
        print(f"Error: Invalid course number '{args.course_num}'. Must be an integer.")
        sys.exit(1)

    course_num = int(clean_num)
    course_slug = args.course_slug

    syllabus_modules = SYLLABUS.get(course_num, {}).get("modules", [])
    selected_modules = []

    if args.modules:
        mod_arg = args.modules.strip().lower()
        if mod_arg in ["all", "a"]:
            selected_modules = syllabus_modules
        elif mod_arg in ["none", "0"]:
            selected_modules = []
        elif (
            mod_arg.isdigit()
            and syllabus_modules
            and int(mod_arg) <= len(syllabus_modules)
        ):
            selected_modules = syllabus_modules[: int(mod_arg)]
        elif syllabus_modules:
            parts = [p.strip().zfill(2) for p in mod_arg.split(",") if p.strip()]
            for p in parts:
                found = next((m for m in syllabus_modules if m["num"] == p), None)
                if found:
                    selected_modules.append(found)
        elif mod_arg.isdigit():
            count = int(mod_arg)
            for i in range(1, count + 1):
                num_str = str(i).zfill(2)
                selected_modules.append(
                    {
                        "num": num_str,
                        "slug": f"module_{num_str}",
                        "title": f"Module {num_str}",
                    }
                )
    else:
        # Default when run non-interactively without --modules flag: all syllabus modules if preset, else none
        selected_modules = syllabus_modules

    course_title = None
    if course_num in SYLLABUS:
        course_title = SYLLABUS[course_num]["title"]
        if not course_slug:
            course_slug = SYLLABUS[course_num]["slug"]

    root_dir = get_root_dir()
    course_path = create_course(
        course_num=course_num,
        course_slug=course_slug,
        course_title=course_title,
        selected_modules=selected_modules,
    )

    print(f"✨ Successfully created {course_path.name}!")
    print(f"  - Course Directory: {course_path.relative_to(root_dir)}/")
    print(f"  - Modules Directory: {course_path.relative_to(root_dir)}/modules/")
    print(f"  - Data Directory: {course_path.relative_to(root_dir)}/data/")
    print(f"  - Test Suite: tests/course_{course_num}/")
    if selected_modules:
        print(f"  - Created {len(selected_modules)} modules:")
        for m in selected_modules:
            print(f"      • module_{m['num']}_{m['slug']}")


if __name__ == "__main__":
    main()
