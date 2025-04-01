import os
import yaml

def generate_contrib_docs():
    contrib_root = './contrib'
    doc_filename = 'contributions-list.md'
    
    with open(doc_filename, 'w') as doc:
        doc.write("# Contributions\n\n")
        
        for contrib_folder in os.listdir(contrib_root):
            contrib_path = os.path.join(contrib_root, contrib_folder)
            
            if os.path.isdir(contrib_path):
                contrib_info_file = os.path.join(contrib_path, 'metadatas.yml')
                
                with open(contrib_info_file, 'r') as f:
                    contrib_data = yaml.safe_load(f)
                    doc.write(f"## {contrib_data['name']} ({contrib_data['version']})\n\n")
                    doc.write(f"**Description**: {contrib_data['description']}\n\n")
                    doc.write(f"**Date**: {contrib_data['date']}\n\n")
                    doc.write(f"**Contact**: {contrib_data['contact']}\n\n")
                    doc.write(f"**License**: {contrib_data['license']}\n\n")
                    doc.write(f"**Dependencies**: {', '.join(contrib_data['dependencies'])}\n\n")
                    doc.write("---\n\n")

if __name__ == "__main__":
    generate_contrib_docs()
