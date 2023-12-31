# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:29:39 2023

@author: admin
"""

# READ FILE

import pandas as pd

df=pd.read_csv("iris.csv")
print(df)

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                Id  SepalLengthCm  ...  PetalWidthCm         Species
          0      1            5.1  ...           0.2     Iris-setosa
          1      2            4.9  ...           0.2     Iris-setosa
          2      3            4.7  ...           0.2     Iris-setosa
          3      4            4.6  ...           0.2     Iris-setosa
          4      5            5.0  ...           0.2     Iris-setosa
          ..   ...            ...  ...           ...             ...
          145  146            6.7  ...           2.3  Iris-virginica
          146  147            6.3  ...           1.9  Iris-virginica
          147  148            6.5  ...           2.0  Iris-virginica
          148  149            6.2  ...           2.3  Iris-virginica
          149  150            5.9  ...           1.8  Iris-virginica
          
          [150 rows x 6 columns]

#DESCRIBE FILE DATA

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.describe())

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
    count  150.000000     150.000000    150.000000     150.000000    150.000000
    mean    75.500000       5.843333      3.054000       3.758667      1.198667
    std     43.445368       0.828066      0.433594       1.764420      0.763161
    min      1.000000       4.300000      2.000000       1.000000      0.100000
    25%     38.250000       5.100000      2.800000       1.600000      0.300000
    50%     75.500000       5.800000      3.000000       4.350000      1.300000
    75%    112.750000       6.400000      3.300000       5.100000      1.800000
    max    150.000000       7.900000      4.400000       6.900000      2.500000


#TECHNICAL INFO OF DATASET
import pandas as pd

df=pd.read_csv("iris.csv")
print(df.info())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          <class 'pandas.core.frame.DataFrame'>
          RangeIndex: 150 entries, 0 to 149
          Data columns (total 6 columns):
           #   Column         Non-Null Count  Dtype  
          ---  ------         --------------  -----  
           0   Id             150 non-null    int64  
           1   SepalLengthCm  150 non-null    float64
           2   SepalWidthCm   150 non-null    float64
           3   PetalLengthCm  150 non-null    float64
           4   PetalWidthCm   150 non-null    float64
           5   Species        150 non-null    object 
          dtypes: float64(4), int64(1), object(1)
          memory usage: 7.2+ KB
          None

# HEAD TOP 5 RECORDS / Selected

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.head())

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
           Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
        0   1            5.1           3.5            1.4           0.2  Iris-setosa
        1   2            4.9           3.0            1.4           0.2  Iris-setosa
        2   3            4.7           3.2            1.3           0.2  Iris-setosa
        3   4            4.6           3.1            1.5           0.2  Iris-setosa
        4   5            5.0           3.6            1.4           0.2  Iris-setosa

#

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.head(8))

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
         Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
      0   1            5.1           3.5            1.4           0.2  Iris-setosa
      1   2            4.9           3.0            1.4           0.2  Iris-setosa
      2   3            4.7           3.2            1.3           0.2  Iris-setosa
      3   4            4.6           3.1            1.5           0.2  Iris-setosa
      4   5            5.0           3.6            1.4           0.2  Iris-setosa
      5   6            5.4           3.9            1.7           0.4  Iris-setosa
      6   7            4.6           3.4            1.4           0.3  Iris-setosa
      7   8            5.0           3.4            1.5           0.2  Iris-setosa

# TAIL / SELECTED LAST RECORDS

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.tail())

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
            Id  SepalLengthCm  ...  PetalWidthCm         Species
      145  146            6.7  ...           2.3  Iris-virginica
      146  147            6.3  ...           1.9  Iris-virginica
      147  148            6.5  ...           2.0  Iris-virginica
      148  149            6.2  ...           2.3  Iris-virginica
      149  150            5.9  ...           1.8  Iris-virginica
      
      [5 rows x 6 columns]

#

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.tail(10))


      In [10]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
            Id  SepalLengthCm  ...  PetalWidthCm         Species
      140  141            6.7  ...           2.4  Iris-virginica
      141  142            6.9  ...           2.3  Iris-virginica
      142  143            5.8  ...           1.9  Iris-virginica
      143  144            6.8  ...           2.3  Iris-virginica
      144  145            6.7  ...           2.5  Iris-virginica
      145  146            6.7  ...           2.3  Iris-virginica
      146  147            6.3  ...           1.9  Iris-virginica
      147  148            6.5  ...           2.0  Iris-virginica
      148  149            6.2  ...           2.3  Iris-virginica
      149  150            5.9  ...           1.8  Iris-virginica
      
      [10 rows x 6 columns]


# Display top 5 and bottom 5 value of column

import pandas as pd

df=pd.read_csv("iris.csv")
print(df['Species'])

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
      0         Iris-setosa
      1         Iris-setosa
      2         Iris-setosa
      3         Iris-setosa
      4         Iris-setosa
           
      145    Iris-virginica
      146    Iris-virginica
      147    Iris-virginica
      148    Iris-virginica
      149    Iris-virginica
      Name: Species, Length: 150, dtype: object

# top 10 records of specific column

import pandas as pd

df=pd.read_csv("iris.csv")
print(df['Species',].head(10))

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          0    Iris-setosa
          1    Iris-setosa
          2    Iris-setosa
          3    Iris-setosa
          4    Iris-setosa
          5    Iris-setosa
          6    Iris-setosa
          7    Iris-setosa
          8    Iris-setosa
          9    Iris-setosa
          Name: Species, dtype: object

# Show column selected


import pandas as pd

df=pd.read_csv("iris.csv")
print(df[['PetalWidthCm','Species']].head())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
             PetalWidthCm      Species
          0           0.2  Iris-setosa
          1           0.2  Iris-setosa
          2           0.2  Iris-setosa
          3           0.2  Iris-setosa
          4           0.2  Iris-setosa


# CHECK NULL CALUE

import pandas as pd

df=pd.read_csv("iris.csv")
print(df[['PetalWidthCm','Species']].head().isnull())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
             PetalWidthCm  Species
          0         False    False
          1         False    False
          2         False    False
          3         False    False
          4         False    False

# CHECK NULL FROM ALL

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.head().isnull())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm  Species
          0  False          False         False          False         False    False
          1  False          False         False          False         False    False
          2  False          False         False          False         False    False
          3  False          False         False          False         False    False
          4  False          False         False          False         False    False



# SPECIFIC ITEM OF COLUMN

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.at[2,'Species'])

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          Iris-setosa


# location of data


import pandas as pd

df=pd.read_csv("iris.csv")
print(df.loc[2])

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          Id                         3
          SepalLengthCm            4.7
          SepalWidthCm             3.2
          PetalLengthCm            1.3
          PetalWidthCm             0.2
          Species          Iris-setosa
          Name: 2, dtype: object

# INT location or value 

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.iloc[2,2])

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          3.2


# FIRST 2 ROW AND COLUMN

import pandas as pd

df=pd.read_csv("iris.csv")
print(df.iloc[0:2,0:2])

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
             Id  SepalLengthCm
          0   1            5.1
          1   2            4.9

# Frequency count

import pandas as pd

df=pd.read_csv("iris.csv")
print(df['Species'].value_counts())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          Iris-setosa        50
          Iris-versicolor    50
          Iris-virginica     50
          Name: Species, dtype: int64


# 
import pandas as pd

df=pd.read_csv("iris.csv")

from numpy import NaN
df.at[1, 'SepalLenghtCm']=NaN
print(df['SepalLenghtCm'].head())


          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          0   NaN
          1   NaN
          2   NaN
          3   NaN
          4   NaN
          Name: SepalLenghtCm, dtype: float64

# isna CHECK THE VALUE IS NAME OR NOT

import pandas as pd

df=pd.read_csv("iris.csv")

from numpy import NaN

df.loc[1, 'SepalLenghtCm']=NaN
print(df['SepalLenghtCm'].isna().head())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          0    True
          1    True
          2    True
          3    True
          4    True
          Name: SepalLenghtCm, dtype: bool
          
          This version of python seems to be incorrectly compiled
          (internal generated filenames are not absolute).
          This may make the debugger miss breakpoints.
          Related bug: http://bugs.python.org/issue1666807


# Sum Of value

import pandas as pd

df=pd.read_csv("iris.csv")

from numpy import NaN

df.loc[1, 'SepalLenghtCm']=NaN
print(df['SepalLenghtCm'].isna().sum())

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          150

#


import pandas as pd

df=pd.read_csv("iris.csv")

from numpy import NaN

df.loc[1, 'SepalLenghtCm']=NaN
print(df['SepalLenghtCm'].isna().sum())
print(df.isna().sum())

          
          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          150
          Id                 0
          SepalLengthCm      0
          SepalWidthCm       0
          PetalLengthCm      0
          PetalWidthCm       0
          Species            0
          SepalLenghtCm    150
          dtype: int64

# Replace value / change cell value

import pandas as pd

df=pd.read_csv("iris.csv")

from numpy import NaN

df.at[1, 'SepalLenghtCm']=NaN

avg=df['SepalLenghtCm'].mean()
df=df['SepalLenghtCm'].fillna(avg)
print(df.head())


# Count value

import pandas as pd

df=pd.read_csv("iris.csv")

ds=df(['Species'].value_counts())



# Replcae value by assgine new value

import pandas as pd

df=pd.read_csv("iris.csv")

ds=df['Species'].map({'Iris-setosa':0,'Iris-versicolor':1})
print(ds.tail())

# 

import pandas as pd

df=pd.read_csv("iris.csv")

ds=df['Species'].map({'Iris-setosa':0,'Iris-versicolor':1})
print(ds)


