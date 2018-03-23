## Importing libraries
## -------------------

import numpy as np
import pandas as pd

# Importing scikit-learn sample splitter and preprocessor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Importing the random forest model family
from sklearn.ensemble import RandomForestRegressor

# Tools for cross-validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# Import evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score

# An alternative to python's pickle
from sklearn.externals import joblib

## ----------------
## Loading the data
## ----------------

# Loading the data from an url
dataset_url = "http://mlr.cs.umass.edu/ml/machine-learning-databases/\
               wine-quality/winequality-red.csv"
data = pd.read_csv(dataset_url, sep = ';')

# Examining the data
print(data.head())
print(data.shape)
print(data.describe())

## ------------------
## Splitting the data
## ------------------

# Defining the target (y) and input features (x)
y = data.quality
X = data.drop('quality', axis = 1)

# - Separating 20% of data to test
# - Defining a random 'seed' to make the results reproducable
# - Stratifying the target variable
X_train, \
X_test, \
y_train, \
y_test = train_test_split(X, y, test_size=0.2,\
                          random_state=123, stratify=y)

## ----------------------------------
## Declaring data preprocessing steps
## ----------------------------------

# Scaling the dataset
# We use the Transformer API which uses the training data to 'fit'
# preprocessing (just like 'fitting' a model)

# 1. Fitting the transformer on the training set
scaler = preprocessing.StandardScaler().fit(X_train)

# 2. Applying the transformer on the training set
X_train_scaled = scaler.transform(X_train)
print(X_train_scaled.mean(axis=0))
print(X_train_scaled.std(axis=0))

# 3. Applying the transformer on the test set
X_test_scaled = scaler.transform(X_test)
print(X_test_scaled.mean(axis=0))
print(X_test_scaled.std(axis=0))

# The scaled features of the test set are not perfectly centered at zero with
# unit variance!

# Setting up the cross-validation pipeline
# 1. Transforming the data with StandardScaler
# 2. Fitting the model on the standardized data
pipeline = make_pipeline(preprocessing.StandardScaler(),\
                         RandomForestRegressor(n_estimators=100))

## ----------------------------------
## Declaring hyperparameters to tune
## ----------------------------------
# 1. Model parameters: what we can learn from the data
# 2. Hyperparameters: we cannot learn from the data, they express 'high-level'
#                     structural information

# Listing tunable hyperparameters
print(pipeline.get_params())

# Declaring hyperparameters
hyperparameters = {\
    'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],\
    'randomforestregressor__max_depth': [None, 5, 3, 1]}

## ------------------------------------------------
## Tune the model with the cross-valiation pipeline
## ------------------------------------------------

# Cross-validation: Estimating the performance of a method for building a model
# by training and estimating the model multiple times with the same methodself.

# 1. Split your data into k equal parts, or "folds" (typically k=10).
# 2. Train your model on k-1 folds (e.g. the first 9 folds).
# 3. Evaluate it on the remaining "hold-out" fold (e.g. the 10th fold).
# 4. Perform steps (2) and (3) k times, each time holding out a different fold.
# 5. Aggregate the performance across all k folds. This is your performance metric.

# With cross-valiation we can evaluate the different hyperparameters we would
# like to tune in. By this you can evaluate various models (and there different
# versions) on the training set only, and then use the chosen model and settings
# on the test set.

# Cross-validation pipeline: the best practice, when you preprocess inside the
# cross-validation loop.

# 1. Split your data into k equal parts, or "folds" (typically k=10).
# 2. Preprocess the k-1 trianing folds.
# 3. Train your model on k-1 folds (e.g. the first 9 folds).
# 4. Preprocess the k^th hold-out fold  (e.g. the 10th) with step 2's tranformations.
# 5. Evaluate the model on the remaining "hold-out" fold.
# 6. Perform steps (2)-(5) k times, each time holding out a different fold.
# 7. Aggregate the performance across all k folds. This is your performance metric.

# In scikit-learn:
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)

# Listing the best parameters
print(clf.best_params_)

## ---------------------------------
## Refitting the entire training set
## ---------------------------------

# Refitting the model on the entire training set might produce a slight
# performance increase. GridSearchCV, however, does this by deafaultself.

# Confirming the refit
print(clf.refit)

# From now on, we can use the `clf` as our model to apply it on other sets of data.

## ------------------------------------------
## Evaluating the model pipeline on test data
## ------------------------------------------

# Predicting a new set of data
y_pred = clf.predict(X_test)

# Evaluating model performance
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))

# Interpreting the results
# 1. Does the model help to solve the business problem?
# 2. What does the academic literature say?
# 3. Is there an obvious and easy way to improve the model?

# Improving the model
# * Other model families (possibly with the same training/test set)
# * Collect more data
# * Engineer smarter features after exploratory data analysis
# * Gain domain knowledge

## -------------------------------
## Saving the model for future use
## -------------------------------

# Saving the model
joblib.dump(clf, 'rf_regressor.pkl')

# Loading the model from the pkl
clf2 = joblib.load('rf_regressor.pkl')

# Predicting the dataset using the loaded model
clf2.predict(X_test)
