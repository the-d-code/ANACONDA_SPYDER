/------------------------------------------------------
# ARRAY
/------------------------------------------------------


# 1D ARRAY SERIES

import pandas as pd

S1=pd.Series([2,.4,6,8,10])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    0     2.0
    1     0.4
    2     6.0
    3     8.0
    4    10.0
    dtype: float64

# 1D ARRAY SERIES OF WORDS/LIST

import pandas as pd

S1=pd.Series(["PYTHON","PROGRAM"])
<br>print(S1)
    
    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    0     PYTHON
    1    PROGRAM
    dtype: object

# 1D ARRAY SERIES OF COMBINATION

import pandas as pd

S1=pd.Series([5,10,"PYTHON","PROGRAM"])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    0          5
    1         10
    2     PYTHON
    3    PROGRAM
    dtype: object

# 1D ARRAY INT DATA TYPE

import pandas as pd

S1=pd.Series([2,4,5,6,8,10])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    0     2
    1     4
    2     5
    3     6
    4     8
    5    10
    dtype: int64

# 2D ARRAY LIST

import pandas as pd

S1=pd.Series([[5,10],[20,25],[30,40]])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    0     [5, 10]
    1    [20, 25]
    2    [30, 40]
    dtype: object


# CREATE OWN INDEX TO ASSIGN VALUE

import pandas as pd

S1=pd.Series(data=[5,10,15,20],index=['A','B','C','D'])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    A     5
    B    10
    C    15
    D    20
    dtype: int64

import pandas as pd

S1=pd.Series(data=[5,10,15,20],index=['Hello','Python','Set','D'])<br>
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    Hello      5
    Python    10
    Set       15
    D         20
    dtype: int64


/------------------------------------------------------
# CSV FILE 
/------------------------------------------------------




# READ FILE

import pandas as pd

df=pd.read_csv("iris.csv")
<br>print(df)

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

# DESCRIBE FILE DATA

import pandas as pd

df=pd.read_csv("iris.csv")
<br>print(df.describe())

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


# TECHNICAL INFO OF DATASET

import pandas as pd

df=pd.read_csv("iris.csv")
<br>print(df.info())

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
<br>print(df.head())

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
<br>print(df.head(8))

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
<br>print(df.tail())

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



