# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:58:30 2020

@author: Axel Blaze
"""
import math
import numpy as np  
import pandas as pd  
#from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
from sklearn.neural_network import MLPClassifier
#importing Dataset
dataset = pd.read_csv(r'test.csv')
df=pd.read_excel(r'alpha power.xlsx')
X_train=df.iloc[:,0:19]
y_train=df.iloc[:,19]
x=dataset.iloc[0:19,1]
X_test=np.vstack((x,x))
print(X_test)
mlp = MLPClassifier(hidden_layer_sizes=(15,15,15),max_iter=500)
mlp.fit(X_train,y_train)
y_pred = mlp.predict(X_test)
print(y_pred)
#column wise
