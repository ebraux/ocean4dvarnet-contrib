"""
Script to validate the metadatas.yml files in the contrib directory.

Usage:
    python validate_contrib_metadatas.py <contrib_name>

This script checks if the 'metadatas.yml' file exists in the specified contribution folder,
parses its content, and ensures that all required fields are present.
"""

import os
import sys
import yaml

REQUIRED_FIELDS = ['name', 'description', 'date', 'contact', 'version', 'license']
CONTRIB_DIR = "./contrib"

def validate_contrib_metadatas(contrib_name):
    """
    Validate the 'metadatas.yml' file in a given contribution folder.

    This function checks if the 'metadatas.yml' file exists in the specified folder,
    parses its content, and ensures that all required fields are present.

    Parameters:
    - contrib_name (str): Name of the contribution.

    Returns:
    - bool: True if the 'metadatas.yml' file is valid, False otherwise.
    """
    contrib_info_file = os.path.join(CONTRIB_DIR, contrib_name, "metadatas.yml")

    if not os.path.exists(contrib_info_file):
        print(f"Missing contribution info file in {contrib_name}")
        return False

    with open(contrib_info_file, 'r', encoding='utf-8') as file:
        try:
            contrib_data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file in {contrib_name}: {exc}")
            return False

        missing_fields = [field for field in REQUIRED_FIELDS if field not in contrib_data]

        if missing_fields:
            print(f"Missing required fields in {contrib_name}: {', '.join(missing_fields)}")
            return False

    print(f"Contribution info for {contrib_name} is valid.")
    return True

if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python validate_contrib_metadatas.py <contrib_name>")
        sys.exit(1)

    # Get the contribution name from the command-line arguments
    contrib_name = sys.argv[1]

    # Validate the contribution metadata
    is_valid = validate_contrib_metadatas(contrib_name)

    # Exit with an appropriate status code
    if is_valid:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Failure

