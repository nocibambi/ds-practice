from sklearn import datasets

# Loading datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris)
print(digits)

# Prints the features of the dataset
print("digits.data:\n{}".format(digits.data))

# Prints the target variables
print("\ndigits.target:\n{}".format(digits.target))

# image of shape (8,8)
print("\ndigits.images[0]:\n{}".format(digits.images[0]))

# Example estimator
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100)

print("\nfitting the SVM model:\n{}".format(clf.fit(digits.data[:-1], digits.target[:-1])))
print("\nThe prediction made by the model: {}".format(clf.predict(digits.data[-1:])))
