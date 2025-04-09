# generate_contrib_docs

---

::: scripts.generate_contrib_docs



La fonction read_pyproject_metadata retourne uniquement la section [project].

Les auteurs sont formatés proprement si présents en liste.

Ce code utilise tomllib, dispo nativement à partir de Python 3.11, ou pour Python 3.10 ou inférieur utilise tomli

- Détecte dynamiquement la version de Python
- Utilise tomllib si dispo (Python 3.11+), sinon fallback sur tomli
- Inclut un message d’erreur clair si tomli n’est pas installé en Python < 3.11


