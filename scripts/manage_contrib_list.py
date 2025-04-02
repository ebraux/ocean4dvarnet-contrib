"""
This script synchronizes the `docs/contrib` directory with the `contrib` directory.

Steps:
1. List subdirectories in `contrib` and `docs/contrib`.
2. Remove subdirectories in `docs/contrib` that do not exist in `contrib`.
3. Display subdirectories in `contrib` that are missing in `docs/contrib`.
4. Generate an `index.md` file in `docs/contrib` with links to the `README.md` files
   of valid subdirectories.

Example:
    If `contrib` contains:
    ```
    contrib/
    ├── folder1/
    ├── folder2/
    └── folder3/
    ```

    And `docs/contrib` contains:
    ```
    docs/contrib/
    ├── folder1/
    │   └── README.md
    ├── folder4/
    │   └── README.md
    ```

    After execution:
    - `docs/contrib/folder4` will be removed.
    - `docs/contrib/index.md` will be generated with links to valid README.md files.
"""

import os
import shutil

CONTRIB_DIR = "./contrib"
DOCS_CONTRIB_DIR = "./docs/contrib"
INDEX_FILE = "./docs/contrib/index.md"

def list_directories(path):
    """
    List all subdirectories in the given path.

    Args:
        path (str): The directory path to list subdirectories from.

    Returns:
        set: A set of subdirectory names.

    """
    if not os.path.exists(path):
        return set()
    return {name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))}

def sync_contrib_docs():
    """
    Synchronize the `docs/contrib` directory with the `contrib` directory.
    """
    # List subdirectories in contrib and docs/contrib
    contrib_dirs = list_directories(CONTRIB_DIR)
    docs_contrib_dirs = list_directories(DOCS_CONTRIB_DIR)

    print("Subdirectories in contrib:")
    print(contrib_dirs)

    print("\nSubdirectories in docs/contrib:")
    print(docs_contrib_dirs)

    # Remove directories in docs/contrib that do not exist in contrib
    for doc_dir in docs_contrib_dirs - contrib_dirs:
        doc_dir_path = os.path.join(DOCS_CONTRIB_DIR, doc_dir)
        print(f"Removing obsolete directory: {doc_dir_path}")
        shutil.rmtree(doc_dir_path)

    # List directories in contrib that do not exist in docs/contrib
    missing_in_docs = contrib_dirs - docs_contrib_dirs
    print("\nDirectories in contrib missing in docs/contrib:")
    print(missing_in_docs)

    # Generate the index.md file
    os.makedirs(DOCS_CONTRIB_DIR, exist_ok=True)
    with open(INDEX_FILE, 'w', encoding='utf-8') as index_file:
        index_file.write("# Index of Contributions\n\n")
        for doc_dir in sorted(docs_contrib_dirs & contrib_dirs):  # Only include valid directories
            readme_path = os.path.join(DOCS_CONTRIB_DIR, doc_dir, "README.md")
            if os.path.exists(readme_path):
                index_file.write(f"- [{doc_dir}](./{doc_dir}/README.md)\n")

    print(f"\nGenerated index file : {INDEX_FILE}")

#### Execution:
if __name__ == "__main__":
    sync_contrib_docs()

