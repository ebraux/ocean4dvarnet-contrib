"""
Script to initialize a new contribution by creating a folder with README.md
and metadatas.yml files.
"""
import os
import re
import sys
from datetime import datetime


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
    Create a new contribution directory with a README.md and metadatas.yml file.

    Parameters:
    - name (str): The name of the contribution.
    """
    contrib_root = './contrib'
    contrib_path = os.path.join(contrib_root, name)

    # Create the directory if it doesn't exist
    os.makedirs(contrib_path, exist_ok=True)

    # Create README.md
    readme_path = os.path.join(contrib_path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(f"# {name}\n")
    print(f"Created README.md in {contrib_path}")

    # Create metadatas.yml
    metadata_path = os.path.join(contrib_path, 'metadatas.yml')
    today_date = datetime.now().strftime("%Y-%m-%d")
    with open(metadata_path, 'w', encoding='utf-8') as metadata_file:
        metadata_file.write(
            f"""name: "{name}"
description: "{name}"
date: "{today_date}"
contact: "contributor1@example.com"
version: "1.0.0"
license: "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
dependencies: ""
"""
        )
    print(f"Created metadatas.yml in {contrib_path}")

    # Create __init__.py
    init_py_path = os.path.join(contrib_path, '__init__.py')
    with open(init_py_path, 'w', encoding='utf-8') as init_py_path:
        init_py_path.write(f"# {name}\n")
    print(f"Created __init__.py in {contrib_path}")


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
