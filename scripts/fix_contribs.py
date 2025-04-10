"""
Module: fix_contribs

This module provides functionality to ensure that necessary files and directories 
exist for each contribution in a specified contributions directory. It automates 
the creation of essential files such as `pyproject.toml`, `README.md`, `__init__.py`, 
a main Python file, and test files for each subdirectory within the contributions 
directory. Additionally, it ensures the presence of a `tests` directory for each 
contribution.

Functions:
    - create_files_for_contribs: Ensures the existence of required files and directories 
      for each contribution subdirectory.

Usage:
    Run this script directly to automatically create or verify the required files 
    and directories for contributions in the specified `CONTRIB_DIR`.
"""

import os
from .utils import (
    list_subdirs,
    write_pyproject_file,
    pyproject_file_exists,
    readme_exists,
    create_readme,
    init_py_exists,
    create_init_py,
    main_py_exists,
    create_main_py,
    create_tests_directory,
    test_file_exists,
    create_test_file,
    conftest_file_exists,
    create_conftest_file,

)


CONTRIB_DIR = "./contrib"


def create_files_for_contribs() -> None:
    """
    Ensures that necessary files and directories exist for each contribution 
    in the specified contributions directory.

    This function performs the following tasks for each subdirectory in the 
    contributions directory:
    - Checks if a `pyproject.toml` file exists; if not, creates one.
    - Checks if a `README.md` file exists; if not, creates one.
    - Checks if an `__init__.py` file exists; if not, creates one.
    - Checks if a main Python file named after the subdirectory exists; if not, creates one.
    - Creates a `tests` directory if it does not already exist.
    - Checks if a test file named `test_<subdir>.py` exists in the `tests` directory; if not, creates one.

    If any of the above files or directories already exist, a message is printed 
    indicating their presence.

    Returns:
        None
    """

    if not os.path.exists(CONTRIB_DIR):
        print(f" The directory '{CONTRIB_DIR}' does not exist.")
        return

    for subdir in list_subdirs(CONTRIB_DIR):
        path = os.path.join(CONTRIB_DIR, subdir)

        # Create the tests directory if it doesn't exist
        create_tests_directory(contrib_path=path)

        # Define file-checking tasks and their corresponding creation functions
        tasks = [
            (pyproject_file_exists, write_pyproject_file, "pyproject.toml", {'contrib_path': path}),
            (readme_exists, create_readme, "README.md", {'contrib_path': path}),
            (init_py_exists, create_init_py, "__init__.py", {'contrib_path': path}),
            (main_py_exists, create_main_py, f"{subdir}.py", {'contrib_path': path, 'name': subdir}),
            (test_file_exists, create_test_file, f"test_{subdir}.py", {'contrib_path': path, 'name': subdir}),
            (conftest_file_exists, create_conftest_file, "conftest.py", {'contrib_path': path}),
        ]

        # Perform tasks for each file
        for check_func, create_func, file_name, params in tasks:
            if not check_func(**params):
                create_func(**params)
            else:
                print(f" {file_name} already exists in {path}/{subdir}")


if __name__ == "__main__":
    create_files_for_contribs()
