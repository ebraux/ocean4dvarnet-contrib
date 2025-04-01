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

The the `github.event.before` might not exist in the repository. This can happen if the event triggering the workflow (e.g., a push) is the first commit in the branch or if the branch was created without a prior commit.

To fix this, we can add a fallback mechanism to handle cases where `github.event.before` is invalid. If `github.event.before` is not a valid commit, we can use the initial commit of the branch or compare against the default branch.

### [test-and-lint.yml](file:///home/ebraux/_LOCAL/mee/ocean4dvarnet-contrib/.github/workflows/test-and-lint.yml)

Update the `Detect changed folders` step to handle invalid `github.event.before` values.

````yaml
# ...existing code...
      - name: Detect changed folders
        id: get-changes
        run: |
          echo "Detecting changed folders..."
          BEFORE_COMMIT=${{ github.event.before }}
          if ! git cat-file -e $BEFORE_COMMIT 2>/dev/null; then
            echo "Invalid 'before' commit. Using the default branch as the base."
            BEFORE_COMMIT=$(git rev-parse origin/${{ github.event.repository.default_branch }})
          fi
          CHANGED_FOLDERS=$(git diff --name-only $BEFORE_COMMIT ${{ github.sha }} | grep '^contrib/' | cut -d'/' -f2 | sort | uniq)
          echo "Changed folders: $CHANGED_FOLDERS"
          echo "::set-output name=folders::[$(echo $CHANGED_FOLDERS | jq -R -s -c 'split(\"\\n\") | map(select(. != \"\"))')]"
# ...existing code...
````

### Explanation of Changes:
1. **Fallback for `github.event.before`:** 
   - Check if `github.event.before` is a valid commit using `git cat-file -e`.
   - If invalid, fallback to the default branch's latest commit (`origin/${{ github.event.repository.default_branch }}`).

2. **Ensure Robustness:**
   - This ensures the workflow works even for the first commit in a branch or when `github.event.before` is unavailable.

Made changes.