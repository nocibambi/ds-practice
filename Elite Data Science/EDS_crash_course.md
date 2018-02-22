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
