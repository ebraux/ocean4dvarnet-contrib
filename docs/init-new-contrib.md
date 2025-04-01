# Creating a New Contribution

From the terminal, run the command:
``` bash
python3 scripts/init.py <YOUR_CONTRIB_NAME>
```
The contribution name must only contain lowercase letters, digits, and underscores.

If the name is valid, a folder will be created in `contrib` with the files `README.md` and `metadatas.yml`, initialized with default values.

For example, if you enter :
``` bash
python3 scripts/init.py  example_contrib
```
the script will create:

- `contrib/example_contrib/README.md` with the content:
``` bash
# example_contrib
```

- `contrib/example_contrib/metadatas.yml` with the content:
``` yaml
name: "example_contrib"
description: "example_contrib"
date: "2025-04-01"
contact: "contributor1@example.com"
version: "1.0.0"
license: "CeCILL-C FREE SOFTWARE LICENSE AGREEMENT"
dependencies: ""
```
