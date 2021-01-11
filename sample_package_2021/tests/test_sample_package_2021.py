"""
Unit and regression test for the sample_package_2021 package.
"""

# Import package, test suite, and other packages as needed
import sample_package_2021 as sp
import pytest
import sys

import numpy as np


@pytest.fixture(scope="function")
def methane_molecule():
    symbols = np.array(["C", "H", "H", "H", "H"])
    coordinates = np.array(
        [[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]]
    )
    return symbols, coordinates

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = sp.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


def test_calculate_angle():
    """Test the calculate_angle function"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_value = 90

    calculated_value = sp.calculate_angle(r1, r2, r3, degrees=True)
    assert expected_value == calculated_value

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = sp.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle), F'{calculated_angle} {expected_angle}'

def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5

def test_build_bond_list(methane_molecule):

    _, coordinates = methane_molecule

    bonds = sp.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_build_bond_list_error():

    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )

    with pytest.raises(ValueError):
        bonds = sp.build_bond_list(coordinates, min_bond=-1)


def test_center_of_mass(methane_molecule):

    symbols, coordinates = methane_molecule

    center_of_mass = sp.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1, 1, 1])

    assert np.array_equal(center_of_mass, expected_center)


def test_molecular_mass(methane_molecule):

    symbols, _ = methane_molecule

    calculated_mass = sp.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass


def test_sample_package_2021_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sample_package_2021" in sys.modules
