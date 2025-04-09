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
from scripts import list_subdirs

CONTRIB_DIR = "./contrib"
DOCS_CONTRIB_DIR = "./docs/contrib"

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
    contrib_dirs = list_subdirs(CONTRIB_DIR)
    docs_contrib_dirs = list_subdirs(DOCS_CONTRIB_DIR)

    print("Subdirectories in contrib:")
    print(contrib_dirs)

    print("\nSubdirectories in docs/contrib:")
    print(docs_contrib_dirs)

    # Remove directories in docs/contrib that do not exist in contrib
    obsolete_in_docs= docs_contrib_dirs - contrib_dirs
    if (not obsolete_in_docs):
        print("\nNo obsolete contrib in docs/contrib.")
    else:
        for doc_dir in obsolete_in_docs:
            doc_dir_path = os.path.join(DOCS_CONTRIB_DIR, doc_dir)
            print(f"Removing obsolete contrib: {doc_dir_path}")
            shutil.rmtree(doc_dir_path)

    # List directories in contrib that do not exist in docs/contrib
    missing_in_docs = contrib_dirs - docs_contrib_dirs
    if (not missing_in_docs):
        print("\nNo contrib missing in docs/contrib.")
    else:
        print(f"\nContrib missing in docs/contrib:\n{missing_in_docs}")

    # Generate the index.md file
    os.makedirs(DOCS_CONTRIB_DIR, exist_ok=True)
    index_path = os.path.join(DOCS_CONTRIB_DIR, 'index.md')
    with open(index_path, 'w', encoding='utf-8') as index_file:
        index_file.write("# Index of Contributions\n\n")
        for doc_dir in sorted(docs_contrib_dirs & contrib_dirs):  # Only include valid directories
            readme_path = os.path.join(DOCS_CONTRIB_DIR, doc_dir)
            if os.path.exists(readme_path):
                index_file.write(f"- [{doc_dir}](./{doc_dir}/README.md)\n")

    print(f"\nGenerated index file : {index_path}")

#### Execution:
if __name__ == "__main__":
    sync_contrib_docs()
