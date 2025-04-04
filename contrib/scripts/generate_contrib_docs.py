"""
This script generates a Markdown file for a specific subdirectory in the 'contrib' directory.

The subdirectory name is passed as a parameter. The script generates a Markdown file
named after the subdirectory and contains a line for each Python file (*.py) in the subdirectory,
formatted as:
::: {SUBDIRECTORY_NAME} .{PYTHON_FILE_NAME}

The script ignores the `__init__.py` files and also updates an `index.md` file
with a link to the generated Markdown file.
"""

import os
import sys
import yaml

CONTRIB_DIR = "contrib"
DOCS_DIR = "docs/contrib"
INDEX_FILE = "docs/contrib/index.md"

def generate_markdown_for_contrib(contrib_name):
    """
    Generate a Markdown file for a specific subdirectory in the 'contrib' directory.

    Args:
        contrib_name (str): The name of the subdirectory to process.
    """
    subdir_path = os.path.join(CONTRIB_DIR, contrib_name)
    docdir_path = os.path.join(DOCS_DIR, contrib_name)

    # Check if the specified subdirectory exists
    if not os.path.exists(subdir_path) or not os.path.isdir(subdir_path):
        print(f"The subdirectory '{contrib_name}' does not exist in '{CONTRIB_DIR}'.")
        return

    # Ensure the docs directory exists
    os.makedirs(docdir_path, exist_ok=True)

    # Create a Markdown file named after the subdirectory
    markdown_file = os.path.join(docdir_path, 'README.md')
    print(f"Creating Markdown file: {markdown_file}")
    with open(markdown_file, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {contrib_name}\n")

        # Badges pylint and pytest
        md_file.write("![pylint](./badges/pylint.svg)")
        md_file.write("![pytest](./badges/coverage.svg)")
        md_file.write("\n\n")

        # Check if metadatas.yml exists in the subdirectory
        metadata_file_path = os.path.join(subdir_path, "metadatas.yml")
        if os.path.exists(metadata_file_path):
            with open(metadata_file_path, 'r', encoding='utf-8') as metadata_file:
                metadata_content = yaml.safe_load(metadata_file)

                if isinstance(metadata_content, dict):
                    md_file.write("| Key | Value |\n")
                    md_file.write("|-----|-------|\n")
                    for key, value in metadata_content.items():
                        md_file.write(f"| {key} | {value} |\n")
                else:
                    md_file.write("Invalid metadata format. Expected a dictionary.\n")

                md_file.write("\n" + "-" * 40 + "\n")
        else:
            md_file.write(f"No metadatas.yml found in {subdir_path}.\n" + "-" * 40 + "\n")

        # List all Python files in the subdirectory, excluding `__init__.py`
        for file in os.listdir(subdir_path):
            if file.endswith(".py") and file != "__init__.py":
                file_name_without_extension = os.path.splitext(file)[0]
                md_file.write(f"- [{file_name_without_extension}](./{file_name_without_extension}.md)\n")
                
                # Create a new Markdown file  for each Python file
                new_md_file_path = os.path.join(docdir_path, f"{file_name_without_extension}.md")
                with open(new_md_file_path, 'w', encoding='utf-8') as new_md_file:
                    new_md_file.write(f"# {contrib_name}.{file_name_without_extension}\n")
                    new_md_file.write(f"::: {CONTRIB_DIR}.{contrib_name}.{file_name_without_extension}\n")
                    print(f"Generated Markdown file: {new_md_file_path}")

    print(f"Generated Markdown file: {markdown_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_contrib_docs.py <subdirectory_name>")
        sys.exit(1)

    contrib_name = sys.argv[1]
    generate_markdown_for_contrib(contrib_name)