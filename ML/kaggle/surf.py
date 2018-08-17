# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:39:52 2018

@author: Vigneshwaran
"""

import pandas as pd
import matplotlib.pyplot as mpl
filepath=r'C:\Users\Vigneshwaraen\Desktop\bin\melb_data.csv'
data=pd.read_csv(filepath)
#print(data.isnull().any())
data = data.fillna(data.mean())
#print(data.isnull().any())
#print(data.columns)
#print(data.Price.head())
#columns_of_interest = ['Landsize', 'BuildingArea']
#two_columns_of_data = data[columns_of_interest]
#print(two_columns_of_data.head())
from sklearn.tree import DecisionTreeRegressor
melbourne_predictors = ['Rooms']
# Define model
melbourne_model = DecisionTreeRegressor()
x=data[melbourne_predictors]
y=data.Price
# Fit model
o=melbourne_model.fit(x, y)
mpl.plot(x,y,data=o)

