---
description: Python course practice guidelines and standards for Google IT Automation with Python
always_on: true
---

# Google IT Automation with Python - Practice Standards

## Environment & Python Configuration
- **Python Version**: Python 3.11+
- **Virtual Environment**: `.venv` located at project root (`/home/itemplecristo/.gemini/antigravity/scratch/course_practice/.venv`)
- **Interpreter Path**: Always execute scripts and tests using `.venv/bin/python` or `.venv/bin/pytest`.
- **Dependencies**: Managed via `requirements.txt` (`pytest`, `pytest-cov`, `black`, `flake8`).

## Directory Organization
- `course_<number>_<course_name>/`: Contains course learning materials separated by certificate course.
  - `modules/module_<XX>_<topic>/`: Sequential modules (e.g. `module_01_basics`, `module_02_data_structures`, `module_03_regular_expressions`).
    - `practice.py`: Pure functions, solutions, and implementations.
    - `practice_manually.py`: Scratchpad and manual experiments.
    - `notes.md`: Key concepts, cheat sheets, and explanation notes.
  - `data/`: Course-specific datasets (`.csv`, `.txt`).
- `tests/course_<number>/`: Automated unit tests matching each module (`test_module_01.py`, `test_module_02.py`, etc.).
- `scripts/`: Project maintenance tools (`setup_venv.sh`, `new_module.py`).

## Coding & Testing Conventions
- Use descriptive function and variable names with snake_case.
- Format all code with Black (`black .`).
- Ensure all tests pass with `pytest`.
- Keep exercises modular and importable for test coverage.
