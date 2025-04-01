"""
This script generates a Markdown file for each subdirectory in the 'contrib' directory.

Each Markdown file is named after its corresponding subdirectory and contains a line
for each Python file (*.py) in the subdirectory, formatted as:
::: {SUBDIRECTORY_NAME} .{PYTHON_FILE_NAME}

The script ignores the `__init__.py` files and also generates an `index.md` file
containing links to all the generated Markdown files.
"""

import os
import shutil
import yaml

CONTRIB_DIR = "./contrib"
DOCS_DIR = "./docs/api"
INDEX_FILE = "./docs/api/index.md"

def generate_markdown_files():
    """
    Generate a Markdown file for each subdirectory in the 'contrib' directory.

    Each Markdown file is named after the subdirectory and contains a line for
    each Python file (*.py) in the subdirectory, excluding `__init__.py`.

    Additionally, an `index.md` file is created with links to all the generated Markdown files.
    """
    if not os.path.exists(CONTRIB_DIR):
        print(f"The directory '{CONTRIB_DIR}' does not exist.")
        return

    # Remove existing docs directory if it exists
    if os.path.exists(f"{DOCS_DIR}"):
        shutil.rmtree(f"{DOCS_DIR}")
    os.makedirs(f"{DOCS_DIR}", exist_ok=False)

    markdown_files = []

    for subdir in os.listdir(CONTRIB_DIR):
        subdir_path = os.path.join(CONTRIB_DIR, subdir)

        # Skip if it's not a directory
        if not os.path.isdir(subdir_path):
            continue

        # Create a Markdown file named after the subdirectory
        markdown_file = os.path.join(DOCS_DIR, f"{subdir}.md")
        markdown_files.append(markdown_file)
        
        with open(markdown_file, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# {subdir}\n\n")

            # Check if metadatas.yml exists in the subdirectory
            metadata_file_path = os.path.join(subdir_path, "metadatas.yml")
            if os.path.exists(metadata_file_path):
                with open(metadata_file_path, 'r', encoding='utf-8') as metadata_file:
                    metadata_content = yaml.safe_load(metadata_file)
                    
                    if isinstance(metadata_content, dict):
                        md_file.write(f"| Key | Value |\n")
                        md_file.write(f"|-----|-------|\n")
                        for key, value in metadata_content.items():
                            md_file.write(f"| {key} | {value} |\n")
                    else:
                        md_file.write("Invalid metadata format. Expected a dictionary.\n")
                    
                    md_file.write(f"\n" + "-" * 40 + "\n")
            else:
                md_file.write(f"No metadatas.yml found in {subdir_path}.\n" + "-" * 40 + "\n")
            
            # List all Python files in the subdirectory, excluding `__init__.py`
            for file in os.listdir(subdir_path):
                if file.endswith(".py") and file != "__init__.py":
                    file_name_without_extension = os.path.splitext(file)[0]
                    md_file.write(f"::: {subdir}.{file_name_without_extension}\n")

        print(f"Generated Markdown file: {markdown_file}")

    # Generate the index.md file
    with open(INDEX_FILE, 'w', encoding='utf-8') as index_file:
        index_file.write("# Index of Contributions\n\n")
        for markdown_file in sorted(markdown_files):
            file_name = os.path.basename(markdown_file)
            subdir_name = os.path.splitext(file_name)[0]
            index_file.write(f"- [{subdir_name}]({file_name})\n")

    print(f"Generated index file: {INDEX_FILE}")

if __name__ == "__main__":
    generate_markdown_files()