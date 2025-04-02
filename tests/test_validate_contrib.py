"""
Unit tests for the `validate_contrib_info` and `validate_all_contrib` functions
from the `scripts.validate_contrib` module.

This test suite verifies the validation of individual contribution metadata
and the validation of all contributions in the contrib directory.
"""

import os
import shutil
from scripts.validate_contrib_metadatas import validate_contrib_info, validate_all_contrib

valid_contrib_name = "_test_valid_contrib"
invalid_contrib_name = "_test_invalid_contrib"

def setup_module(module):
    """
    Setup function to create temporary contrib directories with valid and invalid contributions.

    Args:
        module: The module object (automatically passed by pytest).
    """
    os.makedirs(f"./contrib/{valid_contrib_name}", exist_ok=False)
    with open(f"./contrib/{valid_contrib_name}/metadatas.yml", 'w') as f:
        f.write("""name: "valid_contrib"
description: "A valid contribution"
date: "2025-04-01"
contact: "contributor1@example.com"
version: "1.0.0"
license: "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
dependencies: ""
""")
    os.makedirs(f"./contrib/{invalid_contrib_name}", exist_ok=False)

def teardown_module(module):
    """
    Teardown function to remove the temporary contrib directories after tests are run.

    Args:
        module: The module object (automatically passed by pytest).
    """
    if os.path.exists(f"./contrib/{valid_contrib_name}"):
        shutil.rmtree(f"./contrib/{valid_contrib_name}")
    if os.path.exists(f"./contrib/{invalid_contrib_name}"):
        shutil.rmtree(f"./contrib/{invalid_contrib_name}")

def test_validate_contrib_info():
    """
    Test the `validate_contrib_info` function to ensure it correctly validates
    the metadata of individual contributions.

    - Valid contribution should return True.
    - Invalid contribution (missing metadata) should return False.
    """
    assert validate_contrib_info(f"./contrib/{valid_contrib_name}") is True
    assert validate_contrib_info(f"./contrib/{invalid_contrib_name}") is False

def test_validate_all_contrib():
    """
    Test the `validate_all_contrib` function to ensure it validates all contributions
    in the contrib directory.

    - If at least one contribution is invalid, the function should return False.
    """
    assert validate_all_contrib() is False  # One valid and one invalid contribution