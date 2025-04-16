"""
Unit tests for the `create_readme_files` function from the `scripts.create_readme` module.

This test suite verifies the creation of README files in a temporary contrib directory.
"""

import os
import shutil
from scripts.create_readme import create_readme_files

contrib_name = "_test_readme"

def setup_module(module):
    """
    Setup function to create a temporary contrib directory before tests are run.

    Args:
        module: The module object (automatically passed by pytest).
    """
    os.makedirs(f"./contrib/{contrib_name}", exist_ok=False)

def teardown_module(module):
    """
    Teardown function to remove the temporary contrib directory after tests are run.

    Args:
        module: The module object (automatically passed by pytest).
    """
    if os.path.exists(f"./contrib/{contrib_name}"):
        shutil.rmtree(f"./contrib/{contrib_name}")

def test_create_readme_files():
    """
    Test the `create_readme_files` function to ensure it creates a README.md file
    with the correct content in the temporary contrib directory.
    """
    create_readme_files()
    assert os.path.isfile(f"./contrib/{contrib_name}/README.md")
    with open(f"./contrib/{contrib_name}/README.md", 'r') as f:
        content = f.read()
        assert content == f"# {contrib_name}\n"
