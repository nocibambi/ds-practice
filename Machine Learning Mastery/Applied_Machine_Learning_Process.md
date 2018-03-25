# The 5 main steps of the Applied Machine Learning Process

## 1. Define the Problem
Perhaps the most important part.

Steps allowing to quickly overview the problem from different angles:
1. What is the problem?
    1. Informal description, as you were explaining to a friend.
    2. Formal:
        1. Task: to be performed by the model
        2. Experience: from which the model learns
        3. Performance: the models efficiecy to do the task
        The machine 'learns' if 'P' increases.
    3. Assumptions
        * Create a list of them
        * Useful if they can be tested with real data.
        * Can also highlight issues in problem specification.
    4. Similar problems: can point out limitations, methods.
2. Why this problem needs to be solved?
    1. Motivation: what need to be fulfilled?
    2. Solution benefits
        * Be clear that when will I know that I had acquired these benefits
    3. Solution use
        * How will it be used?
        * What time of lifetime can we excpect?
        * How much maintenance will it need?
3. How can we answer the question?
    * List step-by-step, how would I solve the problem manually?
    * This can bring up many very useful and surprising details.

## 2. Prepare Data
* Summarizing attributes.
* Visualizing the data with historgrams and scatter plots.
* Describing the relationship between attributes.

### Main parts
1. Selection
    1. Defining what data is available
    2. What data is missing
    3. What data can be removed
2. Preprocessing
    1. Formatting
    2. Cleaning
    3. Sampling
3. Transformation
    1. Aggregating attributes
    2. Decomposing attributes

## 3. Spot Check Algorithms
By using 10 fold cross validation, running a test on 10-20 algorithms.
* Collecting mean and standard deviation on each.
* Running statistical significance tests.
* Using box plots to visualize the accuracies of algorithm-dataset combinations.


## 4. Improve Results
* Algorithm tuning: Trying to find the best models in the parameter space. Running sensitivity analysis on the parameters of the selected algorithms.
* Designing and running ensemble methods
* Extreme feature engineering: attribute decomposition and aggregation.

Keeping statistical significance in focus is still crucial here.

## 5. Present Results
* Context
* Problem
* Solution
* Finding
* Limitations
* Conclusion
