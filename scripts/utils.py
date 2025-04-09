"""
utils.py - Utility functions for managing Ocean4DVarNet contributions

This module provides helper functions to manage the initialization,
validation, and documentation of contribution folders inside the `contrib/`
directory. Each contribution typically contains:

- A `pyproject.toml` file with project metadata
- A main Python file named after the contribution
- A `README.md` file
- An `__init__.py` file
- A `tests/` subdirectory with a test file

Key functionalities include:
- Reading and validating `pyproject.toml` metadata
- Automatically generating boilerplate files (`README.md`, `__init__.py`, etc.)
- Synchronizing documentation folders (`docs/contrib/`)
- Utility methods to check file/directory existence and list subfolders

Constants:
- `CONTRIB_DIR`: Root path for contributions
- `DOCS_CONTRIB_DIR`: Root path for associated documentation

This module assumes contributions follow a standardized structure and can be used
in CLI scripts or tests to automate common tasks.

Dependencies:
- Python 3.11+ (for `tomllib`)
- For Python 3.6–3.10, the `tomli` library is used as a fallback. Ensure it is installed:
    `pip install tomli`
"""
import os
import sys
from typing import Optional
import shutil

# Load tomllib (Python 3.11+) or fallback to tomli
try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    try:
        import tomli as tomllib  # Python 3.6–3.10
    except ModuleNotFoundError:
        print("Error: Python < 3.11 detected. You need to install 'tomli':\n  pip install tomli")
        sys.exit(1)


DEFAULT_AUTHOR = {
    "name": "Contributor Name",
    "email": "contributor1@example.com"
}
DEFAULT_LICENSE = "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
DEFAULT_VERSION = "1.0.0"

CONTRIB_DIR = "./contrib"
DOCS_CONTRIB_DIR = "./docs/contrib"
REQUIRED_FIELDS = ['name', 'description', 'contact', 'version', 'license']




def list_subdirs(path):
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



def readme_exists(contrib_path: str) -> bool:
    """
    Checks if a README.md file exists in the specified directory.

    Args:
        contrib_path (str): The path to the directory where the README.md file is expected.

    Returns:
        bool: True if the README.md file exists in the specified directory, False otherwise.
    """
    return os.path.exists(os.path.join(contrib_path, 'README.md'))

