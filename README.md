# Google IT Automation with Python

A structured repository for hands-on Python exercises, course modules, manual experiments, datasets, and automated testing with pytest for the **Google IT Automation with Python Professional Certificate**. Configured natively for **Antigravity IDE**.

---

## Project Structure

```text
course_practice/
├── .agents/                                       # Antigravity IDE Customizations
│   └── rules/                                     # Workspace rules & standards
│       └── workspace-rules.md
├── .vscode/                                       # IDE settings (Python interpreter, pytest, black)
│   └── settings.json
├── course_1_python_crash_course/                  # Course 1: Python Crash Course
│   └── modules/
│       └── module_01_basics/
│           ├── practice.py
│           ├── practice_manually.py
│           └── notes.md
├── course_2_python_with_operating_system/         # Course 2: Python with Operating System
│   ├── data/                                      # Sample CSV & text datasets
│   │   ├── by_department.csv
│   │   ├── csv_file.txt
│   │   ├── flowers.csv
│   │   ├── hosts.csv
│   │   └── software.csv
│   └── modules/
│       ├── module_02_managing_files/
│       │   ├── practice.py
│       │   ├── practice_manually.py
│       │   ├── practice_manually_formatted.py
│       │   ├── notes.md
│       │   ├── csv_file.txt
│       │   └── employees.csv
│       └── module_03_regular_expressions/
│           ├── practice.py
│           ├── practice_manually.py
│           └── notes.md
├── course_3_git_and_github/                       # Course 3: Introduction to Git and GitHub
│   ├── data/
│   └── modules/
│       ├── module_01_intro_to_version_control/
│       ├── module_02_using_git_locally/
│       ├── module_03_working_with_remotes/
│       └── module_04_collaboration/
├── course_5_configuration_management_and_cloud/   # Course 5: Configuration Management and the Cloud
│   ├── data/
│   └── modules/
│       ├── module_01_automation_at_scale/
│       ├── module_02_deploying_puppet/
│       ├── module_03_automation_in_the_cloud/
│       └── module_04_managing_cloud_instances/
├── tests/                                         # Automated unit tests (pytest / unittest)
│   ├── course_1/
│   │   └── test_module_01.py
│   ├── course_2/
│   │   ├── test_module_02.py
│   │   └── test_module_03.py
│   ├── course_3/
│   │   ├── test_module_01.py
│   │   ├── test_module_02.py
│   │   ├── test_module_03.py
│   │   └── test_module_04.py
│   └── course_5/
│       ├── test_module_01.py
│       ├── test_module_02.py
│       ├── test_module_03.py
│       └── test_module_04.py
├── scripts/                                       # Helper and automation scripts
│   ├── setup_venv.sh                              # Virtual environment setup script
│   ├── new_course.py                              # Scaffold a whole course with modules & tests
│   └── new_module.py                              # Scaffold a single module + test suite
├── requirements.txt                               # Python development dependencies
└── README.md
```

---

## Quickstart

### 1. Set Up Virtual Environment
Run the setup script:
```bash
./scripts/setup_venv.sh
```

Or activate manually:
```bash
source .venv/bin/activate
```

### 2. Run Tests
Run all tests across all courses:
```bash
pytest
```

Run tests for a specific course:
```bash
pytest tests/course_1
pytest tests/course_2
```

With coverage report:
```bash
pytest --cov=course_1_python_crash_course --cov=course_2_python_with_operating_system
```

### 3. Create a New Course (with Module Subfolders)
Scaffold an entire certificate course directory, including modules, tests, datasets, and README:
```bash
# Interactive mode (prompts with the Google IT Automation syllabus)
python scripts/new_course.py

# CLI mode with all syllabus modules for Course 3 (Git & GitHub)
python scripts/new_course.py 3 --modules all

# Create Course 4 with first 2 modules
python scripts/new_course.py 4 --modules 2

# Create Course 5 with specific modules
python scripts/new_course.py 5 --modules 1,2
```

### 4. Create an Individual Module
Scaffold an additional module directory with practice templates and a test suite under any course:
```bash
# Add module to Course 1
python scripts/new_module.py 1 03 loops_and_functions

# Add module to Course 2
python scripts/new_module.py 2 01 os_basics
```

### 5. Code Formatting
Format all files according to PEP 8:
```bash
black .
```
