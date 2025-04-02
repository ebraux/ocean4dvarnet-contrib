# Creating a New Contribution

Une  contribution doit contenir au minimum :

``` bash
contrib/
├── <CONTRIB_NAME>
│   ├── __init__.py
│   ├── metadatas.yml
│   ├── README.md
│   ├── <CONTRIB_NAME>.py
|   └── tests/
|      └── test_<CONTRIB_NAME>.py
```

- `__init__.py` : fichier de configuration du module, peut êtr vide
- `metadatas.yml` : contient les information sur la contrinution, auteur, description, ...
- `README.md`
- `<CONTRIB_NAME>.py` : votre code
- `test


Il peut également contenir en plus :

- `requirement.txt`
- `pyproject.toml`
- `LICENSE.md`
- d'autres fichiers de code python

Pour initialiser une nouvelle contribution, utiliser le script `init-new-contrib`
``` bash
python scripts/init-new-contrib.sh CONTRIB_NAME
```

Pour être intégré au dépôt, la contribution sera évalué avec les outils de test de qualité de code (`pylint`, ...).

Les test ne sont pas obligatoires, mais fortement recommandés. Le code est testé avec `pytest`



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
