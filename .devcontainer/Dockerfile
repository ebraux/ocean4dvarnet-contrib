FROM mambaorg/micromamba:latest  # Utiliser une image de base avec micromamba

# Définir les variables d'environnement
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Installe des packages systèmes ou autres outils nécessaires
RUN apt-get update && apt-get install -y python3-pip

# Crée un environnement Python avec mamba (ou conda si tu préfères)
RUN micromamba create -n dev-env python=3.12