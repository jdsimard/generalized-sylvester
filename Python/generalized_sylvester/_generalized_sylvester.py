# Created by Joel D. Simard

import numpy as _np


def solve(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray) -> _np.ndarray:
    """Solve the generalized Sylvester equation, AXB + CXD = E, for the matrix X.

    Given A, B, C, D, and E, each a numpy.ndarray with ndim == 1 or 2, and having consistent dimensions, return the numpy.ndarray that solves the matrix equation A @ X @ B + C @ X @ D == E. An argument can only have ndim == 1 if it is a scalar, i.e. ndim == 1 and size == 1.

    Args:
        A: a square numpy.ndarray with shape (1,) or (n,n,), with entries satisfying numpy.isfinite.
        B: a square numpy.ndarray with shape (1,) or (m,m,), with entries satisfying numpy.isfinite.
        C: a square numpy.ndarray with C.shape == A.shape, with entries satisfying numpy.isfinite.
        D: a square numpy.ndarray with D.shape == B.shape, with entries satisfying numpy.isfinite.
        E: a numpy.ndarray with E.shape == (n,m,) (or (1,) if A/B/C/D.shape = (1,)), with entries satisfying numpy.isfinite.

    Returns:
        A numpy.ndarray, X, with X.shape == (n,m,), that satisfies A @ X @ B + C @ X @ D == E.

    Raises:
        ValueError: A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1].
        ValueError: A and C must be the same shape, and B and D must be the same shape.
        ValueError: E must be either a 1darray or 2darray with consistent shape.
        ValueError: Provided matrices must contain only finite values (no inf, -inf, or NaN).
        ValueError: Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D).
        ValueError: The problem is singular and a unique solution does not exist.
        ValueError: Couldn't reshape vectorized solution to be consistent with the equation.
        TypeError: Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric.
    """

    # make sure that A, B, C, D are square 2darray
    square_matrices = [A, B, C, D]
    # doing arr = arr.reshape((1,1)) in the loop only changes the arr variable locally, and not in the list, so we need to enumerate so that we can reshape the actual matrix in the list
    for i, arr in enumerate(square_matrices):
        if arr.ndim == 1:
            if arr.size == 1:
                square_matrices[i] = arr.reshape((1,1))
            else:
                raise ValueError("A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1].")
        elif arr.ndim == 2:
            n, m = arr.shape
            if n != m:
                raise ValueError("A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1].")
        else:
            raise ValueError("A, B, C, D must be square matrices: either 1) 1darray with arr.size == 1, or 2) 2darray with arr.shape[0] == arr.shape[1].")
    A, B, C, D = square_matrices[0], square_matrices[1], square_matrices[2], square_matrices[3]
    # now everything except E should be square 2darray, including scalar 1darray values that have been cast to 2darray

    # A and C should have the same shape, B and D should have the same shape
    if not A.shape == C.shape or not B.shape == D.shape:
        raise ValueError("A and C must be the same shape, and B and D must be the same shape.")
    
    # E shape should be consistent with A, B, C, D shape
    n, _ = A.shape
    m, _ = B.shape
    if E.ndim == 1:
        try:
            E = E.reshape((n,m), order='F')
        except:
            raise ValueError("E must be either a 1darray or 2darray with consistent shape.")
    elif E.ndim == 2:
        if E.shape != (n,m):
            raise ValueError("E must be either a 1darray or 2darray with consistent shape.")
    else:
        raise ValueError("E must be either a 1darray or 2darray with consistent shape.")
    # all of A,B,C,D,E should now be 2darrays with consistent sizes, A,B,C,D square, A,C same size, and B,D same size

    # check for finiteness (no inf, -inf, or NaN)
    # check 'isfinite' can be used
    try:
        all_is_finite: _np.bool = _np.all(_np.isfinite(A)) and _np.all(_np.isfinite(B)) and _np.all(_np.isfinite(C)) and _np.all(_np.isfinite(D)) and _np.all(_np.isfinite(E))
    except TypeError:
        raise TypeError("Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric.")
    # check no inf or nan or empty
    if not all_is_finite:
        raise ValueError("Provided matrices must contain only finite values (no inf, -inf, or NaN).")

    # generate Kron vectorization factor, check that it has non-zero determinant
    kroneckor_vectorization_factor: _np.ndarray = _np.kron(B.T, A) + _np.kron(D.T, C)
    try:
        det: float = float(_np.linalg.det(kroneckor_vectorization_factor))
    except ValueError:
        raise ValueError("Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D).")
    if det == 0:
        raise ValueError("The problem is singular and a unique solution does not exist.")
    
    # generate vectorized solution and verify consistency
    # note: need to use Fortran-like indexing (order='F') rather than C-like indexing so that reshape does the traditional/mathematical vectorization operation on E
    vecX: _np.ndarray = _np.linalg.inv(kroneckor_vectorization_factor) @ E.reshape((-1,1), order='F')

    # reshape to proper solution and return
    try:
        # note: need to use Fortran-like indexing (order='F') rather than C-like indexing so that reshape correctly undoes the previous vectorization on E, for X
        X: _np.ndarray = vecX.reshape(E.shape, order='F')
    except:
        raise ValueError("Couldn't reshape vectorized solution to be consistent with the equation.")
    return X



def main() -> None:
    # ToDo help(module)
    print("A module for solving the generalized Sylvester equation AXB + CXD = E for the unknown X.")



if __name__ == "__main__":
    main()