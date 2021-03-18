"""
QET-Vib
QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy
"""

# Add imports here
from .qet_vib import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
