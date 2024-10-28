import pytest
from generalized_sylvester import generalized_sylvester
import numpy as np






# test for empty arrays
def test_empty_args() -> None:
    A = np.array([])
    B, C, D, E = np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."
    A = np.eye(2)
    B = np.array([])
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."
    B = np.eye(3)
    C = np.array([])
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."
    C = np.eye(2)
    D = np.array([])
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."
    D = np.eye(3)
    E = np.array([])
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "E must be either a 1darray or 2darray with consistent shape."



# check that 1darrays with size > 1 raise errors
def test_bad_1darray() -> None:
    A, B, C, D, E = np.array([1,1]), np.eye(3), np.eye(1), np.eye(3), 2*np.ones((1,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."




# test for non-numeric entries
def test_non_numeric() -> None:
    A = np.array([['a','b'],['c','d']])
    B, C, D, E = np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    with pytest.raises((TypeError, ValueError)) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    if excinfo.type == TypeError:
        assert excinfo.value.args[0] == "Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric."
    elif excinfo.type == ValueError:
        assert excinfo.value.args[0] == "Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D)."
    A = np.eye(2)
    B = np.array([['a','b','c'],['d','e','f'],['g','h','i']])
    with pytest.raises((TypeError, ValueError)) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    if excinfo.type == TypeError:
        assert excinfo.value.args[0] == "Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric."
    elif excinfo.type == ValueError:
        assert excinfo.value.args[0] == "Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D)."
    B = np.eye(3)
    C = np.array([['a','b'],['c','d']])
    with pytest.raises((TypeError, ValueError)) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    if excinfo.type == TypeError:
        assert excinfo.value.args[0] == "Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric."
    elif excinfo.type == ValueError:
        assert excinfo.value.args[0] == "Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D)."
    C = np.eye(2)
    D = np.array([['a','b','c'],['d','e','f'],['g','h','i']])
    with pytest.raises((TypeError, ValueError)) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    if excinfo.type == TypeError:
        assert excinfo.value.args[0] == "Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric."
    elif excinfo.type == ValueError:
        assert excinfo.value.args[0] == "Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D)."
    D = np.eye(3)
    E = np.array([['a','b','c'],['d','e','f']])
    with pytest.raises((TypeError, ValueError)) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    if excinfo.type == TypeError:
        assert excinfo.value.args[0] == "Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric."
    elif excinfo.type == ValueError:
        assert excinfo.value.args[0] == "Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D)."
    






# test for inf/-inf and NaN
def test_inf_or_NaN_A() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    A[0,0] = np.nan
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    A = np.eye(2)
    A[1,1] = np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    A = np.eye(2)
    A[0,1] = -np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."

def test_inf_or_NaN_B() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    B[0,0] = np.nan
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    B = np.eye(3)
    B[1,1] = np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    B = np.eye(3)
    B[0,1] = -np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."

def test_inf_or_NaN_C() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    C[0,0] = np.nan
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    C = np.eye(2)
    C[1,1] = np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    C = np.eye(2)
    C[0,1] = -np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."

def test_inf_or_NaN_D() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    D[0,0] = np.nan
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    D = np.eye(3)
    D[1,1] = np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    D = np.eye(3)
    D[0,1] = -np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."

def test_inf_or_NaN_E() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((2,3))
    E[0,0] = np.nan
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    E = 2*np.ones((2,3))
    E[1,1] = np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."
    E = 2*np.ones((2,3))
    E[0,1] = -np.inf
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A,B,C,D,E)
    assert excinfo.value.args[0] == "Provided matrices must contain only finite values (no inf, -inf, or NaN)."





# test for non-square A, B, C, and D
def test_non_square() -> None:
    A, B, C, D, E = np.ones((2,1)), np.eye(3), np.ones((2,1)), np.eye(3), 2*np.ones((2,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A, B, C, D, E)
    assert excinfo.value.args[0] == "A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1]."

# test for A C / B D inconsistency
def test_AC_BD_inconsistency() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(3), np.eye(3), 2*np.ones((2,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A, B, C, D, E)
    assert excinfo.value.args[0] == "A and C must be the same shape, and B and D must be the same shape."
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(4), 2*np.ones((2,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A, B, C, D, E)
    assert excinfo.value.args[0] == "A and C must be the same shape, and B and D must be the same shape."

# test for E inconsistency
def test_E_inconsistency() -> None:
    A, B, C, D, E = np.eye(2), np.eye(3), np.eye(2), np.eye(3), 2*np.ones((3,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A, B, C, D, E)
    assert excinfo.value.args[0] == "E must be either a 1darray or 2darray with consistent shape."

# test for irregularity / all arguments good, but solution doesn't exist or is not unique
def test_irregularity() -> None:
    A, B, C, D, E = np.zeros((2,2)), np.zeros((3,3)), np.zeros((2,2)), np.zeros((3,3)), 2*np.ones((2,3))
    with pytest.raises(ValueError) as excinfo:
        generalized_sylvester(A, B, C, D, E)
    assert excinfo.value.args[0] == "The problem is singular and a unique solution does not exist."









# test that solutions satisfy the equation
def test_correct_solutions() -> None:
    assert generalized_sylvester(np.array([1]), np.array([[1]]), np.array([[1]]), np.array([[1]]), np.array([4])) == np.array([[2]])
    assert np.all(generalized_sylvester(np.eye(2), np.eye(3), np.eye(2), np.eye(3), np.ones((2,3)) * 2) == np.ones((2,3)))
    # test coercing 1darrays into 2darrays
    



