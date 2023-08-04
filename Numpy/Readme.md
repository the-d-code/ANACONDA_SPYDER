# //------------------------Array------------------------//

# 1D ARRAY

import numpy as np<br>
n1=np.array([10,30,50,60,90])
<br>print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')<br>
        [10 30 50 60 90]<br>

# Array of Array / 2D ARRAY

import numpy as np<br>
n1=np.array([[10,30,50,60,90],[5,15,25,35,45]])
<br>print(n1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')<br>
    [[10 30 50 60 90]<br>
     [ 5 15 25 35 45]]<br>

# SIZE OF ARRAY

import numpy as np<br>
n1=np.array([[10,30,50,60,90],[5,15,25,35,45]])
<br>print(n1.shape)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        (2, 5)

# ARRAY OF MATRIX ZERO

import numpy as np

n1=np.zeros((2,3))<br>
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[0. 0. 0.]
         [0. 0. 0.]]

# ARRAY OF MATRIX VALUE ONE

import numpy as np

n1=np.ones((3,3))<br>
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]

# PROVIDE RANGE TO ARRAY

import numpy as np

n1=np.arange(11,20)<br>
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [11 12 13 14 15 16 17 18 19]

# STEPS IN VALUE OF ARRAY

import numpy as np

n1=np.arange(11,20,2)<br>
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [11 13 15 17 19]

# PRINT ARRAY AND SHAPE OF ARRAY

import numpy as np

n1=np.arange(10,100,10)
<br>print(n1)
<br>print(n1.shape)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [10 20 30 40 50 60 70 80 90]
        (9,)

# CRATE ARRAY BY ASSIGN VALUE

import numpy as np

n1=np.arange(10,100,10)
<br>n1.shape = (3,3)
<br>print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[10 20 30]
         [40 50 60]
         [70 80 90]]

import numpy as np

n1=np.arange(10,90,10)
<br>n1.shape = (4,2)
<br>print(n1)


        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[10 20]
         [30 40]
         [50 60]
         [70 80]]
         
# COMBINE 2 NUMPY ARRAY

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(np.hstack((n1,n2)))

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [ 1  2  3  4 11 12 13 14]

#VARTICAL COMBINE

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(np.vstack((n1,n2)))

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [[ 1  2  3  4]
         [11 12 13 14]]

#column stack

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(np.column_stack((n1,n2)))

runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
[1 2 3 4]
[11 12 13 14]
[[ 1 11]
 [ 2 12]
 [ 3 13]
 [ 4 14]]

#ADDITION OF ARRAY

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(n1+n2)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [12 14 16 18]

#SUBSTRACTION OF ARRAY

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(n1-n2)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [-10 -10 -10 -10]

#MULTIPLICATION

import numpy as np

n1=np.arange(1,5)
<br>n2=np.arange(11,15)
<br>print(n1)
<br>print(n2)
<br>print(n1*n2)

runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
[1 2 3 4]
[11 12 13 14]
[11 24 39 56]

#
#
#
#
#
#
#
