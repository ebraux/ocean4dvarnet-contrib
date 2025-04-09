# scripts/generate_contrib_files.py

import os
import argparse
from scripts import pyproject_file_exists, write_pyproject_file, readme_exists, create_readme, init_py_exists, create_init_py, main_py_exists, create_main_py, create_tests_directory, test_file_exists, create_test_file

CONTRIB_DIR = "./contrib"


def get_contrib_subdirs() -> list:
    return [
        name for name in os.listdir(CONTRIB_DIR)
        if os.path.isdir(os.path.join(CONTRIB_DIR, name))
    ]



def create_files_for_contribs() -> None:

    if not os.path.exists(CONTRIB_DIR):
        print(f" The directory '{CONTRIB_DIR}' does not exist.")
        return

    for subdir in get_contrib_subdirs():
        path = os.path.join(CONTRIB_DIR, subdir)

        if not pyproject_file_exists(contrib_path=path):
            write_pyproject_file(contrib_path=path, name=subdir)
        else:
            print(f" pyproject.toml already exists in {path}/{subdir}")

        if not readme_exists(contrib_path=path):
            write_readme_file(contrib_path=path, name=subdir)
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
