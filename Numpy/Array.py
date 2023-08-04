
# 1D ARRAY

import numpy as np
n1=np.array([10,30,50,60,90])
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [10 30 50 60 90]

# ARRAY OF ARRAY / 2D ARRAY

import numpy as np
n1=np.array([[10,30,50,60,90],[5,15,25,35,45]])
print(n1)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    [[10 30 50 60 90]
     [ 5 15 25 35 45]]

# SIZE OF ARRAY

import numpy as np
n1=np.array([[10,30,50,60,90],[5,15,25,35,45]])
print(n1.shape)

  import numpy as np
  n1=np.array([[10,30,50,60,90],[5,15,25,35,45]])
  print(n1.shape)

# ARRAY OF MATRIX ZERO

import numpy as np

n1=np.zeros((2,3))
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[0. 0. 0.]
         [0. 0. 0.]]

# ARRAY OF MATRIX VALUE ONE

import numpy as np

n1=np.ones((3,3))
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]

# PROVIDE RANGE TO ARRAY

import numpy as np

n1=np.arange(11,20)
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [11 12 13 14 15 16 17 18 19]

# STEPS IN VALUE OF ARRAY

import numpy as np

n1=np.arange(11,20,2)
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [11 13 15 17 19]

# PRINT ARRAY AND SHAPE OF ARRAY

import numpy as np

n1=np.arange(10,100,10)
print(n1)
print(n1.shape)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [10 20 30 40 50 60 70 80 90]
        (9,)

# CRATE ARRAY BY ASSIGN VALUE

import numpy as np

n1=np.arange(10,100,10)
n1.shape = (3,3)
print(n1)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[10 20 30]
         [40 50 60]
         [70 80 90]]

import numpy as np

n1=np.arange(10,90,10)
n1.shape = (4,2)
print(n1)


        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [[10 20]
         [30 40]
         [50 60]
         [70 80]]

# CREATE RANDOM ARRAY EVERYTIME

import numpy as np 

n1=np.random.randint(1,100,10)
print(n1)
             
        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [17 93 33 81  1 80 33 98 91 22]

# COMBINE 2 NUMPY ARRAY

import numpy as np

n1=np.arange(1,5)
n2=np.arange(11,15)
print(n1)
print(n2)
print(np.hstack((n1,n2)))

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [ 1  2  3  4 11 12 13 14]

#VARTICAL COMBINE

import numpy as np

n1=np.arange(1,5)
n2=np.arange(11,15)
print(n1)
print(n2)
print(np.vstack((n1,n2)))

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [[ 1  2  3  4]
         [11 12 13 14]]

#column stack

import numpy as np

n1=np.arange(1,5)
n2=np.arange(11,15)
print(n1)
print(n2)
print(np.column_stack((n1,n2)))

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
n2=np.arange(11,15)
print(n1)
print(n2)
print(n1+n2)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [12 14 16 18]

#SUBSTRACTION OF ARRAY

import numpy as np

n1=np.arange(1,5)
n2=np.arange(11,15)
print(n1)
print(n2)
print(n1-n2)

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        [1 2 3 4]
        [11 12 13 14]
        [-10 -10 -10 -10]

#MULTIPLICATION

import numpy as np

n1=np.arange(1,5)
n2=np.arange(11,15)
print(n1)
print(n2)
print(n1*n2)

runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
[1 2 3 4]
[11 12 13 14]
[11 24 39 56]

#
#
#
#
#
