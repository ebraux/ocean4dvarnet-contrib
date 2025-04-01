"""
Unit tests for the `generate_contrib_docs` function from the `scripts.generate_contrib_docs` module.

This test suite verifies that the Markdown document is correctly generated based on the
metadata files in the 'contrib' directory.
"""

import os
import shutil
from pathlib import Path
from scripts.generate_contrib_docs import generate_contrib_docs

CONTRIB_DIR = "./contrib"
OUTPUT_FILE = "./contributions-list.md"

def setup_module(module):
    """
    Setup function to create temporary contrib directories with metadata files for testing.

    Args:
        module: The module object (automatically passed by pytest).
    """
    os.makedirs(CONTRIB_DIR, exist_ok=False)

    # Create a valid contribution directory with metadata
    os.makedirs(f"{CONTRIB_DIR}/valid_contrib", exist_ok=True)
    with open(f"{CONTRIB_DIR}/valid_contrib/metadatas.yml", 'w') as f:
        f.write("""name: "Valid Contribution"
description: "A valid contribution for testing."
date: "2025-04-01"
contact: "test@example.com"
version: "1.0.0"
license: "MIT"
dependencies: ["dependency1", "dependency2"]
""")

    # Create another valid contribution directory
    os.makedirs(f"{CONTRIB_DIR}/another_contrib", exist_ok=True)
    with open(f"{CONTRIB_DIR}/another_contrib/metadatas.yml", 'w') as f:
        f.write("""name: "Another Contribution"
description: "Another valid contribution for testing."
date: "2025-04-02"
contact: "another@example.com"
version: "2.0.0"
license: "Apache-2.0"
dependencies: ["dependency3"]
""")

def teardown_module(module):
    """
    Teardown function to remove the temporary contrib directories and output file after tests.

    Args:
        module: The module object (automatically passed by pytest).
    """
    if os.path.exists(CONTRIB_DIR):
        shutil.rmtree(CONTRIB_DIR)
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

def test_generate_contrib_docs():
    """
    Test the `generate_contrib_docs` function to ensure it generates the expected Markdown file.
    """
    generate_contrib_docs()

    # Check if the output file exists
    assert os.path.isfile(OUTPUT_FILE)

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

    assert "## Another Contribution (2.0.0)" in content
    assert "**Description**: Another valid contribution for testing." in content
    assert "**Date**: 2025-04-02" in content
    assert "**Contact**: another@example.com" in content
    assert "**License**: Apache-2.0" in content
    assert "**Dependencies**: dependency3" in content