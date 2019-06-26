import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

from sklearn.neighbors import KNeighborsClassifier

knnClassifier = KNeighborsClassifier(n_neighbors=3)

#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=1/3)

knnClassifier.fit(x,y)

y_pred = knnClassifier.predict(x)

j=0
count=0
for i in y:
    if i == y_pred[j]:
        count+=1
    j+=1
print(count)
u=j-count
print(u)