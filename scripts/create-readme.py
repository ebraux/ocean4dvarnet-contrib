import os

def create_readme_files():
    contrib_root = './contrib'
    
    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)
        
        if os.path.isdir(contrib_path):
            readme_path = os.path.join(contrib_path, 'README.md')
            
            if not os.path.exists(readme_path):
                with open(readme_path, 'w') as readme_file:
                    readme_file.write(f"# {contrib_folder}\n")
                print(f"Created README.md in {contrib_path}")
            else:
                print(f"README.md already exists in {contrib_path}")

if __name__ == "__main__":
    create_readme_files()