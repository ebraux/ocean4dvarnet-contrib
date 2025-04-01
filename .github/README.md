Worflow


- `validate_contrib` :
    - s'execute à chaque à chaque  à chaque `push` ou `pull_request`. 
    - uniquement si le contenu du dossier `contrib/` est modifié
- `deploy`:
    - s'execute à chaque  à chaque `push` ou `pull_request`.
    - ne s'execute pas si `validate_contrib` est en erreur.



Mis en place d'une logique conditionnelle pour exécuter `deploy` directement pour tous les `push` et `pull_request`, sauf si le dossier `contrib` est modifié. Dans ce cas, `deploy` dépendra de la réussite de `validate_contrib`.


1. **Déclencheurs** :
   - `push` : Le workflow `deploy` s'exécute pour chaque `push` sur `main`.
   - `pull_request` : Le workflow `deploy` s'exécute pour chaque `pull_request` sur `main`.
   - `workflow_run` : Le workflow `deploy` s'exécute après `validate_contrib` si ce dernier réussit.

2. **Condition `if`** :
   - Si le workflow est déclenché par un `workflow_run` (après `validate_contrib`), il vérifie que `validate_contrib` a réussi (`workflow_run.conclusion == 'success'`).
   - Sinon, il s'exécute directement pour les autres événements (`push` ou `pull_request`).

Avec cette configuration :
- `deploy` s'exécute pour tous les `push` et `pull_request`.
- Si le dossier `contrib` est modifié, `validate_contrib` est exécuté en premier, et `deploy` ne s'exécute que si `validate_contrib` réussit.


---
## test-and-lint

Tu veux mettre en place une **CI GitHub Actions** qui :  
✅ **Exécute `pylint` et `pytest` sur chaque sous-dossier de `contrib/`**  
✅ **Ne déclenche les tests que si le sous-dossier a été modifié**  
✅ **Stocke les résultats individuellement pour générer des badges**  

---

### 🛠 **1. Organisation du Dossier**
Ton projet ressemble à ceci :  
```
ocean4dvarnet-contrib/
│── contrib/
│   ├── projet_A/
│   │   ├── tests/    # Tests pour projet_A
│   │   ├── module_A.py
│   ├── projet_B/
│   │   ├── tests/    # Tests pour projet_B
│   │   ├── module_B.py
│   ├── ...
│── .github/workflows/
│   ├── ci.yml        # Workflow GitHub Actions
```

---


---

### 📌 **3. Comment Ça Fonctionne ?**
1. 🔍 **Détecte les changements** dans `contrib/` et identifie les sous-dossiers impactés  
2. 🔄 **Déclenche des jobs indépendants** pour chaque dossier modifié  
3. ✅ **Exécute `pylint` et `pytest` seulement sur les dossiers concernés**  
4. 📂 **Stocke les résultats (`.json` et `.xml`)** pour générer des badges  

---

### 🏅 **4. Générer des Badges**
Tu peux ajouter des badges dans `README.md` en utilisant [shields.io](https://shields.io) :

#### ✅ **Badge Pytest (via GitHub Actions)**
Ajoute ceci dans **README.md** :
```md
![Pytest](https://github.com/ebraux/ocean4dvarnet-contrib/actions/workflows/ci.yml/badge.svg)
```

#### ✅ **Badge Pylint (via Shields.io + Upload des Scores)**
Tu peux aussi **publier le score Pylint** dans un fichier (`pylint-score.txt`) et utiliser une **GitHub Action spécifique** pour l'extraire.

---

### 🎯 **Avantages de cette Approche**
✅ **Se lance uniquement si nécessaire**  
✅ **Exécute `pytest` et `pylint` indépendamment pour chaque projet**  
✅ **Stocke des résultats exploitables pour des badges et des stats**  

---

### ❓ **Besoin d'aide pour générer les badges automatiquement ?** 😊