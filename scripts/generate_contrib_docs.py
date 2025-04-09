"""
This script generates Markdown documentation for a specific subdirectory
inside the 'contrib' directory of a project.

It performs the following tasks:
- Reads metadata from a `pyproject.toml` file located in the contrib submodule.
- Creates a `README.md` file in the corresponding `docs/contrib/<subdir>` directory
  with badges, metadata table, and links to individual module documentation.
- Creates a separate Markdown file for each Python module (excluding `__init__.py`)
  using the `:::` directive compatible with tools like `mkdocstrings`.

This tool is intended to help automate documentation generation for modular
contrib packages, especially in a monorepo-style structure.

Requirements:
- Python 3.11+ (uses `tomllib`), or
- Python 3.6–3.10 with `tomli` installed (`pip install tomli`)
"""

import os
import sys
from typing import Optional
from scripts import read_pyproject_metadata


def generate_python_file_docs(module_name: str, subdir_path: str, docdir_path: str) -> list:
    """
    Generates a Markdown documentation file for each Python module in the given subdirectory.

    Args:
        module_name (str): The name of the contribution module (used in headings and paths).
        subdir_path (str): Path to the source contrib directory.
        docdir_path (str): Path where the Markdown documentation files will be written.

    Returns:
        list: List of Python module filenames (without .py extension) that were processed.
    """
    entries = []
    for file in os.listdir(subdir_path):
        if file.endswith(".py") and file != "__init__.py":
            name = os.path.splitext(file)[0]
            entries.append(name)

            # Generate a Markdown file for each Python file
            md_path = os.path.join(docdir_path, f"{name}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {module_name}.{name}\n")
                f.write(f"::: contrib.{module_name}.{name}\n")
                print(f"Generated Markdown file: {md_path}")
    return entries


def write_readme(module_name: str, docdir_path: str, metadata: Optional[dict],
                 py_files: list, subdir_path: str) -> None:
    """
    Creates a README.md file summarizing the contrib module, its metadata,
    and links to individual module docs.

    Args:
        module_name (str): The name of the contrib submodule.
        docdir_path (str): Output path for the README.md file.
        metadata (Optional[dict]): Metadata dictionary from pyproject.toml.
        py_files (list): List of processed Python file names (no extensions).
        subdir_path (str): Path to the original contrib source directory.
    """
    readme_path = os.path.join(docdir_path, "README.md")

    with open(readme_path, 'w', encoding='utf-8') as md_file:
        # Title and badges
        md_file.write(f"# {module_name}\n")
        md_file.write("![pylint](./badges/pylint.svg)")
        md_file.write("![pytest](./badges/coverage.svg)\n\n")

        # Metadata table
        if metadata:
            md_file.write("| Key | Value |\n|-----|-------|\n")
            for key, value in metadata.items():
                # Special formatting for authors list
                if key == "authors" and isinstance(value, list):
                    authors = ", ".join(a.get("name", "") for a in value if isinstance(a, dict))
                    md_file.write(f"| {key} | {authors} |\n")
                else:
                    md_file.write(f"| {key} | {value} |\n")
        else:
            md_file.write(f"No pyproject.toml or [project] section found in {subdir_path}.\n")

        md_file.write("\n" + "-" * 40 + "\n")

        # Links to individual module docs
        for name in py_files:
            md_file.write(f"- [{name}](./{name}.md)\n")

    print(f"Generated Markdown file: {readme_path}")


def generate_markdown_for_contrib(module_name: str,
                                  contrib_dir: str = "contrib",
                                  docs_dir: str = "docs/contrib") -> None:
    """
    Orchestrates the documentation generation for a contrib submodule.

    Args:
        module_name (str): Name of the submodule inside contrib/.
        contrib_dir (str): Path to the contrib source directory.
        docs_dir (str): Path to the output documentation directory.
    """
    subdir_path = os.path.join(contrib_dir, module_name)
    docdir_path = os.path.join(docs_dir, module_name)

    # Check if the target subdirectory exists
    if not os.path.exists(subdir_path) or not os.path.isdir(subdir_path):
        print(f"The subdirectory '{module_name}' does not exist in '{contrib_dir}'.")
        return

    # Ensure output directory exists
    os.makedirs(docdir_path, exist_ok=True)

    # Load metadata from pyproject.toml
    metadata = read_pyproject_metadata(os.path.join(subdir_path, "pyproject.toml"))

    # Generate .md files for each Python module
    py_files = generate_python_file_docs(module_name, subdir_path, docdir_path)

    # Generate the README.md summary
    write_readme(module_name, docdir_path, metadata, py_files, subdir_path)


if __name__ == "__main__":
    # Command-line interface
    if len(sys.argv) != 2:
        print("Usage: python generate_contrib_docs.py <subdirectory_name>")
        sys.exit(1)

    contrib_name = sys.argv[1]
    generate_markdown_for_contrib(contrib_name)
