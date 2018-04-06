# Classification and representation
## The sigmoid (or logistic) function
Compared to the linear regression problem, $ h_\theta(x) $ has to fall into the [0, 1] since $ y \in \{0, 1\} $


```math
\begin{gathered}

h_\theta(x) = g(\theta^T x) \\

z = \theta^T x \\

g(z) = \frac{1}{1 + e^{-z}}

\end{gathered}
```

Where $ h_\theta(x) $ will give us the probability that our output is 1.

## Decision boundary
We can divide the possible cases when $ y $ is 1 and when it is 0. Based on the sigmoid function this occurs in the following cases:

```math
\begin{gathered}

\theta^T x \ge 0 \quad \Rightarrow \quad y = 1 \\
\theta^T x \le 0 \quad \Rightarrow \quad y = 0

\end{gathered}
```

# Logistic regression
## Cost function
We cannot use the same cost function as for linear regression because in this case it would be 'wavy', that is, non-convex.

Instead we use the following cost function:
```math
\begin{gathered}

J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \text{Cost}(h_\theta(x(i)), y(i)) \\

\text{Cost}(h_\theta(x), y)= -\log (h_\theta(x)) \quad if \quad y = 1 \\

\text{Cost}(h_\theta(x), y)= -\log (1 - h_\theta(x)) \quad if \quad y = 0

\end{gathered}
```

This will generate the following cost outcomes for the different $y$ and $h(\theta)$ conbinations:

```math
\begin{gathered}
\text{Cost}(h_\theta(x),y)=0 \quad if \quad  h_\theta(x)=y \\
\text{Cost}(h_\theta(x),y)→∞ \quad if \quad  y=0 \quad and \quad h_\theta(x)→1 \\
\text{Cost}(h_\theta(x),y)→∞ \quad if \quad  y=1 \quad and \quad h_\theta(x)→0
\end{gathered}
```

## Simplified cost function and gradient descent
Merging the two cases of the cost function and expressing it in a vectorized form:

```math
\begin{gathered}

h = g(X\theta) \\
J(\theta) = \frac{1}{m} \big(-y^T \log h - (1-y)^T \log(1 - h) \big)

\end{gathered}
```

The vectorized gradient descent is similar to the one we used with linear regression:

```math

\theta:= \theta - \frac {\alpha}{m} X^T (h - \overrightarrow{y})
```

## Conjugate gradient (BFGS, L-BFGS)
These are advanced optimization techniques optimizing $\theta$ faster.

These can be very complicated but are already optimized in Octave:

First we calculate both $ J(\theta) $ and its derivative on $\theta_j$:

```octave
function [jVal, gradient] = costFunction(theta)
    jVal = [...code to copute J(theta)...];
    gradient = [...code to compute the derivativ of J(theta)];
end
```

We then use the `fminunc()` optimization algorithm with the following parameters:
* the cost function
* the initial theta values vector
* setting parametes set with the `otpimset()` function

```Ocatve
options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2, 1);
    [optTheta, functionVal, exitFlag] = fminumc(@costFunction, initialTheta, options);
```

# Multiclass classification
Now we have n > 2 classes so we divide the initial problem as n + 1 different binary problems (+1, because the index starts at 0).

1. We run a logistic regression for each class as if it would be the primary class and everything else the secondary and calculate the probability that y is the member of it.
2. From among these, we take the highest probability as our result.

```math
\begin{gathered}

y \in \{0,1,...,n\} \\
h_\theta^{(0)} (x) = P(y=0|x;\theta) \\
h_\theta^{(1)} (x) = P(y=1|x;\theta) \\
... \\
h_\theta^{(n)} (x) = P(y=n|x;\theta) \\
\\
\text{prediction} = \max_{i} (h_\theta^{(i)}(x))

\end{gathered}
```

# Solving the problem of Overfitting
## The Problem of overfitting
* Underfitting or high bias: where our hypothesis function maps poorly on the data
* Overfitting or high variance: fits very well the available data but cannot generalize and predict new data.

Solutions for overfitting:
1. Reducing features manually or algorithmically
2. Regulating the model: reduce the magniture of $\theta_j$

## Cost function
We can reduce $\theta$s' magnitude by inflating the cost of some of them:
```math
min_{\theta} \frac {1}{2m} \sum_{i=1}^{m} (h_\theta (x)^{(i)} - y^{(i)})^2 + \lambda \sum_{j=1}^{n}\theta_j^2
```

However, if the $ \lambda $ is too big, it can cause underfitting.

## Regularized linear regression

### Gradual descent
For linear regression we separate $\theta_0$ from the penalization. For the rest we can write up the following method:

```math
\theta_j := \theta_j - \alpha \Big [ \Big (\frac{1}{m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)}) x_j^{(i)} \Big) + \frac{\lambda}{m} \theta_j \Big] \quad \quad j \in \{1,2...n\}
```
Or, in another form:
```math
\theta_j := \theta_j (1 - \alpha \frac{\lambda}{m}) - \frac{\alpha}{m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)}) x_j^{(i)}
```
### Normal equation
```math
\begin{gathered}
    \theta = (X^T X + \lambda \cdot L)^{-1} X^T y
\\ \\
    \text{where} \quad
    L = \begin{bmatrix}
            0 \\
            & 1 \\
            && 1 \\
            &&& \ddots \\
            &&&& 1
        \end{bmatrix}
\end{gathered}
```

## Regularized logistic regression
Very similar to the linear regression, the new cost function looks like this:

```math
J(\theta) = - \frac{1}{m} \sum_{i=1}^{n} \big[+y^{(i)} \log h_\theta(x^{(i)}) + (1-y)^{(i)} \log(1 - h_\theta(x^{(i)})) + \frac{\lambda}{2m} \sum_{j=1}^{n} \theta_j^2 \big]
```
