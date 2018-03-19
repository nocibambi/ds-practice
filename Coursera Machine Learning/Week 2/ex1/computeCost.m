function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

h = X * theta; % 1. h = {multiply X and theta in the proper order}
error = h - y; % 2. error = {the difference between h and y}
error_sqr = error.^2; % 3. error_sqr = square of errors by element-wise exponentiation
J = 1/(2*m) * sum(error_sqr); % 4. sum of error square and scale (multiply) the result by

% =========================================================================

end
