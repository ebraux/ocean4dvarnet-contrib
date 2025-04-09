import os
import shutil
import pytest

from generate_contrib_docs import (
    read_pyproject_metadata,
    generate_python_file_docs,
    write_readme,
    generate_markdown_for_contrib,
)


@pytest.fixture
def example_contrib_dir(tmp_path):
    """
    Create a temporary contrib module with:
    - pyproject.toml
    - 2 Python files
    """
    contrib_name = "my_module"
    contrib_path = tmp_path / "contrib" / contrib_name
    contrib_path.mkdir(parents=True)

    # pyproject.toml with basic metadata
    pyproject = contrib_path / "pyproject.toml"
    pyproject.write_text("""
[project]
name = "my_module"
version = "0.1.0"
description = "Example contrib module"
authors = [{name = "Alice"}, {name = "Bob"}]
""")

    # Sample Python files
    (contrib_path / "script1.py").write_text("# Script 1")
    (contrib_path / "script2.py").write_text("# Script 2")
    (contrib_path / "__init__.py").write_text("# Init")

    return tmp_path, contrib_name


def test_read_pyproject_metadata(example_contrib_dir):
    tmp_path, contrib_name = example_contrib_dir
    contrib_path = tmp_path / "contrib" / contrib_name
    metadata = read_pyproject_metadata(contrib_path / "pyproject.toml")

    assert metadata["name"] == "my_module"
    assert metadata["version"] == "0.1.0"
    assert isinstance(metadata["authors"], list)


def test_generate_python_file_docs(example_contrib_dir):
    tmp_path, contrib_name = example_contrib_dir
    contrib_path = tmp_path / "contrib" / contrib_name
    doc_path = tmp_path / "docs" / "contrib" / contrib_name
    doc_path.mkdir(parents=True)

    files = generate_python_file_docs(contrib_name, str(contrib_path), str(doc_path))

    assert sorted(files) == ["script1", "script2"]

    for name in files:
        md = doc_path / f"{name}.md"
        assert md.exists()
        assert f"::: contrib.{contrib_name}.{name}" in md.read_text()


def test_write_readme(example_contrib_dir):
    tmp_path, contrib_name = example_contrib_dir
    contrib_path = tmp_path / "contrib" / contrib_name
    doc_path = tmp_path / "docs" / "contrib" / contrib_name
    doc_path.mkdir(parents=True)

    metadata = read_pyproject_metadata(contrib_path / "pyproject.toml")
    py_files = ["script1", "script2"]

    write_readme(contrib_name, str(doc_path), metadata, py_files, str(contrib_path))

    readme = doc_path / "README.md"
    content = readme.read_text()
    assert "# my_module" in content
    assert "| name | my_module |" in content
    assert "- [script1](./script1.md)" in content


def test_generate_markdown_for_contrib_end_to_end(example_contrib_dir):
    tmp_path, contrib_name = example_contrib_dir
    os.chdir(tmp_path)  # simulate project root

    generate_markdown_for_contrib(contrib_name)

    doc_path = tmp_path / "docs" / "contrib" / contrib_name
    assert (doc_path / "README.md").exists()
    assert (doc_path / "script1.md").exists()
    assert (doc_path / "script2.md").exists()


def test_missing_pyproject(monkeypatch, tmp_path):
    contrib_name = "empty_module"
    contrib_path = tmp_path / "contrib" / contrib_name
    contrib_path.mkdir(parents=True)
    (contrib_path / "hello.py").write_text("print('hi')")

    os.chdir(tmp_path)
    generate_markdown_for_contrib(contrib_name)

    readme_path = tmp_path / "docs" / "contrib" / contrib_name / "README.md"
    assert readme_path.exists()
    assert "No pyproject.toml" in readme_path.read_text()
