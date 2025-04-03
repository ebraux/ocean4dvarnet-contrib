# Manage ocean4dVarnet Contributions

- [Tools](./scripts/README.md) : 
- [Contributions](./contrib/README.md)


[![Validate Contributions](https://github.com/ebraux/ocean4dvarnet-contrib/actions/workflows/validate_contrib.yml/badge.svg)](https://github.com/ebraux/ocean4dvarnet-contrib/actions/workflows/validate_contrib.yml)

# Résumé de l'organisation**

1. Structure des contributions : Chaque contribution dans un dossier dédié avec un fichier `metadatas.yml` contenant des informations obligatoires (date, description, contact, etc.).
2. Validation automatique : Utilisation d'un script Python intégré à une CI (GitHub Actions, GitLab CI, etc.) pour valider que les informations obligatoires sont présentes.
3. Génération de la documentation : Utilisation d'un script pour extraire ces informations et les afficher dans un fichier markdown ou directement dans la documentation du projet.
4. Pipeline CI : Automatisation de la validation et de la génération de documentation dans ton pipeline CI.
