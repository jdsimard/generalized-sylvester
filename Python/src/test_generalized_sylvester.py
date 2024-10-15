import generalized_sylvester as gs
import pytest
import numpy as np

# test for empty args

def test_empty_args() -> None:
    pass

# test for non-numeric
def test_non_numeric() -> None:
    pass

# test for inf
def test_inf() -> None:
    pass

# test for NaN
def test_nan() -> None:
    pass

# test for non-square
def test_non_square() -> None:
    pass

# test for A C / B D inconsistency
def test_AC_BD_inconsistency() -> None:
    pass

# test for E inconsistency
def test_E_inconsistency() -> None:
    pass

# test for irregularity / all arguments good, but solution doesn't exist or is not unique
def test_irregularity() -> None:
    pass

# test that solutions satisfy the equation
def test_correct_solutions() -> None:
    assert gs.generalized_sylvester(np.array([[1]]), np.array([[1]]), np.array([[1]]), np.array([[1]]), np.array([[4]])) == np.array([[2]])
    



