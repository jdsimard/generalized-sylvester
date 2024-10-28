import numpy as np
from generalized_sylvester import generalized_sylvester

# A and C will be 4x4
# B and D will be 2x2
# -> E and X will be 4x2
n, m = 4, 2

# generate a matrix of size n1xn2 with entries uniformly distributed in [-10,10)
rand_mat = lambda n1, n2: 20*(np.random.random_sample((n1,n2)) - 0.5)

A, B, C, D, E = rand_mat(n,n), rand_mat(m,m), rand_mat(n,n), rand_mat(m,m), rand_mat(n,m)

print(f"A = {A}", f"B = {B}", f"C = {C}", f"D = {D}", f"E = {E}", sep="\n\n")

X = generalized_sylvester(A, B, C, D, E)
print(f"\n-> X = {X}")

eqn_error = A @ X @ B + C @ X @ D - E
print(f"\nSolution error matrix:\nAXB + CXD - E\n= {eqn_error}")
print(f"\nSolution error norm:\nfrob_norm(AXB + CXD - E) = {np.linalg.norm(eqn_error, ord="fro")}")