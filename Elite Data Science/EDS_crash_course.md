# 1. Overview

## Supervised learning
* Continuous data: Regression
* Categorical data: Classification

## Unsupervised learning
* Clustering, making groups

## Overfitting
* When the model learns the 'noise' in the training set

# 2. Exploratory Data Analysis

## Basic questions to ask
1. Number of observations
2. Number of features
3. Data types of features
4. Is there a target variable?

## Getting a feel of the data
In python, **seaborn** is a great library for Exploratory Analysis.
1. Do columns make sense?
2. Do values make sense?
3. Are values on the right scale?
4. Is too much data missing?

## Reviewing data distributions
Getting a grid of **histograms** of the columns is very useful. This might provide information about the following issues:
* Unexpected distributions
* Outliers
* Features that should be binary (i.e. "wannabe indicator variables")
* Boundaries that don't make sense
* Measurement errors

## Categorical features
You cannot plot **categorical features** on histograms, but instead you can use **bar plots** for them.
* **Sparse classes** (with very few observations)
  - They either do not influence the model, or
  - they make it overfit.

## Segmentations
**Box plots** allow to observe **relationship between categorical and numerical variables**.
* Median values for different categories
* Min and max transaction prices comparable between classes.
* Round-number min and max values suggest possible data truncation.

## Correlations
We can use them to examine the relationship between numeric features. **Correlation heatmaps** are great ways to examine them.
* "Correlation is a value between -1 and 1 that represents how closely two features move in unison.
* **Positive** correlation means that as one feature increases, the other increases. E.g. a child’s age and her height.
* **Negative** correlation means that as one feature increases, the other decreases. E.g. hours spent studying and number of parties attended.
* Correlations **near -1 or 1** indicate a strong relationship."
* Those **closer to 0** indicate a weak relationship and 0 indicates no relationship whatsoever.

# 3. Data cleaning
Main problems:
* Unwanted observations
* Structural errors
* Unwanted outliers
* Missing data

## Unwanted observations
* **Duplicates**, often as the result of:
  - Combining data sets
  - Scraping data
  - Receiving data from other places
* **Irrelevant data**
  - Observations which do not fit the specific problem
  - Charts of categorical features can be helpful here

## Structural errors
Structural errors are those that arise during measurement, data transfer, or other types of "poor housekeeping."
* Typos
* Inconsistent capitalization
* Mislabeled classes

## Missing data
You cannot simply ignore them.
* Dropping
  - It also drops information
  - The fact of being missing is information
* Imputing: also leads to information loss

Instead you should **tell the model that there is information missing**.
 * Categorical data: label them Missing!
 * Numerical data: flag and fill the values with 0!

You allow the model to estimate the optimum constant of missingness.

## 4. Feature Engineering
Creating new input features from existing ones.
* Isolate and highlight information
  - Creating an **indicator (binary) variable**
* Use own or other's domain expertise
  - **Interaction features**: The combination of two or more features (e.g. product, sum, difference, etc.) which is more useful.
  - **Sparse classes**: combining them into bigger groups (e.g. ~50 observations)
  - **Dummy variables**:
    - Machine learning algorithms cannot directly handle categorical (esp. text) variables
    - Dummy variables represent a single class from each
  - Remove **unused**: which does not make sense
    - id
    - text descriptors
    - features that won't be available in the time of prediction

As a result you transformed the original raw data into **Analytical Base Table (ABS)**.

Not all the engineered features has to be useful. Some machine learning algorithms have **built-in feature selection**, that is, they can automatically select the best features.

## 5. Algorithms
Linear regression is perhaps the most easily usable model widely applied in research and reporting. Howerver it has some problems which make it a very bad tool for prediction.

### Flaws of Linear Regression
1. **Overfitting data**: the regression model learns all the features (including the noise) but not the underlying connections. Accordingly it will not be able to predict new data.
2. Inability to predict **non-linear** relations.

### Regularization
The main method to avoid overfitting is to artificially constrain the model features by dampening large coefficients or dropping features entirely.
1. **Lasso regression**:
    * Dropping whole features or weaening them to zero coefficients.
    * Works with absolute sizes of coefficients.
    * Offers automatic feature selection.
2. **Ridge regression** ('feature shrinkage')
    * Weakening features' weight close to zero.
    * Works with squared size of coefficients.
3. **Elastic net**: Combination of the Ridge and Lasso.
    * The ratio of the two methods and the overall strength can be tuned.

### Decision trees
Decision trees are good predicting non-linear relationship. However they are very prone to overlearning the data (by making a leave for each observation). In order to use them effectively, the need to be constrained or combined with other models.

### Ensembles
It is very common that data scientists use different models so they can overcome each other's limitations.
1. **Bagging**: Developing a few 'strong' (unconstrained) models and smoothing out their issues.
2. **Boosting**: Developing many 'weak' (i.e. constrained) models learning from the mistakes of the previous ones and combining them.

#### Ensemble decision tree models
Decision trees are often used in ensembles.
1. **Random forest**
    * Very usable, one-shot model
    * Based on randomization:
        - Feature selection: Choosing from a random sample of features to decide upon
        - Resampling: Being trained only on a random sample of observations.
2. **Boosted tree**: sequence of week constrained decision trees
    * Each tree has an allowed maximum depth
    * Each tree learns from the previous tress' mistakes
    * Have the highest performance ceelings, but they need lots of complicated tuning.

## 6. Model training

### Split dataset
Because our data is a limited resource we should use it very wisely, so we separate out a part of it.

Before everything we should split our data into training and testing sets. After we have trained the model(s) on the training set we can apply it on the testing set.

### Hyperparameters
Hyperparameters (e.g. penalty strength, number of trees) are parameters which we cannot tell from the date itself, and which are not model-specific. We need to decide about the hyperparameters before fitting the model.

### Cross-validation
During cross-validation we train models on parts of the training set and test them on the remaining part. We combine them multiple times so we basically traing through the whole training set.

The steps of the most common, 10-fold method:
1. Randomly splitting the training data into 10 equal size.
2. Training the model on 9 folds.
3. Testing the trained model on the 10th fold.
4. Executing 2-4. steps on the next fold.
5. Taking the average of the 10 performances, the **cross-validated score**.

This is a good method to avoid overfitting.

### Fitting and tuning models
With all the model types we run the cross-validate loops with all the hyperparameter combinations we want to try out.

Based on the resulting cross validation scores we rank the model-hyperparameter combinations, pick those which we want to use on the test data set and **train them on the whole training set**.

### Winner selection
We apply the chosen model-hyperparameter combination on the testing data set and run various performance measures on them.

* Regression: Mean Squared Error or Mean Absolute Error (MAE)
* Classification: Area under ROC curve (AUROC)

Questions to pick the winning model:
1. Performance
2. Robustness: performing well across various metrics
3. Consistency: cross-validated score on the training set.
4. Business usability: soling the original business problem.
