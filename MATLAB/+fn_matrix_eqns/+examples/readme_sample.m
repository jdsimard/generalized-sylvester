A = [1 2 3; 0 2 1; 0 0 1]
B = [1 0; 2 1]
C = [2 0 0; 1 1 0; 3 2 1]
D = [1 2; 0 2]
E = [4, 1; 0, 0; 1, -2]

X = fn_matrix_eqns.generalized_sylvester(A, B, C, D, E)

A*X*B + C*X*D
norm(A*X*B + C*X*D - E, 2)

