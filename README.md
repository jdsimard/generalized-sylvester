# generalized Sylvester

MATLAB and Python/NumPy functions to solve the generalized Sylvester equation

$$AXB + CXD = E,$$

for the matrix $X$, given the matrix $E$ and square matrices $A$, $B$, $C$, and $D$, with $A$ and $C$ the same size and $B$ and $D$ the same size.

See [K. E. Chu, "The Solution of the Matrix Equations AXB - CXD = E and (YA - DZ, YC - BZ) = (E, F)," Linear Algebra and its Applications 93 (1987): 93-105](https://doi.org/10.1016/S0024-3795(87)90314-4), for example.

MATLAB contains the function sylvester which solves a matrix equation of the form $AX + XB = C$, but no such function for solving the generalized Sylvester equation. The included function solves the matrix equation $AXB + CXD = E$ using a naive vectorization approach, so long as a unique solution exists. Because it uses a vectorization approach, it may require the inversion of a large matrix with dimensions $nm \times nm$, where $A$ and $C$ are $n \times n$ matrices and $B$ and $D$ are $m \times m$ matrices, so currently it may not perform well (or as expected) if the dimension becomes large. A future improvement should switch to a generalized eigenvalue / eigenvector approach.

A Python implementation using the NumPy framework is also included.

# Example Usage

Consider matrices

$$A = \begin{bmatrix} 1 & 2 & 3 \\\ 0 & 2 & 1 \\\ 0 & 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 0 \\\ 2 & 1 \end{bmatrix},$$
$$C = \begin{bmatrix} 2 & 0 & 0 \\\ 1 & 1 & 0 \\\ 3 & 2 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 1 & 2 \\\ 0 & 2 \end{bmatrix},$$

and

$$E = \begin{bmatrix} 4 & 1 \\\ 0 & 0 \\\ 1 & -2 \end{bmatrix}.$$

The associated generalized Sylvester equation has the solution

$$X = \begin{bmatrix} 1 & -1 \\\ -2 & 1 \\\ 1 & 0 \end{bmatrix}.$$

## Python

To solve this in Python, ensure the directory 'generalized_sylvester' ('.\Python\generalized_sylvester' in this repo) is found in your Python search path, make sure that NumPy is installed (see '.\Python\env\generalized-sylvester-environment.yml' for a conda environment that can be imported), and run the script
```
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
print(gs_error.eqn_error_norm(*matrices)) # frobenius norm of the equation error, ~3.1244445429724018e-15
```

## MATLAB

To solve this in MATLAB, ensure the directory '+fn_matrix_eqns' ('.\MATLAB\+fn_matrix_eqns' in this repo) is found in your MATLAB path and run
```
A = [1 2 3; 0 2 1; 0 0 1];
B = [1 0; 2 1];
C = [2 0 0; 1 1 0; 3 2 1];
D = [1 2; 0 2];
E = [4, 1; 0, 0; 1, -2];

X = fn_matrix_eqns.generalized_sylvester(A, B, C, D, E);

norm(A*X*B + C*X*D - E, 2)    % ~1.6140e-15
```


# Usage

## Python

The Python implementation contains a YML file to generate a conda environment, along with some batch files for running unit tests and type checking. The implemented module is in ".\Python\generalized_sylvester". Example usage can be found in ".\Python\example_usage.py".

To use the Python implementation as a module, you only need the directory tree at ".\Python\generalized_sylvester". Simply make sure this is in a location that can be found by the Python interpreter, and then you can import the functions via something like
```
import generalized_sylvester as gs
```
and/or
```
import generalized_sylvester.error as gs_error
```

The functions in the generalized_sylvester namespace are
```
# Solve the generalized Sylvester equations.
generalized_sylvester.solve(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray) -> _np.ndarray

# Get the equation error matrix, AXB + CXD - E.
generalized_sylvester.error.eqn_error_matrix(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray

# Get the Frobenius norm of the equation error matrix, AXB + CXD - E.
generalized_sylvester.error.eqn_error_norm(A: _np.ndarray, B: _np.ndarray, C: _np.ndarray, D: _np.ndarray, E: _np.ndarray, X: _np.ndarray) -> _np.ndarray
```

There are a number of pytest unit test cases in '.\Python\generalized_sylvester\test\test_generalized_sylvester.py'.

## MATLAB

All included MATLAB functions and scripts have been included under the namespaces fn_matrix_eqns, fn_matrix_eqns.examples, and fn_matrix_eqns.tests to avoid possible namespace conflicts in the future.

```
% The function for solving the generalized Sylvester equation.
fn_matrix_eqns.generalized_sylvester.m

% A simple script demonstrating usage of fn_matrix_eqns.generalized_sylvester.m.
fn_matrix_eqns.examples.example_generalized_sylvester.m

% A function that runs a variety of unit test cases on fn_matrix_eqns.generalized_sylvester.m.
fn_matrix_eqns.tests.run_tests_generalized_sylvester.m

% A script that runs test cases for included functions.
fn_matrix_eqns.tests.run_all_tests.m
```
