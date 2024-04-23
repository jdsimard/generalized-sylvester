function [results] = run_tests_generalized_sylvester(num_solution_comparisons,solution_error_tolerance)
%RUN_TESTS_GENERALIZED_SYLVESTER
%results = run_tests_generalized_sylvester(num_solution_comparisons,solution_error_tolerance)
%tests that the function generalized_sylvester is throwing errors when
%necessary, and calculating solutions correctly
%
%   Checks the function for input argument properties that should give
%       errors: empty, non-numeric, infinite, NaN, non-square (A,B,C,D),
%       size consistency (A/C, B/D, and E), non-invertibility of the
%       kronecker vectorization factor when the input matrices are known
%       to be irregular;
%   
%   Further checks that obtained solutions actually satisfy the equation
%       (num_solution_comparisons times, with an error tolerance of
%       solution_error_tolerance) and that using an incorrect solution via
%       flipping the sign of E does not satisfy the equation
%       (num_solution_comparisons times, with an error tolerance of
%       solution_error_tolerance);
%   
%   INPUTS
%   num_solution_comparisons: the number of times to check that a solution
%       satisfies the equation, and the number of times to check that an
%       incorrect solution does not satisfy the equation;
%   solution_error_tolerance: the acceptable error tolerance, i.e. a
%       solution X is considered correct if it satisfies
%       norm(AXB + CXD - E,"fro") < solution_error_tolerance;
%
%   OUTPUTS
%   results: a 2-element cell, where the the ith element of results{1}
%       contains a string describing the ith test, and the ith element of
%       results{2} contains logical 1 if the ith test passed and logical 0
%       if the ith test failed;
    
    num_args = 5;
    
    test_run = [];
    test_result = [];

    % Test for empty input arguments
    for i1 = 1 : 1 : num_args
        input_args = {1,1,1,1,1};
        input_args{i1} = [];
        test_run = [test_run; strcat('Caught empty arg ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:expectedNonempty')
                test_result(end) = true;
            end
        end
    end

    % Test for nonnumeric
    for i1 = 1 : 1 : num_args
        input_args = {1,1,1,1,1};
        input_args{i1} = 'test';
        test_run = [test_run; strcat('Caught non-numeric arg ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:invalidType')
                test_result(end) = true;
            end
        end
    end

    % Test for infinite
    for i1 = 1 : 1 : num_args
        input_args = {1,1,1,1,1};
        input_args{i1} = Inf;
        test_run = [test_run; strcat('Caught Inf arg ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:expectedFinite')
                test_result(end) = true;
            end
        end
    end

    % Test for NaN
    for i1 = 1 : 1 : num_args
        input_args = {1,1,1,1,1};
        input_args{i1} = NaN;
        test_run = [test_run; strcat('Caught NaN arg ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:expectedFinite')
                test_result(end) = true;
            end
        end
    end

    % Test for not square
    for i1 = 1 : 1 : num_args-1
        input_args = {1,1,1,1,1};
        input_args{i1} = [1 1];
        test_run = [test_run; strcat('Caught non-square arg ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:expectedSquare')
                test_result(end) = true;
            end
        end
    end

    % Test for A C / B D inconsistency
    Mat1 = {rand(2,2), rand(3,3)};
    Mat2 = {rand(3,3), rand(2,2)};
    Mat3 = {rand(2,3), rand(3,2)};
    for i1 = 1 : 1 : 2
        input_args = {Mat1{i1},Mat2{i1},Mat2{i1},Mat2{i1},Mat3{i1}};
        test_run = [test_run; strcat('Caught inconsistent arg A C ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:incorrectSize')
                test_result(end) = true;
            end
        end
        input_args = {Mat1{i1},Mat1{i1},Mat1{i1},Mat2{i1},Mat3{i1}};
        test_run = [test_run; strcat('Caught inconsistent arg B D ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier,'MATLAB:incorrectSize')
                test_result(end) = true;
            end
        end
    end

    % Test for E inconsistency
    Mat1 = {rand(2,2), rand(3,3)};
    Mat2 = {rand(3,3), rand(2,2)};
    Mat3 = {rand(3,2), rand(2,2)};
    for i1 = 1 : 1 : 2
        input_args = {Mat1{i1},Mat2{i1},Mat1{i1},Mat2{i1},Mat3{i1}};
        test_run = [test_run; strcat('Caught inconsistent arg E ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier, 'MATLAB:incorrectSize')
                test_result(end) = true;
            end
        end
    end

    % Test for irregularity / all arguments good, but solution doesn't
    % exist or is not unique
    MatA = {zeros(3,3), [0 1; 0 0]};
    MatB = {rand(2,2), rand(3,3)};
    MatC = {zeros(3,3), [1 0; 0 0]};
    MatD = {rand(2,2), rand(3,3)};
    MatE = {rand(3,2), rand(2,3)};
    for i1 = 1 : 1 : 2
        input_args = {MatA{i1},MatB{i1},MatC{i1},MatD{i1},MatE{i1}};
        test_run = [test_run; strcat('Caught irregular pair A C ',string(i1))];
        test_result = [test_result; false];
        try
            X = fn_matrix_eqns.generalized_sylvester(input_args{1},input_args{2},input_args{3},input_args{4},input_args{5});
        catch exc
            %disp(exc.identifier)
            if strcmp(exc.identifier, 'MATLAB:expectedNonZero')
                test_result(end) = true;
            end
        end
    end

    % Test that solutions satisfy the equation
    err_tolerance = solution_error_tolerance;
    num_test_cases = num_solution_comparisons;
    test_cases_passed = 0;
    for i1 = 1 : 1 : num_test_cases
        n = randi(10,1);
        m = randi(10,1);
        A = rand(n,n);
        B = rand(m,m);
        C = rand(n,n);
        D = rand(m,m);
        E = rand(n,m);
        X = fn_matrix_eqns.generalized_sylvester(A,B,C,D,E);
        if norm(A*X*B + C*X*D - E,"fro") < err_tolerance
            test_cases_passed = test_cases_passed + 1;
        end
    end
    test_run = [test_run; strcat('Calculated solution satisfies equation in (',string(test_cases_passed),') out of (',string(num_test_cases),') trials, with error tolerance in Frobenius norm: ',string(err_tolerance))];
    test_result = [test_result; test_cases_passed == num_test_cases];

    % Test for results that are not solutions satisfying the equation
    err_tolerance = solution_error_tolerance;
    num_test_cases = num_solution_comparisons;
    test_cases_passed = 0;
    for i1 = 1 : 1 : num_test_cases
        n = randi(10,1);
        m = randi(10,1);
        A = rand(n,n);
        B = rand(m,m);
        C = rand(n,n);
        D = rand(m,m);
        E = rand(n,m);
        X = fn_matrix_eqns.generalized_sylvester(A,B,C,D,E);
        E = -E;
        if norm(A*X*B + C*X*D - E,"fro") > err_tolerance
            test_cases_passed = test_cases_passed + 1;
        end
    end
    test_run = [test_run; strcat('Checked that -X (sign-flipped) does not satisfy the equation in (',string(test_cases_passed),') out of (',string(num_test_cases),') trials, with error tolerance in Frobenius norm: ',string(err_tolerance))];
    test_result = [test_result; test_cases_passed == num_test_cases];

    results = {test_run,test_result};
end