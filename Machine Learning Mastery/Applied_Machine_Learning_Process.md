# The 5 main steps of the Applied Machine Learning Process

## 1. Defining the Problem
Perhaps the most important part.

Steps allowing to quickly overview the problem from different angles:
### 1. What is the problem?
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
### 2. Why this problem needs to be solved?
1. Motivation: what need to be fulfilled?
2. Solution benefits
    * Be clear that when will I know that I had acquired these benefits
3. Solution use
    * How will it be used?
    * What time of lifetime can we excpect?
    * How much maintenance will it need?
### 3. How can we solve the problem?
* List step-by-step, how would I solve the problem manually?
* This can bring up many very useful and surprising details.

## 2. Data preparation
* Summarizing attributes.
* Visualizing the data with historgrams and scatter plots.
* Describing the relationship between attributes.

### Main parts
#### 1. Selection
Make assumption about the data I require to answer the problem and record these for later review.
1. Defining what data is available
2. What data is missing
3. What data can be removed
#### 2. Preprocessing
1. Formatting
2. Cleaning
3. Sampling
#### 3. Transformation (Feature Engineering)
1. Transforming data
    1. Standardization: mean of zero and standar deviation of one
    2. Scaling or normalization: scale into a zero to one range
    3. Replacing skewed data with log, square root or inverse or using Box-Cox
    4. Binning (discretization): grouping data into discrete bins
2. Adding attributes
    1. Category dummy attributes
    2. Transformed (e.g. log, square, square root)
    3. Missing data replacement
3. Removing attributes
    1. Aggregating attributes: Reducing dimensions by combining features
        1. Projection (e.g. with Principal Component Analysis) # Is projection a part of dimensionality reduction
        2. Singular Value Decomposition
        3. Sammon's Mapping
    2. Spatial sign: transform data onto the surface of a multidimensional sphere
    3. Remove correlated attributes
3. Decomposing attributes

### Outlier analysis
* **Extreme Value Analysis**: Determine the statistical tails of the underlying distribution of the data (e.g. z-scores on univariate data).
* **Probabilistic and Statistical Models**: Determine unlikely instances from a probabilistic model of the data. For example, gaussian mixture models optimized using expectation-maximization.
* **Linear Models**: Projection methods that model the data into lower dimensions using linear correlations. For example, principle component analysis and data with large residual errors may be outliers.
* **Proximity-based Models**: Data instances that are isolated from the mass of the data as determined by cluster, density or nearest neighbor analysis.
* **Information Theoretic Models**: Outliers are detected as data instances that increase the complexity (minimum code length) of the dataset.
* **High-Dimensional Outlier Detection**: Methods that search subspaces for outliers give the breakdown of distance based measures in higher dimensions (curse of dimensionality).

