[Original post](https://machinelearningmastery.com/handle-missing-data-python/)

# Identifying missing values
Sometimes missing data is not visible immediately but is coded as a 'normal' value (e.g. 0 or 999, etc.)

One way do find these cases is to examine the attributes' value distribution.

```py
import pandas as pd
df.describe()
```

E.g. for particular attributes the minimum/maximum values are not meaningful.

# Counting missing values
In order to decide what to do with missing values, we might need to examine their weight within the attribute's value range.

```py
import pandas as pd

miss_count = df.isnull().sum()[df.isnull().any() == True].sort_values(ascending=False)
miss_rat = df.isnull().mean()[df.isnull().any() == True].sort_values(ascending=False)
miss_count.plot(kind='hist')
```

# Selecting attributes above a set threshold proportion of missing values
nonmiss = miss_rat[miss_rat < 0.5].index

# Removing missing values
```py
import pandas as pd

df.shape
df.dropna(axis=1, how='any', inplace=True)
df.shape
```

# Imputing missing values
Variations for imputing:
* A constant value which has meaning on the domain
* Mean, median or mode
* An estimated by another model
* A randomly selected record

Note that you also need to impute missing values whenever you want to apply the model on a new data.

## Doing with pandas
```py
import pandas as pd
df.fillna(df.mean(), inplace=True)
```

## Doing with scikit-learn: imputer()
* Allows replacing other values as well
* Works on the numpy array, not on the dataframe

```py
import pandas as pd
from sklearn.preprocessing import Imputer

imputer = Imputer()
transformed_values = imputer.fit_transform(df.values)
```

# Algorithms that support missing values
* For instance K-nearest neighbors can ignore missing values when calculating distance (although not robust in scikit-learn).
* There are other algorithms which make use of missing values as information (e.g. classification and regression trees)


# References
* http://pandas.pydata.org/pandas-docs/stable/missing_data.html
* http://scikit-learn.org/stable/modules/preprocessing.html#imputation-of-missing-values
