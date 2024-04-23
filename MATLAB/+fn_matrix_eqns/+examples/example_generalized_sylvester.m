
% A simple script demonstrating the usage of generalized_sylvester to datermine a matrix X satisfying the equation AXB + CXD = E

n = 5;
m = 3;
A = rand(n,n)
B = rand(m,m)
C = rand(n,n)
D = rand(m,m)
E = rand(n,m)
X = fn_matrix_eqns.generalized_sylvester(A,B,C,D,E)

disp(strcat('The matrix X satisfies the equation AXB + CXD = E, with error in the Frobenius norm, norm(A*X*B + C*X*D - E, "fro") = ', string(norm(A*X*B + C*X*D - E,"fro"))))

