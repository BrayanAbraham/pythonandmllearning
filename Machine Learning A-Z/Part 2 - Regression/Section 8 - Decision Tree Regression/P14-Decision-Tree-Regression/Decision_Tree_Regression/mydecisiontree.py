import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('Position_Salaries.csv')
X = df.iloc[:,1:-1].values
Y = df.iloc[:,-1].values

regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,Y)


y_pred = regressor.predict(np.array([[6.5]]))
print(y_pred)

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()