"""
Pytest configuration file for the test suite.

This file ensures that the root directory of the project is added to the
PYTHONPATH, allowing the test suite to import modules from the `scripts` package.
"""

import sys
from pathlib import Path

# Ajouter le répertoire racine du projet au PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
