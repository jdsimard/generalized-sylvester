
% A script to run test cases on functions in the project

% number of times to test if a calculated solution satisfies the equation, and number of times to test if an incorrect matrix doesn't satisfy the equation, to the defined error tolerance
num_test_cases = 1000;
err_tolerance = 1e-8;

% run tests on generalized_sylvester
results_generalized_sylvester = fn_matrix_eqns.tests.run_tests_generalized_sylvester(num_test_cases,err_tolerance);
% check that all tests passed for generalized_sylvester
results_generalized_sylvester_bools = results_generalized_sylvester{2};
results_generalized_sylvester_test_passed = true;
for i1 = 1 : 1 : length(results_generalized_sylvester_bools)
    results_generalized_sylvester_test_passed = results_generalized_sylvester_test_passed & results_generalized_sylvester_bools(i1);
end
disp(strcat('generalized_sylvester - all tests passed:',string(results_generalized_sylvester_test_passed)))

% clean up
clear num_test_cases err_tolerance results_generalized_sylvester_bools results_generalized_sylvester_test_passed i1;