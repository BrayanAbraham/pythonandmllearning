import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

df = pd.read_csv("Social_Network_Ads.csv")
X = df.iloc[:,[2,3]].values
Y = df.iloc[:,-1].values
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.25, random_state = 0)
scx = StandardScaler()
xtrain = scx.fit_transform(xtrain)
xtest = scx.transform(xtest)

classifier = LogisticRegression(random_state = 0)
classifier.fit(xtrain,ytrain)

ypred = classifier.predict(xtest)

cm = confusion_matrix(ytest,ypred,)

Xset,Yset = xtrain, ytrain
X1,X2 = np.meshgrid(np.arange(start = Xset[:,0].min() - 1,stop = Xset[:,0].max() + 1, step = 0.01),
                    np.arange(start = Xset[:,1].min() - 1,stop = Xset[:,1].max() + 1, step = 0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(Yset)):
    plt.scatter(Xset[Yset == j,0],Xset[Yset == j,1],
                c=ListedColormap(('red','green'))(i), label = j)
plt.title(" Logistic Regression")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

Xset,Yset = xtest, ytest
X1,X2 = np.meshgrid(np.arange(start = Xset[:,0].min() - 1,stop = Xset[:,0].max() + 1, step = 0.01),np.arange(start = Xset[:,1].min() - 1,stop = Xset[:,1].max() + 1, step = 0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),alpha = 0.75, cmap = ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(Yset)):
    plt.scatter(Xset[Yset == j,0],Xset[Yset == j,1],c=ListedColormap(('red','green'))(i), label = j)
plt.title(" Logistic Regression")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()