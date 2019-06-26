import numpy as np
from sklearn.datasets import load_digits
from sklearn import datasets
digits = load_digits()
#digitsOriginal = datasets.fetch_mldata("MNIST Original")
from sklearn.neighbors import KNeighborsClassifier
knnClassifier = KNeighborsClassifier(n_neighbors=3)

#x = iris['data']
#y = iris["target"]

data = digitsOriginal["data"]

import matplotlib.pyplot as plt
plt.imshow(data[0].reshape(28,28))

labels = digitsOriginal["target"]
labels[0]
from sklearn.neighbors import KNeighborsClassifier

knnClassifier = KNeighborsClassifier(n_neighbors=3)

from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784')



