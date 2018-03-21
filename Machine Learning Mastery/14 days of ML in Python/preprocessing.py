# Here we use scikit-learn preprocessing to prepare data

# Usual options
# 1. Strandardize: mean 0 and std 1
# 2. Normalize e.g to a range of [0, 1]
# 3. Advanced (Binarizing)

# Importing libraries
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# Defining the data
url = "https://goo.gl/bDdBiA"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(url, names=names)
print("Original dataframe from csv:\n{}\n".format(df.head()))

array = df.values

# Separating the target
X = array[:,0:8]
Y = array[:,8]

# Standardizing the data (mean 0, std1)
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
np.set_printoptions(precision=3)
print("Rescaled training data array:\n{}".format(rescaledX[0:5,:]))