def create_readme(contrib_path: str, name: str, description: str = "") -> None:
    """
    Create a README.md file in the specified contribution directory.

    Args:
        contrib_path (str): The path to the contribution directory where the README.md file will be created.
        name (str): The title to be written at the top of the README.md file.
        description (str, optional): An optional description to include in the 
            README.md file. Defaults to an empty string.
    """
    readme_path = os.path.join(contrib_path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(f"# {name}\n")
        if description:
            readme_file.write(f"{description}")
    print(f"Created {readme_path}")

def init_py_exists(contrib_path: str) -> bool:
    """
    Checks if an '__init__.py' file exists in the specified directory.

    Args:
        contrib_path (str): The path to the directory to check.

    Returns:
        bool: True if the '__init__.py' file exists in the directory, False otherwise.
    """
    return os.path.exists(os.path.join(contrib_path, '__init__.py'))

def create_init_py(contrib_path: str, name: str) -> None:
    """
    Create an __init__.py file in the specified contribution directory.

    This function generates an __init__.py file in the given directory path
    and writes a simple docstring containing the provided name.

    Args:
        contrib_path (str): The path to the contribution directory where the
            __init__.py file will be created.
        name (str): The name to include in the docstring of the __init__.py file.

    Returns:
        None
    """
    init_py_path = os.path.join(contrib_path, '__init__.py')
    with open(init_py_path, 'w', encoding='utf-8') as init_py_file:
        init_py_file.write(f"\"\"\" {name} \"\"\"\n")
    print(f"Created {init_py_path}")

def main_py_exists(contrib_path: str, name: str) -> bool:
    """
    Checks if a Python file with the specified name exists in the given directory.

    Args:
        contrib_path (str): The path to the directory where the file is expected to be located.
        name (str): The name of the Python file (without the .py extension).

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(os.path.join(contrib_path, f"{name}.py"))

def create_main_py(contrib_path: str, name: str) -> None:
    """
    Create a main Python file for a contribution.

    This function generates a Python file with the specified name in the given
    contribution path. The file will contain a basic docstring indicating it
    is part of the ocean4dvarnet contributions.

    Args:
        contrib_path (str): The directory path where the Python file will be created.
        name (str): The name of the Python file (without the .py extension).

    Returns:
        None
    """
    code_path = os.path.join(contrib_path, f"{name}.py")
    with open(code_path, 'w', encoding='utf-8') as code_file:
        code_file.write(f"\"\"\"ocean4dvarnet contribution {name}\"\"\"\n")
    print(f"Created {code_path}")


def create_tests_directory(contrib_path: str) -> str:
    """
    Creates a 'tests' directory inside the specified contribution directory.

    Args:
        contrib_path (str): The path to the contribution directory where the 'tests' directory will be created.

    Returns:
        str: The path to the created 'tests' directory.

    Notes:
        If the 'tests' directory already exists, this function will not raise an error.
    """
    tests_path = os.path.join(contrib_path, 'tests')
    os.makedirs(tests_path, exist_ok=True)
    print(f"Created {tests_path}/")


def test_file_exists(contrib_path: str, name: str) -> bool:
    """
    Check if a test file with a specific name exists in the given directory.

    Args:
        contrib_path (str): The path to the directory where the test file is expected to be located.
        name (str): The base name of the test file (without the "test_" prefix and ".py" extension).

    Returns:
        bool: True if the test file exists, False otherwise.
    """
    return os.path.exists(os.path.join(contrib_path, f"test_{name}.py"))

def create_test_file(contrib_path: str, name: str) -> None:
    """Create the test file for the contribution."""
    test_path = os.path.join(contrib_path, 'tests', f"test_{name}.py")
    with open(test_path, 'w', encoding='utf-8') as test_file:
        test_file.write(f"\"\"\"tests for contribution {name}\"\"\"\n")
    print(f"Created {test_path}")



def pyproject_file_exists(contrib_path: str) -> bool:
    """
    Checks if a 'pyproject.toml' file exists in the specified directory.

    Args:
        contrib_path (str): The path to the directory where the function will look for the 'pyproject.toml' file.

    Returns:
        bool: True if the 'pyproject.toml' file exists in the specified directory, False otherwise.
    """
    return os.path.exists(os.path.join(contrib_path, 'pyproject.toml'))

def write_pyproject_file(
    contrib_path: str,
    name: str,
    metadata: Optional[dict] = None
) -> None:
    """
    Generate a `pyproject.toml` file with customizable metadata for a Python project.

    This function creates a `pyproject.toml` file in the specified directory with
    the provided project metadata, including name, description, version, license,
    author information, and dependencies.

    Args:
        contrib_path (str): The directory path where the `pyproject.toml` file will be created.
        name (str): The name of the project. This will also be used as the default description if none is provided.
        metadata (dict, optional): A dictionary containing project metadata, such as:
            - description (str): A brief description of the project.
            - version (str): The version of the project.
            - license (str): The license type or text for the project.
            - author_name (str): The name of the author.
            - author_email (str): The email address of the author.
            - dependencies (list[str]): A list of project dependencies.

    Returns:
        None: This function does not return a value. It writes the `pyproject.toml` file to the specified directory.

    Raises:
        OSError: If there is an issue writing the file to the specified directory.

    Example:
        write_pyproject_file(
            contrib_path="/path/to/project",
            name="my_project",
            metadata={
                "description": "A sample Python project",
                "version": "0.1.0",
                "license": "MIT",
                "author_name": "John Doe",
                "author_email": "john.doe@example.com",
                "dependencies": ["numpy", "pandas"]
            }
        )
    """
    metadata = metadata or {}
    description = metadata.get("description", name)
    version = metadata.get("version", "1.0.0")
    license_str = metadata.get("license", "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT")
    author_name = metadata.get("author_name", "Contributor Name")
    author_email = metadata.get("author_email", "contributor1@example.com")
    dependencies = metadata.get("dependencies", [])

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
