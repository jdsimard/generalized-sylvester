# Created by Joel D. Simard

import numpy as _np

def eqn_error_matrix(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray:
    """Return the ndarray A @ X @ B + C @ X @ D - E.

    Given A, B, C, D, E, and X, each satisfying the conditions of generalized_sylvester.solve(...), return the numpy.ndarray representing the equation error, A @ X @ B + C @ X @ D - E.

    Args:
        A: a square numpy.ndarray with shape (1,) or (n,n,), with entries satisfying numpy.isfinite.
        B: a square numpy.ndarray with shape (1,) or (m,m,), with entries satisfying numpy.isfinite.
        C: a square numpy.ndarray with C.shape == A.shape, with entries satisfying numpy.isfinite.
        D: a square numpy.ndarray with D.shape == B.shape, with entries satisfying numpy.isfinite.
        E: a numpy.ndarray with E.shape == (n,m,) (or (1,) if A/B/C/D.shape = (1,)), with entries satisfying numpy.isfinite.
        X: a numpy.ndarray, X, with X.shape == (n,m,) 

    Returns:
        The numpy.ndarray A @ X @ B + C @ X @ D - E.
    """
    return A @ X @ B + C @ X @ D - E

def eqn_error_norm(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray:
    """Return the Frobenius norm of the ndarray A @ X @ B + C @ X @ D - E.

    Given A, B, C, D, E, and X, each satisfying the conditions of generalized_sylvester.solve(...), return the Frobenius norm of the numpy.ndarray representing the equation error, A @ X @ B + C @ X @ D - E.

    Args:
        A: a square numpy.ndarray with shape (1,) or (n,n,), with entries satisfying numpy.isfinite.
        B: a square numpy.ndarray with shape (1,) or (m,m,), with entries satisfying numpy.isfinite.
        C: a square numpy.ndarray with C.shape == A.shape, with entries satisfying numpy.isfinite.
        D: a square numpy.ndarray with D.shape == B.shape, with entries satisfying numpy.isfinite.
        E: a numpy.ndarray with E.shape == (n,m,) (or (1,) if A/B/C/D.shape = (1,)), with entries satisfying numpy.isfinite.
        X: a numpy.ndarray, X, with X.shape == (n,m,) 

    Returns:
        The Frobenius norm of the numpy.ndarray A @ X @ B + C @ X @ D - E.
    """
    return _np.linalg.norm(A @ X @ B + C @ X @ D - E, ord="fro")
