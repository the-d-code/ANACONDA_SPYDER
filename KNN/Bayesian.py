import numpy as np
import pandas as pd
df=pd.read_csv('iris.csv')
print(df.head())
              In [2]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                 Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
              0   1            5.1           3.5            1.4           0.2  Iris-setosa
              1   2            4.9           3.0            1.4           0.2  Iris-setosa
              2   3            4.7           3.2            1.3           0.2  Iris-setosa
              3   4            4.6           3.1            1.5           0.2  Iris-setosa
              4   5            5.0           3.6            1.4           0.2  Iris-setosa

# Dataset Encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df=df.apply(le.fit_transform)
print(df['Species'].head())

              In [3]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
              0    0
              1    0
              2    0
              3    0
              4    0
              Name: Species, dtype: int32


#Separating feature and target variables
x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
print(x.head())
            
            In [4]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
            0              8            14              4             1
            1              6             9              4             1
            2              4            11              3             1
            3              3            10              5             1
            4              7            15              4             1

# Separating feature and target variables
x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
#print(x.head())
y = df['Species']
print(y.head())


            
            In [6]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
            0    0
            1    0
            2    0
            3    0
            4    0
            Name: Species, dtype: int32


# dividing Dataset into training and testing dataset | random stat for same output
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.20, random_state=5)
print(x_train.head())

        runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
            SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
        39              8            13              5             1
        53             12             2             16             9
        79             14             5             11             6
        10             11            16              5             1
        50             27            11             23            10  

# Model Creation
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

# Model Training
model.fit(x_train,y_train)
result = model.predict(x_test)
print(result)


      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
      [1 1 2 0 2 1 0 2 0 1 1 1 2 2 0 0 2 2 0 0 1 2 0 1 1 2 1 1 1 2]

#Model Performance Evalution
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, result)
print(cm)

      runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
      [[ 8  0  0]
       [ 0 10  1]
       [ 0  2  9]]

# Accurancy Check
from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test, result)*100
print(acc)

    runfile('B:/ICT3-1/OTHER STUUF/SPYDER/Bayesian.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
    90.0


