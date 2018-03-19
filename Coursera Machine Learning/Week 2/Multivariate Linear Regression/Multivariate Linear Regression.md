# Multivariate Linear Regression

## Hypothesis

```math
h_{\theta}(x) = \theta^Tx = \theta_0 x_0 + \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n
```

## Cost function
```math
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta} (x^{(i)}) - y^{(i)})^2
```

## Gradual descent with multivariate linear regression
In this case $(n \ge 1)$.

Repeat the following:
```math
\theta_j := \theta_j - \alpha\frac{1}{m} \sum_{i=1}^{m} (h_{\theta} (x^{(i)}) - y^{(i)})^2 x_j^{(i)}
```

Simultaneously update $\theta_j$ for $j = 0,...,n$.

## Adjusting the range

Gradual descent is more effective when all the features of the data are about of the same range and, therefore, we can transform them into the [-1, 1], [0, 1] or [-0.5, 0.5] intervals.

There are two ways to do it.
1. Feature scaling
2. Mean normalization

### 1. Feature scaling
Dividing values with the range.

### 2. Mean normalization
Substracting the mean from the value and dividing the result by the range or standard deviaton.

```math
x_i := \frac{x_i - \mu_i}{s_i}
```
Where $\mu_i$ is the feature mean and ${s_i}$ the either the range or the standard deviation.

The resulting new average is zero.

## Learning ratio

### Debugging
If a gradient descending iteration increases the $J(\theta)$ cost function, the $\alpha$ should be smaller.

### Finding a threshold value
If the $\alpha$ is small enough, all the iterations will decrease the $J(\theta)$ cost function. If it decreases by less than a particular threshold, we might declare convergence. However, it is not always easy to decide how small this threshold should be.

### Summary
* If $\alpha$ is too big, the gradient descent can take values where the $J(\theta)$ cost function is bigger than the previous one.
* If $\alpha$ is too small, however the learning process is very slow.

## Improving features
We can improve our features by making new ones out of them.

### Combination
The most straightforward way is to multiply them together.

```math
x_3 = x_1 \cdot x_2
```

### Polynomial regressions
From linear regression we can also make higher order equations. This can work well even with univariate equations.

```math
h(0) = \theta_0 + \theta_1 x_1
```
#### Quadratic function
```math
h(0) = \theta_0 + \theta_1 x_1 + \theta_2 x_1^2
```
By which, we practically create a new feature: $ x_2 = x_1^2 $

#### Cubic function
```math
h(0) = \theta_0 + \theta_1 x_1 + \theta_2 x_1^2 + \theta_3 x_1^3
```
Where $ x_3 = x_1^3 $.

#### Square root function
```math
h(0) = \theta_0 + \theta_1 x_1 + \theta_2 \sqrt{x_1}
```
Where $ x_2 = \sqrt{x_1} $.

#### Range
In these cases, however, it is important that we adjust for the features' ranges. For instance if the range for $x_i$ is [1, 100], for $x_i^2$ is [1, 10000].

## Normal equation
We can also minimize $J$ by taking its derivatives with respect to the $(\theta)_j$s and set them to zero. This uses matrix transformations and does not require iterations.

```math
\theta = (X^T X)^{-1} X^T y
```

### Comparing with gradual descent
1. No need for $\alpha$
2. No need for iterations
3. Because of the $ (X^T X)^{-1} $ calculation, $ O(n^3) $ and, therefore, calculating normal equation becomes too slow for very high number of examples (cc. 10.000). In those cases it it better to use gradual descent, which has a $O(kn^2)$.

### Noninvertable normal equations
Sometimes it is not possible to invert the $X^TX$ part of the equation.

Reasons of noninvertability
1. Too many features:
    a. Delete some features
    b. Do regularization
2. Features are linearly interrelated (redundant)

#### Matrix inversion in Octave
In Octave instead of `inv` use `pinv` because that also runs on noninvertable $X^TX$.
