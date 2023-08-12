# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:29:39 2023

@author: admin
"""


import pandas as pd
df=pd.read_csv("iris.csv")

print(df.loc[0:3,'Gender'])
print(df.iloc[0:3,5])
print(df.iloc[2:2,2:4])
