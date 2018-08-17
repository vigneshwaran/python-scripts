# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:44:21 2018

@author: Vigneshwaran
"""

import tensorflow as tf
import pandas as pd
from matplotlib import pyplot as plt
test=pd.read_csv(r"C:\Users\Vigneshwaraen\Desktop\bin\iris_test.csv",names=['f1','f2','f3','f4','f5'])
train=pd.read_csv(r"C:\Users\Vigneshwaraen\Desktop\bin\iris_training.csv",names=['f1','f2','f3','f4','f5'])
train_data=train
test_data=test
"""test['f5']=test['f5'].astype(list)
train['f5']=train['f5'].astype(list)
train_data['f5'] = train_data['f5'].map({0: [1, 0, 0], 1: [0, 1, 0], 2: [0, 0, 1]})
test_data['f5'] = test_data['f5'].map({0: [1, 0, 0], 1: [0, 1, 0], 2: [0, 0, 1]})"""
train_x = train_data[['f1', 'f2', 'f3', 'f4']]
train_y = train_data.loc[:, 'f5']
print(test.describe())
print(train.describe())