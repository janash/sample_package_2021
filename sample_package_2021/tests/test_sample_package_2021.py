"""
Unit and regression test for the sample_package_2021 package.
"""

# Import package, test suite, and other packages as needed
import sample_package_2021
import pytest
import sys

def test_sample_package_2021_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sample_package_2021" in sys.modules
