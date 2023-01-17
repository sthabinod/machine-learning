import pandas as pd
import numpy as np
import seaborn as sns
import pickle

#Loading Data from CSV file

df=pd.read_csv("Riyadh_weather.csv")
df.head()
df=df.drop(['date'],axis=1)
df.head()

y=df.drop(['Humidity_Max','Dew_Point_Max'],axis=1)

x=df.drop(['Temperature_Max','Pressure_Max'],axis=1)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.15)
from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit(x_train,y_train)
clf.score(x_test,y_test)
print("Accuracy \n",clf.score(x_test,y_test))
linear='linearreg.sav'
pickle.dump(clf, open(linear,'wb'))
#Importing Libraries
#For rainfall
#Importing Libraries
#For rainfall
import pandas as pd
from sklearn.naive_bayes import GaussianNB
#Loading Data from CSV file
dataset = pd.read_csv('Weather.csv')
dataset.head()
#Check if table has missing values
pd.isnull(dataset).any(1).nonzero()[0]
dataset.head()
#Drop rows that have missing values
dataset.drop(pd.isnull(dataset).any(1).nonzero()[0], inplace = True)
dataset=dataset.drop(['DATE'],axis=1)
dataset=dataset.drop(['TMAX'],axis=1)
dataset=dataset.drop(['TMIN'],axis=1)
def replace_yn(val):
    if val == 'False':
        return 0
    else:
        return 1
# normalizing the data (1 for yes & 0 for no)
dataset['RAIN']     = dataset['RAIN'].apply(replace_yn, 1)

r=dataset.drop(['RAIN'],axis=1)

a=dataset.drop(['PRCP'],axis=1)
#splitting the data into train and test
from sklearn.model_selection import train_test_split
r_train, r_test, a_train, a_test = train_test_split(r, a, test_size=0.2)
#Feature Scaling
from sklearn.preprocessing import StandardScaler
scalerx = StandardScaler()
scalery = StandardScaler()
r_train = scalerx.fit_transform(r_train)
r_test  = scalery.fit_transform(r_test)
#Create a Gaussian Classifier
gnb = GaussianNB()
#Train the model using the training sets
gnb.fit(r_train, a_train)

def get_input(data) ->int:
    import pandas
    df = pandas.DataFrame(data = data,index = [0])
    p = clf.predict(df)
    mydic={'temperature': p.item(0),'pressure':p.item(1)}
    return mydic
