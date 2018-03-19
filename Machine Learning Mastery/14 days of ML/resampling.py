# Resampling the data in order to split training and testing data sets from each other.

# Steps
# 1. Split a dataset into training and test sets.
# 2. Estimate the accuracy of an algorithm using k-fold cross validation.
# 3. Estimate the accuracy of an algorithm using leave one out cross validation.

# Importing libraries
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Loading and defining the data
url = "https://goo.gl/bDdBiA"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'clas']
df = read_csv(url, names=names)
array = df.values

# Separating the target
X = array[:,0:8]
Y = array[:,8]


kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
