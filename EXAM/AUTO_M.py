# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:29:24 2022

@author: admin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#print(os.chdir("B:\ICT_41\data"))
automobile = pd.read_csv("Automobile_data.csv")
#print the csv file
print(automobile.head())
print("=====================================")
#getting dataypes
print("datatypes are " ,automobile.dtypes)
print("=====================================")
#getting Statistics
print("Describe")
print(automobile.describe())
print("=====================================")
#cleaning data
print("Clean the data")
print(automobile.isnull().sum())
print("=====================================")

# Find out number of records having '?' value for normalized losses
print(automobile['normalized-losses'].loc[automobile['normalized-losses'] =='?'].count())
print("=====================================")

#convert the datatype to integer
nl = (automobile['normalized-losses'].loc[automobile['normalized-losses'] != '?'])
nlmean = nl.astype(str).astype(int).mean()
automobile['normalized-losses'] = automobile['normalized-losses'].replace('?' , nlmean).astype(int)
print(automobile['normalized-losses'].head())
print("=====================================")

#cleaning price data
#Find out the number of values which are not numeric
print(automobile['price'].str.isnumeric().value_counts())
#List out the values which are not numeric
print(automobile['price'].loc[automobile['price'].str.isnumeric() == False])
#Setting the missing value to mean of price and convert the datatype to integer
price = automobile['price'].loc[automobile['price'] != '?']
pmean = price.astype(str).astype(int).mean()
automobile['price'] = automobile['price'].replace('?',pmean).astype(int)
print(automobile['price'].head())
print("=====================================")

#Checking the numberic and replacing with mean value and convert the datatype to integer
automobile['horsepower'].str.isnumeric().value_counts()
horsepower = automobile['horsepower'].loc[automobile['horsepower'] != '?']
hpmean = horsepower.astype(str).astype(int).mean()
automobile['horsepower'] = automobile['horsepower'].replace('?',pmean).astype(int)
#Checking the outlier of horsepower
print(automobile.loc[automobile['horsepower'] > 10000])
#Excluding the outlier data for horsepower
print(automobile[np.abs(automobile.horsepower - automobile.horsepower.mean()) <= (3*automobile.horsepower.std())])
print("=====================================")

#Find out the number of invalid value
print(automobile['bore'].loc[automobile['bore'] == '?'])
#Replace the non-numeric value to null and conver the datatype
automobile['bore'] = pd.to_numeric(automobile['bore'],errors='coerce')
print(automobile.dtypes)
print("=====================================")

#Replace the non-number value to null and convert the datatype
automobile['stroke'] = pd.to_numeric(automobile['stroke'],errors='coerce')
print(automobile.dtypes)
print("=====================================")

#Convert the non-numeric data to null and convert the datatype
automobile['peak-rpm'] = pd.to_numeric(automobile['peak-rpm'],errors='coerce')
print(automobile.dtypes)

#remove the records which are having the value '?'
print("=====================================")
#Line Chart
'''
automobile['num-of-doors'].loc[automobile['num-of-doors'] == '?']
automobile = automobile[automobile['num-of-doors'] != '?']
automobile['num-of-doors'].loc[automobile['num-of-doors'] == '?']
automobile.make.value_counts().nlargest(10).plot(kind='bar',figsize=(15,5))
plt.title('Number of vehicles by make')
plt.ylabel('Number of vehicles')
plt.xlabel('Make');
plt.savefig('CompaniesToNoOfVehicles')
'''

#bar chart
'''
automobile.symboling.hist(bins=6,color='green');
plt.title("Insurance risk ratings of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Risk rating');
plt.savefig('VehiclesToRiskRating.png');
'''
#histogram chart
'''
automobile['normalized-losses'].hist(bins=5,color='orange');
plt.title("Normalized losses of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Normalized losses');
plt.savefig('NoOfVehiclesToNormLossed.png');
'''

#bar chart
'''
automobile['fuel-type'].value_counts().plot(kind='bar',color='purple')
plt.title("Fuel type frequence diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');
plt.savefig('NoOfVehiclesToFuelType.png')
#for pie chart(circle)
'''

#pie chart
'''
automobile['aspiration'].value_counts().plot.pie(figsize=(6, 6),autopct='%.2f')
plt.title("Fuel type pie diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');
plt.savefig('NoOfVehiclesToFuelTypePi.png')
'''

#histogram chart
'''
automobile.horsepower[np.abs(automobile.horsepower-automobile.horsepower.mean())<=(3*automobile.horsepower.std())].hist(bins=5,color='red');
plt.title("Horse power histogram")
plt.ylabel('Number of vehicles')
plt.xlabel('Horse power');
plt.savefig('HorsePowerHistogram.png');
'''

#line chart
'''
automobile['num-of-doors'].value_counts().plot(kind='bar',color='purple')
plt.title("Number of doors frequency diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Number of doors');
'''
