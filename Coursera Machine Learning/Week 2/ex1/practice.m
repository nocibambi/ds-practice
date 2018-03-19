% Practice code

% Multivariate linear regression

% Loading in the data
data = load('ex1data1.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y);
J = 0;

% Plotting the data
plot(X, y, 'rx', 'MarkerSize', 10);
ylabel('Profit in $10,000s');
xlabel('Population of City in 10,000s');

% Setting the parameters for the gradual descent.
X = [ones(m, 1), data(:, 1)];
theta = zeros(2, 1);
iterations = 1500;
alpha = 0.01;

% Calculating J
h = X * theta; % 1. h = {multiply X and theta in the proper order}
error = h - y; % 2. error = {the difference between h and y}
error_sqr = error.^2; % 3. error_sqr = square of errors by element-wise exponentiation
J = 1/(2*m) * sum(error_sqr); % 4. sum of error square and scale (multiply) the result by

% Test cases
computeCost([1 2; 1 3; 1 4; 1 5], [7; 6; 5; 4], [0.1; 0.2])
% ans =  11.945
computeCost([1 2 3; 1 3 4; 1 4 5; 1 5 6], [7; 6; 5; 4], [0.1; 0.2; 0.3])
% ans =  7.0175
