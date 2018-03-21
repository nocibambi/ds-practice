# Random Forest Classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # Averaging decision tree classifiers on various samples of the dataset

# Loading the data
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(url, names=names)

# Transforming data
array = df.values
X = array[:,0:8]
Y = array[:,8]

# Preparing the model
num_trees = 100
max_features = 3
kfold = KFold(n_splits=10, random_state=7)

# Applying the algorithm
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
