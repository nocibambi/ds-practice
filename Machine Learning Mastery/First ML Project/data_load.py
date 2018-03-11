# 1. Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# 2. Loading the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# 3. Summarizing the dataset
# Shape
print(dataset.shape)

# Taking the data sample
print(dataset.sample(30))

# Dataset summary
print(dataset.describe())

# Class distibution
print(dataset.groupby('class').size())

# 4. Data visualization
# 4.1. Univariate plots
# Box diagrams
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# Histograms of variables
dataset.hist()
plt.show()

# 4.2 Multivariate plot
scatter_matrix(dataset)
plt.show()

# 5. Evaluating algorithms
# 5.1. Separating out the validation dataset.
# Getting the values in a numpy array format.
array = dataset.values

# Selecting the value and name columns
X = array[:,0:4]
Y = array[:,4]

# We split the dataset into a 80% training and 20% testing set
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = \
    model_selection.train_test_split(X, Y, test_size=validation_size, \
                                     random_state=seed)

# 2. Set-up the test harness to use 10-fold cross validation.
scoring = 'accuracy'


# 3. Build 5 different models to predict species from flower measurements
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# 4. Select the best model.
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
