# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 21:41:41 2021

@author: Saeed Ramadan
"""
#import lib
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
#read dataset
dataset = pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()
#sort dataset
dataset.sort_values("Title",inplace = True)

#drop duplicates
dataset.drop_duplicates(subset ="Title",
					keep = "first", inplace = True)
x = dataset.iloc[:, :-1].values
df=pd.DataFrame(x)
#handle miss data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values =np.nan , strategy = 'most_frequent')
imputer.fit(x)
x=imputer.transform(x)

# the most freqancy companies
sorted_counts = dataset['Company'].value_counts()[:6]
plt.pie(sorted_counts, labels = sorted_counts.index, autopct='%1.0f%%')
plt.title("high hired company", fontsize=20)
plt.axis('square');
#most popular jop & bar char 
x= dataset['Title'].value_counts()[:5]
x.plot(kind='barh',figsize=(15,15), color="green")

x= dataset['Location'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")

x= dataset['Country'].value_counts()[:10]
x.plot(kind='bar',figsize=(15,10), color="green")