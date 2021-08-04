import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/home/ubuntu/Desktop/AML LAB/studentscores.csv')

x = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=1/4,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor=regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test) 


plt.scatter(X_train, y_train, color='red') 

plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.show() 

plt.scatter(X_test, y_test, color='red') 
plt.plot(X_test, regressor.predict(X_test), color='blue')
plt.show() 