[More about this](https://machinelearningmastery.com/how-to-identify-outliers-in-your-data/)

### Rebalancing datasets
In classification problems, when some classes are overrepresented in the dataset we say that it is **inbalanced**. It is sometimes common or, even more, expected (e.g. fraudulent transactions, customer churn).

**Accuracy paradox**: when you have great accuracy but it refers only to a single (or a small set) of the available classes.

#### Possible solutions
* Collect more data
* Changing performance **metrics**: there are [other measures](http://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/) beyond model accuracy:
    - **Confusion Matrix**: Showing correct predictions (the diagonal) and the types of incorrect predictions made.
    - **Precision**: A measure of a classifiers exactness.
    - **Recall**: A measure of a classifiers completeness.
    - **F1 Score (or F-score)**: A weighted average of precision and recall.
    - **Kappa (or Cohen’s kappa)**: Classification accuracy normalized by the imbalance of the classes in the data.
    - **ROC Curves**: Accuracy is divided into sensitivity and specificity and models can be chosen based on the balance thresholds of these values. [More about ROC curves](http://machinelearningmastery.com/assessing-comparing-classifier-performance-roc-curves-2/)
* Resampling
    - **Oversampling**: Add copies of instances of the under-respresented classes
    - **Undersampling**: delete instances of the over-represented classes
    - These are the most easy to do. Also combine them with dataset size, random/non-random sampling and resampling ratios.
* **Synthetizing** samples
    - Randomly sample instances from the minority classes (instead of making copies of them)
        - Empirically
        - Naive Bayes (samples attributes independently)
        - SMOTE (Synthetic Minority Over-sampling Technique)
* **Changing algorithms**
    - At least spot-check different algorithms
    - Decision trees can work well on imbalanced data
* Penalizing models
    - Imposing costs for making classification mistakes on the minority class
    - Penalties sometimes are model-specific
    - There are also whole frameworks for penalty models (e.g. in Weka)
    - This is a complex thing to do, though.
* Turn the perspective around
    - Get ideas from fields where imbalanced data is the norm
    - **Anomaly detection**: looks for rare events and outliers
    - **Change detection**: looks for change or difference
* Getting creative
    - Think deep about it.
    - Break it down into manageable smaller problems
    - Get ideas from [Quora](http://www.quora.com/In-classification-how-do-you-handle-an-unbalanced-training-set), or from [Reddit](https://www.reddit.com/r/MachineLearning/comments/12evgi/classification_when_80_of_my_training_set_is_of/).
    - Examples:
        - Decompose the larger class into smaller number of other classes
        - Use a One Class Classifier and treat the problem like outlier detection
        - Resample the unbalanced training set into several balanced sets and run an ensemble of classifiers on them.

### Feature Engineering
Data consists of examples/cases (rows) and attributes/dimensions (columns).
A possible definition for feature: **'meaningful attribute'.**

The prediction accuracy can depend on many things, but sometimes even weak models can create good predictions by picking up the feautures of a data with a good structure. This provides flexibility in model selection and therefore more opportunities and higher effectiveness.

Feature engineering is a representational problem and requires to turning inputs into something the algorithm understands.

#### The importance of individual features
Features can be ordered numerically by various methods
* Correlation with the target variable
    - Correlation coefficients
    - Univariate methods
* Models integrating feature importance
    - MARS
    - Random Forest
    - Gradient Booster Machines

#### Feature Extraction
Automatic dimension reduction trying to produce a more manageable shape.
* Principal Component Analysis
* Tabular data: Unsupervised clustering

#### Feature Selection
Feature selection is part of feature engineering and it is the automatic selection of useful features/attributes/variable. It is not dimension reduction, but works rather as filterig out unnecessary features.

Feature selection types
* Filtering: scoring  features according
    - Chi-square
    -
* Wrapping: scoring the sets and combinations of features
* Models containing feature selection elements
    - Stepwise regression
    - Embedding or regulated models
        - Lasso
        - Ridge regression

Danger of overfitting with feature selection
If we implement feature selection before modeling it will introduce bias into the validation mechanism. Accordingly the feature selection should be integral of the cross-validation loop.

##### Feature selection Checklist
1. Do we have domain knowledge so we can generate features manually?
2. Are features commensurate, or need normalization?
3. Might there be interdependence between the features? Create conjunctive/product of features.
4. Do we need to prune input variables? If no, we can create disjunctive features.
5. Do we need to assess features individually? Use ranking variable method.
6. Do we need a predictor? If no, stop.
7. Is our data 'dirty'? Check/disable the first five features from step 5.
8. Do we know what to try first? If no, use linear predictor.
    1. Forward selection with the 'probe' method as the stopping criterion.
    2. Use 0-norm embedded method for comparison by following the ranking in step 5 and construct a sequence of predictors by using increasing subsets of features.
If we can  match or improve performance with a smaller subset we should use that with a non-linear model.
9. Do we have many ideas? Compare
    1. different feature selections.
    2. correlation coefficients
    3. backward selection
    4. embedded methods
    5. linear and non-linear predictors.
10. Do we want a stable solution? Resample the data and redo the analysis for several bootstraps.

#### Feature Construction
Manual and proactive data aggregation and reorganization. Hard, messy and is an art.

#### Feature Learning (representation learning)
Automatic recognition of features.

There are some deep learning methods for that:
* Autoencoders
* Restriced Boltzmann machines
However, these automatic representations are hard to comprehend and, therefore, they are also hard to transfer into other problems.

#### The Feature Engineering process
It is preceded by data selection and preprocessing, however, if new features come out from engineering we might turn back to these steps.

> "It is an iterative process that interplays with data selection and model evaluation, again and again, until we run out of time on our problem."

1. Brainstorm
2. Devise
3. Select
4. Evaluate

It is important to have
* a clearly defined problem so to know when to stop with each step.
* a worked out, well understood and trusted test method to evaluate models on unseen data.

#### General Examples
##### 1. Decomposing categorical attributes
Three initial features:
    1. `Red`
    2. `Blue`
    3. `Unknown feature`

Create a feature which combines the color dimnension for each attribute
Possible new features:
* Binary: [`Is_color`, `Is_not_color`]
* One categorical or three binary: [`Is_Red`, `Is_Blue`, `Is_Unknown`]

These could be used either instead of (linear model) or in addition to the color feature (decision tree).

##### 2. Decompose Date-time features
From a general date time format we can decompose features for, for instance, the time of day:
* `Hour_of_day`
* `Part_of_day`

Similar approach to time of week, time of month, seasonality.

##### 3. Reframing Numarical Quantities
Transforming numerical data into a new unit or decomposing it into rate/amount components.

Weight attribute (in 'kg.gramm' format)
* `Weight_kg`
* `Weight_remainder_grams`
* `item_above_4kg` # If, say, there is a domain threshold for items above 4 kg.

Exposing aggregated quantity's temporal structure. For instance, from num_customer_purchases:
* `purchases_summer`
* `purchases_fall`, etc.

#### Concrete examples
1. Student Test Performance prediction: specific temporal and other non-linearities in the problem structure were reduced to simple composite binary indicators [Link](http://pslcdatashop.org/KDDCup/workshop/papers/kdd2010ntu.pdf)
2. Patient Admittance prediction (Heritage Health Price): There was many feature engineering involved. [Link](https://kaggle2.blob.core.windows.net/wiki-files/327/e4cd1d25-eca9-49ca-9593-b254a773fe03/Market%20Makers%20-%20Milestone%201%20Description%20V2%201.pdf)


#### Feature Engineering resources
* [Feature selection with python scikit-lear](http://machinelearningmastery.com/feature-selection-in-python-with-scikit-learn/)
* [Feature engineering and 'intuition'](http://www.quora.com/What-is-the-intuitive-explanation-of-feature-engineering-in-machine-learning)
* [Feature Construction as a messy artform](http://www.quora.com/How-valuable-do-you-think-feature-selection-is-in-machine-learning-Which-do-you-think-improves-accuracy-more-feature-selection-or-feature-engineering)
* [Feature engineering video](https://www.youtube.com/watch?v=drUToKxEAUA)
* [Feature Engineering: How to perform feature engineering on the Titanic competition](http://trevorstephens.com/post/73461351896/titanic-getting-started-with-r-part-4-feature)
* [... and there are more links in the article](https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/)

### Data leakage
Data leakage is when we use information outside of the data when creating our model. It often provides 'too good to be true' prediction results. It is usually a problem of complex datasets.

#### 1. Data preparation within cross-validation folds
* Doing the following tasks before cross-validation is practically leads to data-leakege:
    - Feature selection
    - Outlier removal
    - Encoding
    - Feature scaling
    - Projection methods for dimensioality reduction
* Instead, execute these tasks based on each fold within each cycle.
* Python Scikit-learn's [Pipe package](http://machinelearningmastery.com/automate-machine-learning-workflows-pipelines-python-scikit-learn/) helps to do this.

#### 2. Holding back a validation dataset for sanity check
Separate out a validation dataset from the training set and store it away, then evaluate the final model on it.

#### Further tips to prevent data leakage
* **Temporal Cutoff**: Remove all data just prior to the event of interest, focusing on the time you learned about a fact or observation rather than the time the observation occurred.
* **Add Noise**: Add random noise to input data to try and smooth out the effects of possibly leaking variables.
* Remove Leaky Variables: Evaluate simple **rule based models** line **OneR** using variables like account numbers and IDs.

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
