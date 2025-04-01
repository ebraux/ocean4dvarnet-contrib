import os
import shutil
from scripts.create_metadatas import create_metadata_files
from scripts.validate_contrib import validate_contrib_info

contrib_name = "_test_metadatas"

def setup_module(module):
    """Setup: Create a temporary contrib directory."""
    os.makedirs(f"./contrib/{contrib_name}", exist_ok=False)

def teardown_module(module):
    """Teardown: Remove the temporary contrib directory."""
    if os.path.exists(f"./contrib/{contrib_name}"):
        shutil.rmtree(f"./contrib/{contrib_name}")

def test_create_metadata_files():
    create_metadata_files()
    validate_contrib_info(contrib_name)