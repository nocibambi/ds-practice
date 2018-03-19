function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Manual insert of values
% data = load('ex1data1.txt');
% y = data(:, 2);
% m = length(y); % number of training examples
% X = [ones(m, 1), data(:,1)]; % Add a column of ones to x
% theta = zeros(2, 1); % initialize fitting parameters
% num_iters = 1500;
% alpha = 0.01;

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta.
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    J = computeCost(X, y, theta);
    h = X * theta;
    error = h - y;
    gradient = (alpha * 1/m) * X' * error;
    theta = theta - gradient;
    J_new = computeCost(X, y, theta);

    % fprintf('\nThe value of the gradient: %f', gradient);
    % fprintf('\nThe value of new theta: %f', theta);

    % fprintf('\nThe value of new J: %f', J);
    % fprintf('\nThe value of the previous J: %f\n', J_history);

    if J < J_new
        break;
    else
        J = J_new;
    end;


    % ============================================================

    J_history(iter) = J;
    % Save the cost J in every iteration

end;

end
