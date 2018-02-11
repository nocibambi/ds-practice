# Background

## Basic concepts

* **Sample**: consists of observation about the **population**.
* **Parameter**: Characteristic of a population, such as a mean or standard deviation. Often notated using Greek letters.
* **Sampling distribution**: The probability distribution of a given statistic based on a random sample.
* **Statistical inference**: Enables you to make an educated guess about a population parameter based on a statistic computed from a sample randomly drawn from that population.
* **Expected value**: A function of the probability distribution of the observed value in the population.
* **Sample mean**: The observed mean value of the data.

> If the experiment has been designed correctly, the sample mean should converge to the expected value as more and more samples are included in the analysis.

## Distributions
### Discrete distribution

#### Properties

```math
0 \le P_i  \le 1, \quad \forall \in N
```
```math
\sum_{i=1}^{n}P_i = 1
```

There $P~i~$ is the **probability mass function** of the distribution **(PMF)**.

#### Expected value

```math
E[X] = \sum_{i} x_iP_i~ = 1
```

### Continuous distribution
Here the probability distribution is continuous, the **probability density function (PMF)**, it  describes the relative likelihood of a random variable X to take on a given value x.

Properties:
```math
p(x) \ge 0, \quad \forall x \in R
```
```math
\int_{-\infty}^{\infty} p(x)dx = 1
```
#### Expected value
```math
E[X] = \int_{-\infty}^{\infty} xf(x)dx
```

### Variance (for both)
```math
Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
```

### Degree of freedom (DOF)
A group of _n_ values have _n_ DOF. Subtracting the sample mean from each value's distribution will result in a *n* - 1 DOF. For **ANOVA** this becomes more complicated in that the group values also contribute to the overall DOF.

## Study design
Example of its importance: clinical trial in US from 2000 need to record their trial methods and outcome measure before data collection. This resulted in a drop of positive correlation from 57% to 8%.

### Terminology
* **Controlled inputs** (often called factors or treatments).
* **Uncontrolled inputs** (cofactors, nuisance factors, or confoundings).
* **Covariate**: a variable that is possibly predictive of the outcome being studied, and can be a factor or a cofactor.

### The general linear model
For a model with two inputs and one output:
```math
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_{12} X_1X_2~ + \epsilon
```
* **Main effect**: $X (\beta_1, \beta_2)$
* **Interaction terms**: $X (\beta_{12})$
* **Residual**: $\epsilon$, expected to be distributed approximately normally around zero if the model describes the data correctly

### Possible goals
Before starting any study it needs to be clarified which one is the main aim:
1. **Hypothesis test**: Compare two or **more groups**, or **one group** to a ﬁxed value.
2. **Screening investigation**: Screen the observed responses to identify factors/effects that are important.
3. **Optimization problem**: Maximize or minimize a response (variability, distance to target, robustness).
4. **Statistical modeling**: Develop a regression model to quantify the dependence of a response variable on the process input.

### Study types
* **Observational/Experimental**: is there interaction?
* **Prospective/Retrospective**: does data come from the past or is it collected within the study?
* **Longitudinal/Cross-sectional**: one single observation or continuous data collection over a period of time
* **Case-control/Cohort study**: is group selected independently of the effects of intervention on it?
* **Randomized controlled trial**: randomly splitting sample into an **intervention** and a **control** group
* **Crossover study**: Longitudinal verson of a randomized controlled trial where every subject receives every intervention but their sequence is randomized

## Experiment design
> Block whatever you can; and randomize the rest!

* **Factors**: which we can control
* **Nuisance factors**: inﬂuence the results, but which we cannot control and/or manipulate

### Points to consider
#### Sample selection
* Sample should be **representative** of the group studied.
* **Groups must be similar** with respect to known sources of variation.
* Selection of samples (or subjects) should sufﬁciently **cover all of the needed parameters**.

#### Sample size
Too small sample can lead to a study failure. In determining the sample size **power analysis** is necessary:
* What is the **variance** of the parameter under investigation?
* What is the **magnitude** of the expected effect, relative to the standard deviation of the parameter?

#### Bias
Bias can have a number of sources
* The selection of subjects.
* The structure of the experiment
* The measurement device.
* The analysis of the data.

#### Randomization
* **Simple randomization**:  Robust against selection and accidental bias but the resulting group size can differ signiﬁcantly.
* **Block randomization**: Balancing the sizes of groups
* **Minimization**: One takes whichever treatment has the smallest number of subjects, and allocates this treatment with a probability greater than 0.5 to the next patient.
* **Stratified randomization**: Trying to keep the number of subjects within different stratums balanced by keeping separate lists of random numbers.

#### Blinding
* **Double blind**: blinding both the experimenter and the study subject
* **Triple blind**: Blinding the analyst also about the identity of the groups

#### Factorial design
* **Full factorial design**: When the researcher tests each combination of factors.
* **Within subject comparison**: detects smaller differences with the same number of subjects (?)
* **Between subject comparison**

### Further advices
* **Preliminary investigation**:
  - Might prove the viability of the question
  - Provides data variability information
  - Helps to estimate required subject/sample size
* **Calibration runs**: Always start and end experimental recording with something known (e.g. 10cm left/right)
* **Documentation**: Circumstances, decisions
* **Data storage**: Be structured and backup.
