"""
This script creates 'metadatas.yml' files in each subdirectory of the 'contrib' directory.

It scans the 'contrib' folder for subdirectories and generates a 'metadatas.yml' file
with a predefined structure if one does not already exist.
"""

import os
# from datetime import datetime


def create_metadata_files():
    """
    Create 'metadatas.yml' files in each subdirectory of the 'contrib' directory.

    The script scans each subdirectory in the 'contrib' folder and checks if a 'metadatas.yml'
    file exists. If not, it creates one with a predefined structure. The 'name' and 'description'
    fields are automatically populated with the name of the subdirectory.

    Requirements:
    - The 'contrib' directory must exist and contain subdirectories.

    Output:
    - A 'metadatas.yml' file in each subdirectory of 'contrib' that does not already have one.

    Example structure of 'metadatas.yml':
    name: "Contribution Name"
    description: "Contribution Name"
    date: "yyyy-mm-dd"
    contact: "contributor1@example.com"
    version: "1.0.0"
    license: "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
    dependencies: ""
    """
    contrib_root = './contrib'
    # today_date = datetime.now().strftime("%Y-%m-%d")

    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)

        if os.path.isdir(contrib_path):
            metadata_path = os.path.join(contrib_path, 'metadatas.yml')
            if not os.path.exists(metadata_path):
                with open(metadata_path, 'w', encoding='utf-8') as metadata_file:
                    metadata_file.write(
                        f"""name: "{contrib_folder}"
description: "{contrib_folder}"
date: "yyyy-mm-dd"
contact: "contributor1@example.com"
version: "1.0.0"
license: "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
dependencies: ""
"""
                    )
                print(f"Created metadatas.yml in {contrib_path}")
            else:
                print(f"metadatas.yml already exists in {contrib_path}")

if __name__ == "__main__":
    create_metadata_files()
