import numpy as np


def generalized_sylvester(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, E: np.ndarray) -> np.ndarray:
    # ToDo: Doc string

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
            E = E.reshape((n,m))
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
        all_is_finite: np.bool = np.all(np.isfinite(A)) and np.all(np.isfinite(B)) and np.all(np.isfinite(C)) and np.all(np.isfinite(D)) and np.all(np.isfinite(E))
    except TypeError:
        raise TypeError("Couldn't check whether all matrix entries are finite. Ensure that A, B, C, D, and E are numeric.")
    # check no inf or nan or empty
    if not all_is_finite:
        raise ValueError("Provided matrices must contain only finite values (no inf, -inf, or NaN).")

    # generate Kron vectorization factor, check that it has non-zero determinant
    kroneckor_vectorization_factor: np.ndarray = np.kron(B.T, A) + np.kron(D.T, C)
    try:
        det: float = float(np.linalg.det(kroneckor_vectorization_factor))
    except ValueError:
        raise ValueError("Couldn't calculate determinant to ensure non-singularity of the problem. Ensure that A, B, C, D, and E are numeric, and ensure that A, B, C, and D are square with shape(A) == shape(C) and shape(B) == shape(D).")
    if det == 0:
        raise ValueError("The problem is singular and a unique solution does not exist.")
    
    # generate vectorized solution and verify consistency
    vecX: np.ndarray = np.linalg.inv(kroneckor_vectorization_factor) @ E.reshape((-1,1))
    
    # reshape to proper solution and return
    try:
        X: np.ndarray = vecX.reshape(E.shape)
    except:
        raise ValueError("Couldn't reshape vectorized solution to be consistent with the equation.")
    return X



def main() -> None:
    # if this runs, print a help blurb
    # ToDo
    print("A module for solve the generalized Sylvester equation AXB + CXD = E for the unknown X.")



if __name__ == "__main__":
    # if this runs, print a help blurb
    main()