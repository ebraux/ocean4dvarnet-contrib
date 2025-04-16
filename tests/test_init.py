"""
Unit tests for the `is_valid_contribution_name` and `create_contribution` functions
from the `scripts.init` module.

This test suite verifies the validation of contribution names and the creation
of contribution directories with the required files.
"""

import os
import shutil
from scripts.init_contrib import is_valid_contribution_name, create_contribution

contrib_name = "_test_contrib"

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

def test_is_valid_contribution_name():
    """
    Test the `is_valid_contribution_name` function to ensure it correctly validates
    contribution names based on predefined rules.
    """
    assert is_valid_contribution_name("valid_name123") is True
    assert is_valid_contribution_name("Invalid-Name") is False
    assert is_valid_contribution_name("invalid name") is False
    assert is_valid_contribution_name("valid_name") is True

def test_create_contribution():
    """
    Test the `create_contribution` function to ensure it creates a contribution
    directory with the required files (README.md and metadatas.yml).
    """
    contrib_name = "test_contrib"
    create_contribution(contrib_name)
    contrib_path = f"./contrib/{contrib_name}"
    assert os.path.exists(contrib_path)
    assert os.path.isfile(f"{contrib_path}/README.md")
    assert os.path.isfile(f"{contrib_path}/metadatas.yml")