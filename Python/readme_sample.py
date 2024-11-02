import numpy as np
import generalized_sylvester as gs
import generalized_sylvester.error as gs_error

A = np.array([[1, 2, 3],[0, 2, 1],[0, 0, 1]])
B = np.array([[1, 0],[2, 1]])
C = np.array([[2, 0, 0],[1, 1, 0],[3, 2, 1]])
D = np.array([[1, 2],[0, 2]])
E = np.array([[4, 1],[0, 0],[1, -2]])

X = gs.solve(A, B, C, D, E)   # solve the generalized sylvester equation AXB + CXD = E for the unknown X

matrices = [A, B, C, D, E, X]
print(gs_error.eqn_error_matrix(*matrices)) # equation error matrix, A @ X @ B + C @ X @ D - E
print(gs_error.eqn_error_norm(*matrices)) # frobenius norm of the equation error