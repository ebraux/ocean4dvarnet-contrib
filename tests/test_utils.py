# pylint: disable=redefined-outer-name
"""Unit tests for  utils.py"""
import os
import shutil
import tempfile

import pytest

from scripts import utils


@pytest.fixture
def contrib_dir_fixture():
    """
    Creates a temporary directory simulating a contribution folder with a valid structure.
    Automatically cleans up after the test.

    Yields:
        tuple: A tuple containing the temporary directory path, contribution name, and contribution path.
    """
    temp_dir = tempfile.mkdtemp()
    contrib_name = "test_contrib"
    contrib_path = os.path.join(temp_dir, contrib_name)
    os.makedirs(contrib_path)
    yield temp_dir, contrib_name, contrib_path
    shutil.rmtree(temp_dir)


def test_create_readme(contrib_dir_fixture):
    """
    Test that the README.md file is created with the correct title and description.
    """
    _, name, path = contrib_dir_fixture
    utils.create_readme(path, name, "Test description")
    readme_path = os.path.join(path, "README.md")
    assert os.path.exists(readme_path)
    with open(readme_path, encoding="utf-8") as f:
        content = f.read()
    assert f"# {name}" in content



def test_create_init_py(contrib_dir_fixture):
    """
    Test that the __init__.py file is created with the module docstring.
    """
    _, name, path = contrib_dir_fixture
    utils.create_init_py(path, name)
    init_path = os.path.join(path, "__init__.py")
    assert os.path.exists(init_path)
    with open(init_path, encoding="utf-8") as f:
        content = f.read()
    assert name in content


def test_create_main_py(contrib_dir_fixture):
    """
    Test that the main Python file is created with a valid docstring.
    """
    _, name, path = contrib_dir_fixture
    utils.create_main_py(path, name)
    main_py = os.path.join(path, f"{name}.py")
    assert os.path.exists(main_py)
    with open(main_py, encoding="utf-8") as f:
        content = f.read()
    assert f"contribution {name}" in content


def test_create_tests_directory_and_file(contrib_dir_fixture):
    """
    Test that the tests/ directory and test file are correctly created.
    """
    _, name, path = contrib_dir_fixture
    utils.create_tests_directory(path)
    utils.create_test_file(path, name)
    test_file = os.path.join(path, "tests", f"test_{name}.py")
    assert os.path.exists(test_file)
    with open(test_file, encoding="utf-8") as f:
        content = f.read()
    assert "tests for contribution" in content


def test_write_and_read_pyproject_file(contrib_dir_fixture):
    """
    Test writing and reading metadata from pyproject.toml.
    """
    _, name, path = contrib_dir_fixture
    utils.write_pyproject_file(
        path,
        name,
        metadata={
            "description": "A test contrib",
            "author_name": "Jane Doe",
            "author_email": "jane@example.com",
            "dependencies": ["numpy", "torch"]
        }
    )

    pyproject_path = os.path.join(path, "pyproject.toml")
    assert os.path.exists(pyproject_path)

    metadata = utils.read_pyproject_metadata(pyproject_path)
    assert metadata is not None
    assert metadata["name"] == name
    assert metadata["description"] == "A test contrib"
    assert metadata["authors"][0]["name"] == "Jane Doe"
    assert "numpy" in metadata["dependencies"]


def test_validate_contrib_metadata_success(contrib_dir_fixture):
    """
    Test that validation succeeds with a valid pyproject.toml.
    """
    temp_dir, name, path = contrib_dir_fixture
    utils.write_pyproject_file(path, name)
    valid = utils.validate_contrib_metadata(name, base_path=temp_dir)
    assert valid is True


def test_validate_contrib_metadata_missing_fields(contrib_dir_fixture):
    """
    Test that validation fails when required fields are missing in pyproject.toml.
    """
    temp_dir, name, path = contrib_dir_fixture
    pyproject_path = os.path.join(path, "pyproject.toml")
    with open(pyproject_path, "w", encoding="utf-8") as f:
        f.write("[project]\nname = \"incomplete\"\n")
    valid = utils.validate_contrib_metadata(name, base_path=temp_dir)
    assert valid is False
