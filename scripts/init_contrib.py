"""
Script to initialize a new contribution by creating a folder with README.md
and metadatas.yml files.
"""
import os
import re
import sys
from datetime import datetime
from scripts import write_pyproject_file, read_pyproject_metadata, create_readme, create_init_py, create_main_py, create_tests_directory, create_test_file

def is_valid_contribution_name(name):
    """
    Validate the contribution name.

    The name must only contain lowercase letters, digits, and underscores.

    Parameters:
    - name (str): The contribution name to validate.

    Returns:
    - bool: True if the name is valid, False otherwise.
    """
    return re.fullmatch(r'[a-z0-9_]+', name) is not None


def create_contribution(name):
    """
    Create a new contribution directory with a README.md, metadatas.yml, __init__.py, code and tests files.

    Parameters:
    - name (str): The name of the contribution.
    """
    contrib_root = './contrib'
    contrib_path = os.path.join(contrib_root, name)

    # Create the directory if it doesn't exist
    os.makedirs(contrib_path, exist_ok=True)

    # Create README.md
    create_readme(contrib_path=contrib_path, name=name,description=name)
    
    # Create metadatas.yml
    write_pyproject_file(contrib_path=contrib_path, name=name, description=name)
    
    # Create __init__.py
    create_init_py(contrib_path=contrib_path, name=name)
    
    # Create CONTRIB_NAME.py
    create_main_py(contrib_path=contrib_path, name=name)

    # Create tests folder
    create_tests_directory(contrib_path=contrib_path)

    # Create tests/tests_CONTRIB_NAME.py
    create_test_file(contrib_path=contrib_path, name=name)


def main():
    """
    Main entry point of the script.

    Accepts the contribution name as a command-line argument, validates it, and creates
    the necessary files and directory structure in the 'contrib' folder.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 init.py <contribution_name>")
        sys.exit(1)

    contrib_name = sys.argv[1].strip()

    if not is_valid_contribution_name(contrib_name):
        print(
            "Error: Contribution name must only contain lowercase letters, "
            "digits, and underscores."
        )
        sys.exit(1)

    create_contribution(contrib_name)


if __name__ == "__main__":
    main()
