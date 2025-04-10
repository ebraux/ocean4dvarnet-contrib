"""
Pytest configuration file for the test suite.

This file ensures that the root directory of the project is added to the
PYTHONPATH, allowing the test suite to import modules from the `scripts` package.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
