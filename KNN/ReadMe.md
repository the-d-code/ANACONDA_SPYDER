# Reading Dataset

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>print(df.head())

          In [1]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
             Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
          0   1            5.1           3.5            1.4           0.2  Iris-setosa
          1   2            4.9           3.0            1.4           0.2  Iris-setosa
          2   3            4.7           3.2            1.3           0.2  Iris-setosa
          3   4            4.6           3.1            1.5           0.2  Iris-setosa
          4   5            5.0           3.6            1.4           0.2  Iris-setosa

# Print Specific Line

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>print(df['Species'])

        In [4]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
        0         Iris-setosa
        1         Iris-setosa
        2         Iris-setosa
        3         Iris-setosa
        4         Iris-setosa
                    ...      
        145    Iris-virginica
        146    Iris-virginica
        147    Iris-virginica
        148    Iris-virginica
        149    Iris-virginica
        Name: Species, Length: 150, dtype: object


# COUNT DATA

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>print(df['Species'].value_counts())

      In [6]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
      Iris-setosa        50
      Iris-versicolor    50
      Iris-virginica     50
      Name: Species, dtype: int64

# DataSet Encoding

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')

from sklearn.preprocessing import LabelEncoder
<br>le = LabelEncoder()
<br>df = df.apply(le.fit_transform)
<br>print(df['Species'])

          In [14]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          0      0
          1      0
          2      0
          3      0
          4      0
                ..
          145    2
          146    2
          147    2
          148    2
          149    2
          Name: Species, Length: 150, dtype: int32
       

# Separating feature and target variables

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')

x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>y = df['Species']
<br>print(x)
<br>print(y)


          In [10]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
          0              5.1           3.5            1.4           0.2
          1              4.9           3.0            1.4           0.2
          2              4.7           3.2            1.3           0.2
          3              4.6           3.1            1.5           0.2
          4              5.0           3.6            1.4           0.2
          ..             ...           ...            ...           ...
          145            6.7           3.0            5.2           2.3
          146            6.3           2.5            5.0           1.9
          147            6.5           3.0            5.2           2.0
          148            6.2           3.4            5.4           2.3
          149            5.9           3.0            5.1           1.8
          
          [150 rows x 4 columns]
          0         Iris-setosa
          1         Iris-setosa
          2         Iris-setosa
          3         Iris-setosa
          4         Iris-setosa
                      ...      
          145    Iris-virginica
          146    Iris-virginica
          147    Iris-virginica
          148    Iris-virginica
          149    Iris-virginica
          Name: Species, Length: 150, dtype: object



# dividing Dataset into training and testing dataset
import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')

from sklearn.model_selection import train_test_split
<br>x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>y = df['Species']
<br>x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20)
<br>print(x_test.head())

        In [18]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
             SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
        126            6.2           2.8            4.8           1.8
        127            6.1           3.0            4.9           1.8
        121            5.6           2.8            4.9           2.0
        19             5.1           3.8            1.5           0.3
        101            5.8           2.7            5.1           1.9


# Model Creation

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>y = df['Species']

from sklearn.neighbors import KNeighborsClassifier
<br>model = KNeighborsClassifier()

          In [22]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
       

# Model Training

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>y = df['Species']

from sklearn.model_selection import train_test_split
<br>from sklearn.neighbors import KNeighborsClassifier
<br>from sklearn.preprocessing import LabelEncoder

model = KNeighborsClassifier()
<br>x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20)

model.fit(x_train,y_train)
<br>result = model.predict(x_test)
<br>print(result)

          In [26]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          ['Iris-versicolor' 'Iris-virginica' 'Iris-versicolor' 'Iris-setosa'
           'Iris-versicolor' 'Iris-setosa' 'Iris-setosa' 'Iris-virginica'
           'Iris-virginica' 'Iris-versicolor' 'Iris-versicolor' 'Iris-setosa'
           'Iris-setosa' 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica'
           'Iris-setosa' 'Iris-setosa' 'Iris-virginica' 'Iris-versicolor'
           'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-versicolor'
           'Iris-versicolor' 'Iris-versicolor' 'Iris-virginica' 'Iris-setosa'
           'Iris-versicolor' 'Iris-virginica']


# Model Performance Evalution

import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')

from sklearn.preprocessing import LabelEncoder

#Separating feature and target variables
<br>x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>y = df['Species']

#dividing Dataset into training and testing dataset | random stat for same output
<br>from sklearn.model_selection import train_test_split
<br>x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20, random_state=5)

#Model Creation
<br>from sklearn.neighbors import KNeighborsClassifier
<br>model = KNeighborsClassifier()

#Model Training
<br>model.fit(x_train,y_train)
<br>result = model.predict(x_test)

#Model Performance Evalution
<br>from sklearn.metrics import confusion_matrix
<br>cm = confusion_matrix(result, y_test)
<br>print(cm)
<br>from sklearn.metrics import accuracy_score
<br>acc=accuracy_score(result, y_test)*100
<br>print(acc)

          In [31]: runfile('B:/ICT3-1/OTHER STUUF/SPYDER/KNN MODEL.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
          [[ 8  0  0]
           [ 0  9  0]
           [ 0  2 11]]
          93.33333333333333


# **BAYESIAN ALGORTHAM**

# Read Dataset
import numpy as np
<br>import pandas as pd
<br>df=pd.read_csv('iris.csv')
<br>#print(df.head())

# Dataset Encoding
from sklearn.preprocessing import LabelEncoder
<br>le=LabelEncoder()
<br>df=df.apply(le.fit_transform)
<br>#print(df['Species'].head())

# Separating feature and target variables
x = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
<br>#print(x.head())
<br>y = df['Species']
<br>#print(y.head())

# dividing Dataset into training and testing dataset | random stat for same output
<br>from sklearn.model_selection import train_test_split
<br>x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.20, random_state=5)
<br>#print(x_train.head())

# Model Creation
<br>from sklearn.naive_bayes import GaussianNB
<br>model=GaussianNB()

# Model Training
model.fit(x_train,y_train)
result = model.predict(x_test)
#print(result)

# Model Performance Evalution
from sklearn.metrics import confusion_matrix
<br>cm = confusion_matrix(y_test, result)
<br>#print(cm)

# Accurancy Check
from sklearn.metrics import accuracy_score
<br>acc=accuracy_score(result,y_test)*100
<br>#print(acc)






