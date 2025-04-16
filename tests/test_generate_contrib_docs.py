"""
Unit tests for the `generate_markdown_for_contrib` function from the `scripts.generate_contrib_docs` module.

This test suite verifies that the Markdown document is correctly generated based on the
metadata files in the 'contrib' directory.
"""

import os
import shutil
from pathlib import Path
from scripts.generate_contrib_docs import generate_markdown_for_contrib

CONTRIB_DIR = "./contrib"


def setup_module(module):
    """
    Setup function to create temporary contrib directories with metadata files for testing.

    Args:
        module: The module object (automatically passed by pytest).
    """
    
    # Create a valid contribution directory with metadata
    os.makedirs(f"{CONTRIB_DIR}/tests_valid_contrib", exist_ok=True)
    with open(f"{CONTRIB_DIR}/tests_valid_contrib/metadatas.yml", 'w') as f:
        f.write("""name: "Valid Contribution"
description: "A valid contribution for testing."
date: "2025-04-01"
contact: "test@example.com"
version: "1.0.0"
license: "MIT"
dependencies: ["dependency1", "dependency2"]
""")


def teardown_module(module):
    """
    Teardown function to remove the temporary contrib directories and output file after tests.

    Args:
        module: The module object (automatically passed by pytest).
    """
    if os.path.exists(f"{CONTRIB_DIR}/tests_valid_contrib"):
        shutil.rmtree(f"{CONTRIB_DIR}/tests_valid_contrib")

def test_generate_markdown_for_contrib():
    """
    Test the `generate_markdown_for_contrib` function to ensure it generates the expected Markdown file.
    """
    generate_markdown_for_contrib('tests_valid_contrib')

    # Check if the output file exists
    assert os.path.isfile(f"{CONTRIB_DIR}/tests_valid_contrib/metadatas.yml")

    # Verify the content of the generated Markdown file
    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "# Contributions" in content
    assert "## Valid Contribution (1.0.0)" in content
    assert "**Description**: A valid contribution for testing." in content
    assert "**Date**: 2025-04-01" in content
    assert "**Contact**: test@example.com" in content
    assert "**License**: MIT" in content
    assert "**Dependencies**: dependency1, dependency2" in content

