function [X] = generalized_sylvester(A,B,C,D,E)
%GENERALIZED_SYLVESTER X = generalized_sylvester(A,B,C,D,E) returns the
%solution X to the matrix equation AXB + CXD = E, if it exists
%   
%   Returns the solution X to the matrix equation AXB + CXD = E where A and
%       C are square matrices of dimension n times n, B and D are square
%       matrices of dimension m times m, and E is a matrix of dimension
%       n times m, so long as such a solution exists and is unique.
%
%   INPUTS
%   A,C: square matrices of dimension n times n, such that (A,C) form a
%       regular matrix pencil;
%   B,D: square matrices of dimension m times m, such that (B,D) form a
%       regular matrix pencil, and the generalized eigenvalues of (A,C) and
%       (-B,D) are disjoint;
%   E: a matrix of dimension n times m;
%
%   OUTPUTS
%   X: a matrix of dimension n times m satisfying AXB + CXD = E;
    
    % Get dimensions of the matrices A and B. These will be used to validate consistency of all inputs A, B, C, D, and E.
    n = length(A);
    m = length(B);

    % All inputs must be numeric
    % A and C must be square matrices of the same size 
    % B and D must be square matrices of the same size
    % E must be a matrix with number of rows being the same as A and C,
    % and number of columns being the same as B and D
    required_classes = {'numeric'};
    required_attributes_A_C = {'nonempty','finite','nonnan','square','size',[n,n]};
    required_attributes_B_D = {'nonempty','finite','nonnan','square','size',[m,m]};
    required_attributes_E = {'nonempty','finite','nonnan','size',[n,m]};
    
    % Validate the properties described above
    validateattributes(A,required_classes,required_attributes_A_C,'','A',1);
    validateattributes(B,required_classes,required_attributes_B_D,'','B',2);
    validateattributes(C,required_classes,required_attributes_A_C,'','C',3);
    validateattributes(D,required_classes,required_attributes_B_D,'','D',4);
    validateattributes(E,required_classes,required_attributes_E,'','E',5);

    % NOTE ON OBTAINING THE SOLUTION: Here I use a vectorization approach to easily determine the solution. However, this approach requires inverting a nm times nm matrix, which could be problematic for large problems. To avoid this, a generalized eigenvalue/eigenvector approach should be implemented in the future.
    % To do this, add a check for regularity and disjoint generalized spectra of the matrix penxils (A + x C), (D - x B), then apply generalized eigenvectors to calculate X element by element.

    % Calculate the vectorization of the solution X by using the kronecker product (for any matrices A, B, C, vec(A*B*C) = kron(transpose(C),A)*vec(B))
    kronecker_vectorization_factor = kron(transpose(B),A) + kron(transpose(D),C);
    
    % Before trying to calculate the inverse, check that it is invertible. If it is not invertible, then there does not exist a unique solution to the generalized Sylvester equation (there is either no solution, or there is an infinite set solutions)
    validateattributes(det(kronecker_vectorization_factor),required_classes,{'nonempty','finite','nonnan','nonzero'},'','the determinant of the Kronecker vectorization factor (required to be invertible for the existence of a unique solution to the generalized Sylvester equation)');
    vecX = kronecker_vectorization_factor\E(:);
    
    % Check that vec(X) is acceptable before reshaping (numeric, nonempty, finite, nonnan, and has size [n*m,1])
    required_attributes_vecX = {'nonempty','finite','nonnan','size',[n*m,1]};
    validateattributes(vecX,required_classes,required_attributes_vecX,'','the solution to the generalized Sylvester equation, X,');
    
    % Reshape vec(X) into the n times m matrix X
    X = reshape(vecX,n,m);
end