## Automatic feature selection
High level summary: https://machinelearningmastery.com/an-introduction-to-feature-selection/
### Univariate selection
Statistical filter methods
```py
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# feature extraction
test = SelectKBest(score_func=chi2, k=4)

fit = test.fit(X, Y)
print(fit.scores_)

features = fit.transform(X)

# summarize selected features
print(features)
```


### RFE
Wrapper methods
Recursive Feature Elimination
```py
from sklearn.feature_selection import RFE

model = LogisticRegression()

rfe = RFE(model, 3)
rfe = rfe.fit(dataset.data, dataset.target)

print(rfe.n_features_)
print(rfe.support_)
print(rfe.ranking_)
```

### PCA
```py
from sklearn.decomposition import PCA

# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

# summarize components
print("Explained Variance: %s") % fit.explained_variance_ratio_
print(fit.components_)
```

### Feature importance

Ensemble or decision tree methods:
```py
from sklearn import metrics
model.fit(X, y)
print(model.feature_importances)
```

### Ensemble methods
Examples of regularization algorithms are the LASSO, Elastic Net and Ridge Regression.
