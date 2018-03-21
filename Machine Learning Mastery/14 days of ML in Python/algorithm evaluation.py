# Algorithm evaluation

# Importing libraries
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Getting and defining the data
url = "https://goo.gl/bDdBiA"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(url, names=names)
array = df.values

# Splitting features and the target
X = array[:, 0:8]
Y = array[:, 8]

# Splitting training and testing datasets
kfold = KFold(n_splits=10, random_state=7)

# Model parameters
model = LogisticRegression()
scoring = 'neg_log_loss'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)

print("logloss: %.3f (%.3f)" % (results.mean(), results.std()))
