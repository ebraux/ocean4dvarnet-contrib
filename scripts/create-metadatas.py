import os
#from datetime import datetime

def create_metadata_files():
    contrib_root = './contrib'
    #today_date = datetime.now().strftime("%Y-%m-%d")
    
    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)
        
        if os.path.isdir(contrib_path):
            metadata_path = os.path.join(contrib_path, 'metadatas.yml')
            if not os.path.exists(metadata_path):
                with open(metadata_path, 'w') as metadata_file:
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
