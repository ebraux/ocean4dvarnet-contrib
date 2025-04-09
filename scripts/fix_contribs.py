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

        if not pyproject_file_exists(contrib_path=path):
            write_pyproject_file(contrib_path=path, name=subdir)
        else:
            print(f" pyproject.toml already exists in {path}/{subdir}")

        if not readme_exists(contrib_path=path):
            create_readme(contrib_path=path, name=subdir)
        else:
            print(f" README.md already exists in {path}/{subdir}")

        if not init_py_exists(contrib_path=path):
            create_init_py(contrib_path=path, name=subdir)
        else:
            print(f" __init__.py already exists in {path}/{subdir}")

        if not main_py_exists(contrib_path=path, name=subdir):
            create_main_py(contrib_path=path, name=subdir)
        else:
            print(f" {subdir}.py already exists in {path}/{subdir}")

        create_tests_directory(contrib_path=path)

        if not test_file_exists(contrib_path=path, name=subdir):
            create_test_file(contrib_path=path, name=subdir)
        else:
            print(f" test_{subdir}.py already exists in {path}/{subdir}/test")

if __name__ == "__main__":
    create_files_for_contribs()
