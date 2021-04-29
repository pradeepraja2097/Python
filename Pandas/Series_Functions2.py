import pandas as pd 
import numpy as np 

#DataFrame inrandon format

dates=pd.date_range('today',periods=6)
number=np.random.randn(6,4)
columns=['a','b','c','d']

dataframe=pd.DataFrame (number,index=dates,columns=['a','b','c','d'])

print(dataframe)

# DataFrame in Dictionary Format

Data={
    'animal':['cat','snake','Dog','parrot','Buffalo'],
    'age':['2','3','4','5','1'],
    'visit':['1','2','3','4','5'],
    'Priority':['yes','No','yes','No','yes']
}

labels=['a','b','c','d','e']

dataframe2=pd.DataFrame(Data,index=labels)
print(dataframe2)
#Dateframe filter by head and tail function
print(dataframe2.head(1))

print(dataframe2.tail(3))

print(Data.values())

print(dataframe2.sort_values(by='age'))
