# Grid Search for Algorithm Tuning
from pandas import read_csv
import numpy
from sklearn.linear_model import Ridge # l2 regularized linear least regression
from sklearn.model_selection import GridSearchCV # Exhastive searh over a parameter grid

# Loading the data
url = 'https://goo.gl/bDdBiA'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(url, names=names)

# Tranforming the data
array = df.values
X = array[:,0:8]
Y = array[:,8]

# Accuracy tuning
alphas = numpy.array([1,0.1,0.01,0.001,0.0001,0])
param_grid = dict(alpha=alphas)
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X, Y)

print(grid.best_score_)
print(grid.best_estimator_.alpha)
