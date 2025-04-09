# scripts/utils.py

import os
from typing import Optional
import tomllib
import shutil

DEFAULT_AUTHOR = {
    "name": "Contributor Name",
    "email": "contributor1@example.com"
}
DEFAULT_LICENSE = "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
DEFAULT_VERSION = "1.0.0"

CONTRIB_DIR = "./contrib"
DOCS_CONTRIB_DIR = "./docs/contrib"


def readme_exists(contrib_path: str) -> bool:
    return os.path.exists(os.path.join(contrib_path, 'README.md'))

def create_readme(contrib_path: str, name: str, description: str) -> None:
    """Create an README.md file in the given contribution directory."""
    readme_path = os.path.join(contrib_path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(f"# {name}\n")
        readme_file.write(f"{description}")
    print(f"Created {readme_path}")

def init_py_exists(contrib_path: str) -> bool:
    return os.path.exists(os.path.join(contrib_path, '__init__.py'))

def create_init_py(contrib_path: str, name: str) -> None:
    """Create an __init__.py file in the given contribution directory."""
    init_py_path = os.path.join(contrib_path, '__init__.py')
    with open(init_py_path, 'w', encoding='utf-8') as init_py_file:
        init_py_file.write(f"\"\"\" {name} \"\"\"\n")
    print(f"Created {init_py_path}")

def main_py_exists(contrib_path: str, name: str) -> bool:
    return os.path.exists(os.path.join(contrib_path, f"{name}.py"))

def create_main_py(contrib_path: str, name: str) -> None:
    """Create the main Python file named after the contribution."""
    code_path = os.path.join(contrib_path, f"{name}.py")
    with open(code_path, 'w', encoding='utf-8') as code_file:
        code_file.write(f"\"\"\"ocean4dvarnet contribution {name}\"\"\"\n")
    print(f"Created {code_path}")


def create_tests_directory(contrib_path: str) -> str:
    """Create the tests directory inside the contribution directory."""
    tests_path = os.path.join(contrib_path, 'tests')
    os.makedirs(tests_path, exist_ok=True)
    print(f"Created {tests_path}/")


def test_file_exists(contrib_path: str, name: str) -> bool:
    return os.path.exists(os.path.join(contrib_path, f"test_{name}.py"))

def create_test_file(contrib_path: str, name: str) -> None:
    """Create the test file for the contribution."""
    test_path = os.path.join(contrib_path, 'tests', f"test_{name}.py")
    with open(test_path, 'w', encoding='utf-8') as test_file:
        test_file.write(f"\"\"\"tests for contribution {name}\"\"\"\n")
    print(f"Created {test_path}")



def pyproject_file_exists(contrib_path: str) -> bool:
    return os.path.exists(os.path.join(contrib_path, f"pyproject.toml"))

def write_pyproject_file(
    contrib_path: str,
    name: str,
    description: str = None,
    version: str = "1.0.0",
    license_str: str = "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT",
    author_name: str = "Contributor Name",
    author_email: str = "contributor1@example.com",
    dependencies: list[str] = None
) -> None:
    """
    Generate a pyproject.toml file with customizable metadata.

    Args:
        contrib_path (str): Path to the target directory.
        name (str): Name of the project (also used as default description).
        description (str, optional): Project description. Defaults to name.
        version (str): Version of the project.
        license_str (str): License text or ID.
        author_name (str): Name of the author.
        author_email (str): Email of the author.
        dependencies (list[str], optional): List of dependencies.
    """
    description = description or name
    dependencies = dependencies or []

    pyproject_toml_file_path = os.path.join(contrib_path, 'pyproject.toml')
    if dependencies:
        deps_str = "\n".join([f'"{dep}",' for dep in dependencies])
        deps_section = f" [\n{deps_str}\n]"
    else:
        deps_section = " []"

    content = f"""[project]
name = "{name}"
description = "{description}"
version = "{version}"
license = "{license_str}"
authors = [{{ name = "{author_name}", email = "{author_email}" }}]
dependencies = {deps_section}
"""

    with open(pyproject_toml_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {pyproject_toml_file_path}")




def read_pyproject_metadata(pyproject_path: str) -> Optional[dict]:
    """
    Reads a pyproject.toml file and extracts the [project] section.

    Args:
        pyproject_path (str): Path to the pyproject.toml file.

    Returns:
        Optional[dict]: A dictionary containing metadata from the [project] section,
                        or None if the file or section is missing.
    """
    if not os.path.exists(pyproject_path):
        return None

    with open(pyproject_path, 'rb') as f:
        data = tomllib.load(f)

    return data.get("project")


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


def validate_contrib_metadata(contrib_name: str) -> bool:
    """
    Validate the pyproject.toml metadata for a given contribution.

    Args:
        contrib_name (str): Name of the contribution folder.

    Returns:
        bool: True if metadata is valid, False otherwise.
    """
    pyproject_path = os.path.join(CONTRIB_DIR, contrib_name, "pyproject.toml")
    metadata = read_pyproject_metadata(pyproject_path)

    if metadata is None:
        print(f"Missing or invalid pyproject.toml in {contrib_name}")
        return False

    missing_fields = [field for field in REQUIRED_FIELDS if field not in metadata]

    if missing_fields:
        print(f"Missing required fields in {contrib_name}: {', '.join(missing_fields)}")
        return False

    print(f"Metadata for {contrib_name} is valid.")
    return True
