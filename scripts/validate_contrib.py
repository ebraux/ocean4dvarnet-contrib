"""
Script to validate the metadatas.yml files in the contrib directory.
"""
import os
import sys
import yaml

REQUIRED_FIELDS = ['name', 'description', 'date', 'contact', 'version', 'license']


def validate_contrib_info(contrib_folder):
    """
    Validate the 'metadatas.yml' file in a given contribution folder.

    This function checks if the 'metadatas.yml' file exists in the specified folder,
    parses its content, and ensures that all required fields are present.

    Parameters:
    - contrib_folder (str): Path to the contribution folder.

    Returns:
    - bool: True if the 'metadatas.yml' file is valid, False otherwise.
    """
    contrib_info_file = os.path.join(contrib_folder, 'metadatas.yml')

    if not os.path.exists(contrib_info_file):
        print(f"Missing contribution info file in {contrib_folder}")
        return False

    with open(contrib_info_file, 'r', encoding='utf-8') as file:
        try:
            contrib_data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file in {contrib_folder}: {exc}")
            return False

        missing_fields = [field for field in REQUIRED_FIELDS if field not in contrib_data]

        if missing_fields:
            print(f"Missing required fields in {contrib_folder}: {', '.join(missing_fields)}")
            return False

    print(f"Contribution info for {contrib_folder} is valid.")
    return True


def validate_all_contrib(contrib_root='./contrib'):
    """
    Validate all contributions in the specified 'contrib' directory.

    This function iterates through all subdirectories in the given 'contrib' folder,
    checks for the presence and validity of the 'metadatas.yml' file in each subdirectory,
    and reports any issues found.

    Parameters:
    - contrib_root (str): Path to the root 'contrib' directory. Defaults to './contrib'.

    Returns:
    - bool: True if all contributions are valid, False otherwise.
    """
    valid = True

    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)

        if os.path.isdir(contrib_path):
            is_valid = validate_contrib_info(contrib_path)
            valid &= is_valid

    return valid


def main():
    """
    Main entry point of the script.

    Validates all contributions in the 'contrib' directory. If any contribution is invalid,
    the script exits with a non-zero status code.
    """
    if not validate_all_contributions():
        sys.exit(1)  # Non-zero exit status indicates failure
    sys.exit(0)


if __name__ == "__main__":
    main()
