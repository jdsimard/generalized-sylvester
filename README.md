# generalized-sylvester
A MATLAB function to solve the generalized Sylvester equation

$$AXB + CXD = E$$

MATLAB contains the function sylvester which solves a matrix equation of the form $AX + XB = C$, but no such function for solving the generalized Sylvester equation. The included function solves the matrix equation $AXB + CXD = E$ using a vectorization approach, so long as a unique solution exists. Because it uses a vectorization approach, it may require the inversion of a large matrix with dimensions $nm \times nm$, where $A$ and $C$ are $n \times n$ matrices and $B$ and $D$ are $m \times m$ matrices, so currently it may not perform well (or as expected) if the dimension becomes large. A future improvement should switch to a generalized eigenvalue / eigenvector approach.

All included functions and scripts have been included under the namespaces fn_matrix_eqns, fn_matrix_eqns.examples, and fn_matrix_eqns.tests to avoid possible namespace conflicts in the future.



Project guide:

fn_matrix_eqns.generalized_sylvester.m
- the function for solving the generalized Sylvester equation;

fn_matrix_eqns.examples.example_generalized_sylvester.m
- a simple script demonstrating usage of fn_matrix_eqns.generalized_sylvester.m;

fn_matrix_eqns.tests.run_tests_generalized_sylvester.m
- a function that runs a variety of unit test cases on fn_matrix_eqns.generalized_sylvester.m, confirming expected failures and that solutions actually satisfy the matrix equation;

fn_matrix_eqns.tests.run_all_tests.m
- a script that runs test cases for included functions; included as a "test everything" script for if I implement functions for more general matrix equations;
