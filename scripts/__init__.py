"""
Scripts module for managing contributions.

This module contains scripts for:

- Initializing new contributions (`init.py`)
- Validating contribution metadata (`validate_contributions.py`)
- Creating README files for contributions (`create_readme.py`)
- Creating metadata files for contributions (`create_metadatas.py`)
"""
# test 99

from .utils  import write_pyproject_file, read_pyproject_metadata, pyproject_file_exists, readme_exists, create_readme, init_py_exists, create_init_py, main_py_exists, create_main_py, create_tests_directory, test_file_exists, create_test_file


