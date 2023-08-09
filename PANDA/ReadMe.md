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

# 

import pandas as pd

S1=pd.Series(data=[5,10,15,20],index=['Hello','Python','Set','D'])
<br>print(S1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    Hello      5
    Python    10
    Set       15
    D         20
    dtype: int64


