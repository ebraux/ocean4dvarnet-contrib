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

- Job detect-changes :
    - Ce job détecte les sous-dossiers modifiés dans contrib en comparant les commits.
    - Il utilise git diff pour lister les fichiers modifiés, extrait les noms des sous-dossiers et les passe au job suivant via set-output.

- Job test-and-lint :
    - Ce job dépend de detect-changes et utilise les sous-dossiers détectés comme matrice pour exécuter les tests et l'analyse de linting.