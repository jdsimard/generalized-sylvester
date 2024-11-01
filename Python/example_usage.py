# Created by Joel D. Simard

import numpy as np
import generalized_sylvester as gs
import generalized_sylvester.error as gs_error

# A and C will be 4x4
# B and D will be 2x2
# -> E and X will be 4x2
n, m = 4, 2




# generate random matrices of size n1xn2 with entries uniformly distributed in [-10,10)
rand_mat = lambda n1, n2: 20*(np.random.random_sample((n1,n2)) - 0.5)
A, B, C, D, E = rand_mat(n,n), rand_mat(m,m), rand_mat(n,n), rand_mat(m,m), rand_mat(n,m)
print(f"A = {A}", f"B = {B}", f"C = {C}", f"D = {D}", f"E = {E}", sep="\n\n")




# solve the generalized sylvester equation AXB + CXD = E for the unknown X
X = gs.solve(A, B, C, D, E)
print(f"\n-> X = {X}")


matrices = [A, B, C, D, E, X]

# get the equation error matrix, A @ X @ B + C @ X @ D - E
eqn_error_mat = gs_error.eqn_error_matrix(*matrices)
print(f"\nSolution error matrix:\nAXB + CXD - E\n= {eqn_error_mat}")

# get the frobenius norm of the equation error matrix
eqn_error_norm = gs_error.eqn_error_norm(*matrices)
print(f"\nSolution error norm:\nfrob_norm(AXB + CXD - E) = {eqn_error_norm}")
