import numpy as np


def generalized_sylvester(A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, E: np.ndarray) -> np.ndarray:
    # check consistency of matrix dimensions
    # check no inf or nan or empty
    # generate Kron vectorization factor, check that it has non-zero determinant
    kroneckor_vectorization_factor: np.ndarray = np.kron(B.transpose(), A) + np.kron(D.transpose(), C)
    det: float = np.linalg.det(kroneckor_vectorization_factor)
    # generate vectorized solution and verify consistency
    vecX: np.ndarray = np.linalg.inv(kroneckor_vectorization_factor) @ E.reshape((-1,1))
    # reshape to proper solution and return
    X: np.ndarray = vecX.reshape(E.shape)
    return X

def main() -> None:
    # if this runs, print a help blurb
    print("A module for solve the generalized Sylvester equation AXB + CXD = E for the unknown X.")

if __name__ == "__main__":
    # if this runs, print a help blurb
    main()