import os
import shutil
import tempfile

import pytest

from create_pyproject_files import create_pyproject_files


@pytest.fixture
def temp_contrib_dir():
    """Fixture to create a temporary 'contrib' directory with dummy subfolders."""
    temp_dir = tempfile.mkdtemp()
    contrib_path = os.path.join(temp_dir, 'contrib')
    os.makedirs(contrib_path)

    # Create subdirectories for testing
    subdirs = ['module1', 'module2']
    for sub in subdirs:
        os.makedirs(os.path.join(contrib_path, sub))

    # Patch the script's expected contrib path
    original_path = os.getcwd()
    os.chdir(temp_dir)

    yield contrib_path

    # Cleanup
    os.chdir(original_path)
    shutil.rmtree(temp_dir)


def test_create_pyproject_files_creation(temp_contrib_dir):
    """Test that pyproject.toml is created in each subdirectory."""
    create_pyproject_files()

    for subdir in ['module1', 'module2']:
        path = os.path.join(temp_contrib_dir, subdir, 'pyproject.toml')
        assert os.path.exists(path), f"{path} should exist"


def test_pyproject_toml_contents(temp_contrib_dir):
    """Test contents of pyproject.toml for expected fields."""
    create_pyproject_files()
    file_path = os.path.join(temp_contrib_dir, 'module1', 'pyproject.toml')

    with open(file_path, encoding='utf-8') as f:
        content = f.read()

    assert '[project]' in content
    assert 'name = "module1"' in content
    assert 'description = "module1"' in content
    assert 'version = "1.0.0"' in content
    assert 'license = "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"' in content
    assert 'authors = [{' in content


def test_pyproject_not_overwritten(temp_contrib_dir):
    """Test that an existing pyproject.toml is not overwritten."""
    file_path = os.path.join(temp_contrib_dir, 'module1', 'pyproject.toml')

    # Create a dummy file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("# Dummy content")

    create_pyproject_files()

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert content.strip() == "# Dummy content"
