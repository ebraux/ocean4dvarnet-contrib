"""
This script creates 'README.md' files in each subdirectory of the 'contrib' directory.

It scans the 'contrib' folder, checks for the existence of 'README.md' files, and creates
them if they are missing. The content of each 'README.md' file is a Markdown header with
the name of the subdirectory.
"""
import os


def create_readme_files():
    """
    Create 'README.md' files in each subdirectory of the 'contrib' directory.

    The script scans each subdirectory in the 'contrib' folder and checks if a 'README.md'
    file exists. If not, it creates one with a predefined structure. The content of the
    'README.md' file is a Markdown header with the name of the subdirectory.

    Requirements:
    - The 'contrib' directory must exist and contain subdirectories.

    Output:
    - A 'README.md' file in each subdirectory of 'contrib' that does not already have one.

    Example content of 'README.md':
    # Contribution Name
    """
    contrib_root = './contrib'

    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)

        if os.path.isdir(contrib_path):
            readme_path = os.path.join(contrib_path, 'README.md')

            if not os.path.exists(readme_path):
                with open(readme_path, 'w', encoding='utf-8') as readme_file:
                    readme_file.write(f"# {contrib_folder}\n")
                print(f"Created README.md in {contrib_path}")
            else:
                print(f"README.md already exists in {contrib_path}")

if __name__ == "__main__":
    create_readme_files()
