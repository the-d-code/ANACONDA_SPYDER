# Count

import pandas as pd

df=pd.read_csv("iris.csv")

cnt=df.loc[df['SepalLengthCm']>5,'SepalLengthCm'].count()
print(cnt)

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
      118

# combine column

import pandas as pd

df=pd.read_csv("iris.csv")

c1=df['SepalLengthCm']
c2=df['PetalLengthCm']

print(c1,"---",c2)

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          0      5.1
          1      4.9
          2      4.7
          3      4.6
          4      5.0
          
          145    6.7
          146    6.3
          147    6.5
          148    6.2
          149    5.9
          Name: SepalLengthCm, Length: 150, dtype: float64 --- 0      1.4
          1      1.4
          2      1.3
          3      1.5
          4      1.4
          
          145    5.2
          146    5.0
          147    5.2
          148    5.4
          149    5.1
          Name: PetalLengthCm, Length: 150, dtype: float64

# Merge two column

import pandas as pd

df=pd.read_csv("iris.csv")

c1=df['SepalLengthCm']
c2=df['PetalLengthCm']

print(c2)


            runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
            0      1.4
            1      1.4
            2      1.3
            3      1.5
            4      1.4
            
            145    5.2
            146    5.0
            147    5.2
            148    5.4
            149    5.1
            Name: PetalLengthCm, Length: 150, dtype: float64

# Side by side


import pandas as pd

df=pd.read_csv("iris.csv")

c1=df['SepalLengthCm']
c2=df['PetalLengthCm']

merge=pd.concat([c1,c2])
print(merge)

          runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
               SepalLengthCm  PetalLengthCm
          0              5.1            1.4
          1              4.9            1.4
          2              4.7            1.3
          3              4.6            1.5
          4              5.0            1.4
          ..             ...            ...
          145            6.7            5.2
          146            6.3            5.0
          147            6.5            5.2
          148            6.2            5.4
          149            5.9            5.1
          
          [150 rows x 2 columns]

# Axis Base

import pandas as pd

df=pd.read_csv("iris.csv")

c1=df['SepalLengthCm']
c2=df['PetalLengthCm']

merge=pd.concat([c1,c2], axis=1)
print(merge)

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
           SepalLengthCm  PetalLengthCm
      0              5.1            1.4
      1              4.9            1.4
      2              4.7            1.3
      3              4.6            1.5
      4              5.0            1.4
      ..             ...            ...
      145            6.7            5.2
      146            6.3            5.0
      147            6.5            5.2
      148            6.2            5.4
      149            5.9            5.1
      
      [150 rows x 2 columns]

# Rename
import pandas as pd

df=pd.read_csv("iris.csv")

c1=df['SepalLengthCm']
c2=df['PetalLengthCm']

merge=pd.concat([c1,c2], axis=1)
merge=merge.rename(columns={'SepalLengthCm':'SLC','PetalLengthCm':'PLC'})
print(merge)


      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/PANDAS.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
           SLC  PLC
      0    5.1  1.4
      1    4.9  1.4
      2    4.7  1.3
      3    4.6  1.5
      4    5.0  1.4
      ..   ...  ...
      145  6.7  5.2
      146  6.3  5.0
      147  6.5  5.2
      148  6.2  5.4
      149  5.9  5.1
      
      [150 rows x 2 columns]
