"""
sample_package_2021
This is a sample repo for the MolSSI Best Practices Workshop - January 2021
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
