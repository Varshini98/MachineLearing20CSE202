
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 
df=pd.read_csv('/home/ubuntu/Desktop/AML LAB/multiple-lr-data.csv')
df.head()

y=df['loan']
x=df[['age','credit-rating','children']]

linear_regres=LinearRegression()
linear_regres.fit(x,y)

y_pred=linear_regres.predict(x)

y_pred

mean_squared_error(y,y_pred)
