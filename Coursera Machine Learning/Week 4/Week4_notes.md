# Model Representation
## Main terms
* dendrites: inputs
* axons: outputs
* $x_0$: bias unit, always equals to 1
* sigmoid (logistic) activation funciton
```math
\frac{1}{1 + e^{-\theta^T x}}
```
* weights: theta values

```math
\begin{bmatrix}
x_0 \\ x_1 \\ x_2
\end{bmatrix}

\rightarrow

\begin{bmatrix}
a_1^{(2)} \\ a_2^{(2)} \\ a_3^{(2)}
\end{bmatrix}

\rightarrow
\begin{bmatrix}
\\...\\\\
\end{bmatrix}
\rightarrow

\begin{bmatrix}
a_1^{(n)} \\ a_2^{(n)} \\ a_3^{(n)}
\end{bmatrix}

\rightarrow h_\theta (x)
```
The input nodes (layer 1) go into another node (layer 2) which becames the hypothesis function (output layer).

## Calculating the hypothesis function
1. Applying each row of the parameter matrix $\Theta_j$ on the particilar input layer. This will give us the values of the activation node for each row.
    * $a_i^{(j)} $: activation of unit $i$ in layer $j$
    * $\Theta^{(j)}$: matrix of weights controlling function mapping from layer $j$ to layer $j+1$.
    * $a_i^{(j)} = g(\Theta_{i0}^{(1)}x_0 + \Theta_{i1}^{(1)}x_2 + \Theta_{i2}^{(1)}x_2 + \Theta_{i3}^{(1)}x_3)$

2. We apply the logistic function on the sum of the activation nodes weighted by another parameter matrix $\Theta_2$.
    * $h_\Theta(x) = a_i^{(n+1)} = g(\Theta_{10}^{(2)}a_0^{(2)} + \Theta_{11}^{(2)}a_1^{(2)} + \Theta_{12}^{(2)}a_2^{(2)} + \Theta_{13}^{(2)}a_3^{(2)})$


If network has $s_j$ units in layer $j$ and $s_{j+1}$ units in layer $j+1$, then $Θ_{(j)}$ will be of dimension $s_{j+1}×(s_j+1)$.

## Vectorized implementation
$z_k^{(j)}$: the parameters in our $g$ function where $a_i^{(j)} = g(z_i^{(j)})$.

Vector representation
```math
x = \begin{bmatrix} x_0 \\ x_1 \\ ... \\ x_n \end{bmatrix} z^{(j)}
  = \begin{bmatrix} z_1^{j} \\ z_2^{j} \\ ... \\ z_n^{j} \end{bmatrix}
```

If we set $x = a^{(1)} $, we can transform the above equation into
```math
z^{(j)} = \Theta^{(j-1)} a^{(j-1)}
```
1. The $\Theta^{(j-1)}$ matrix has $s_j \times (n + 1)$ dimensions ($s_j$: is the number of activation nodes)
2. We multiply $\Theta^{(j-1)}$ with $a^{(j-1)}$ (with (n+1) height) and get $z^{(j)}$ (with $s_j$ height).
3. We get the activation node vector for layer $j$ by $a^{(j)} = g(z^{(j)})$, where the $g$ function is applied element-wise to $z^{(j)}$
4. We add the $a_0^{(j)} = 1$ bias unit to layer $j$.
5. We get the final $z$ value by multiplying the next $\theta$ (one-row) matrix with all the acitvation nodes (one column): $z^{(j+1)} = \Theta^{(j)} a^{(j)}$
6. The hypothesis function: $h_\Theta(x) = a ^ {(j+1)} = g(z^{(j+1)})$
