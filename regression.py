#import pandas as pd

#data=pd.read_excel(r"C:__")

#data

#data.head() 
#shows only 5 rows

#data.dtypes

#from sklearn import preprocessing

#label=preprocessing.LabelEncoder()

data['RskMortScore']=label.fit_transform(data['RskMortScore']) 
#convert obj to int

data['SeverityScore']=label.fit_transform(data['SeverityScore']) 

#data.head()

#data.dtypes

#data1=data.loc[:,['SeverityScore,'RskMortScore','LOS','Mortality','TOTALCHG']]
#features must be numbers

#data2=data1.dropna()
#data cleaning to take out blanks.

#from sklearn.model_selection import train_test_split
#x=data2.loc[:,['SeverityScore,'RskMortScore','LOS','TOTALCHG']]
#y=data2.loc[:,['Mortality']]

#x.dtypes

#y

#x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=200)
#test_size is percentage
#random_state can be any number

#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
#clf=LogisticRegression().fit(x_train,y_train)

#y_pred=clf.predict(x_test)

#print(accuracy_score(y_test, y_pred))

# find correlation score


