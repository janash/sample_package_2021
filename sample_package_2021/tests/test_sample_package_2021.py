"""
Unit and regression test for the sample_package_2021 package.
"""

# Import package, test suite, and other packages as needed
import sample_package_2021 as sp
import pytest
import sys

import numpy as np


def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = sp.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance





def test_sample_package_2021_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sample_package_2021" in sys.modules
