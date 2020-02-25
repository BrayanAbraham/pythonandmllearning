import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv('C:\\Users\\APP India\\Desktop\\New folder\\ML\\Machine Learning A-Z\\Part 1 - Data Preprocessing\\Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values


#missing data
imputer = SimpleImputer(missing_values = 'NaN', strategy = 'mean')
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)