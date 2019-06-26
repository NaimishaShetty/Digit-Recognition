from sklearn.datasets import load_digits

digits= load_digits()

data = digit["data"]
labels = digits["target"]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(data,labels,random_state=0,test_size=1/3)

from sklearn.neighbors import KNeighborsClassifier

kClassifier = 