import os
import yaml
import sys

REQUIRED_FIELDS = ['name', 'description', 'date', 'contact', 'version', 'license']

def validate_contribution_info(contrib_folder):
    contrib_info_file = os.path.join(contrib_folder, 'contribution_info.yaml')
    
    if not os.path.exists(contrib_info_file):
        print(f"Missing contribution info file in {contrib_folder}")
        return False
    
    with open(contrib_info_file, 'r') as f:
        try:
            contrib_data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file in {contrib_folder}: {exc}")
            return False
        
        missing_fields = [field for field in REQUIRED_FIELDS if field not in contrib_data]
        
        if missing_fields:
            print(f"Missing required fields in {contrib_folder}: {', '.join(missing_fields)}")
            return False
        else:
            print(f"Contribution info for {contrib_folder} is valid.")
            return True

def validate_all_contributions():
    contrib_root = './contrib'  # Adjust if necessary
    valid = True
    
    for contrib_folder in os.listdir(contrib_root):
        contrib_path = os.path.join(contrib_root, contrib_folder)
        
        if os.path.isdir(contrib_path):
            is_valid = validate_contribution_info(contrib_path)
            valid &= is_valid
    
    return valid

if __name__ == "__main__":
    if not validate_all_contributions():
        sys.exit(1)  # Non-zero exit status indicates failure
    sys.exit(0)
