import numpy as _np

def eqn_error_matrix(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray:
    # function to return the ndarray A @ X @ B + C @ X @ D - E
    return A @ X @ B + C @ X @ D - E

def eqn_error_norm(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray:
    # function to return the norm of the ndarray A @ X @ B + C @ X @ D - E
    return _np.linalg.norm(A @ X @ B + C @ X @ D - E, ord="fro")
