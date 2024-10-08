# -*- coding: utf-8 -*-
"""EDA of Road accident data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gfyEARsqp3WDxPU67azC8KSKQsYX6f1J
"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('/content/drive/MyDrive/RTA Dataset.csv')
df.head()

df.shape

df_cause=df['Cause_of_accident'].unique()
print(df_cause)

df.columns

df.isnull().sum ()

df.duplicated().sum()

df_caused=df['Road_surface_conditions'].unique()
print(df_caused)

df['Time']= pd.to_datetime(df['Time'])

df.describe(include="all")

df.groupby('Accident_severity').size()

df['Number_of_casualties'].value_counts()

plt.figure(figsize=(10,7))
sns.boxplot(data=df, y='Number_of_vehicles_involved', x='Number_of_casualties')
plt.show()

sns.boxplot(data=df, y='Number_of_casualties')
plt.show()

sns.boxplot(data=df, y='Number_of_vehicles_involved')
plt.show()

sns.scatterplot(x=df['Number_of_vehicles_involved'], y=df['Number_of_casualties'])
plt.show()

sns.pairplot(df[['Number_of_vehicles_involved','Number_of_casualties']])
plt.show()

correlation_matrix = df[['Number_of_vehicles_involved','Number_of_casualties']].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

plt.figure(figsize=(10,7))
plt.pie(x=df['Accident_severity'].value_counts().values,
        labels=df['Accident_severity'].value_counts().index,
        autopct='%2.2f%%')
plt.show()

sns.barplot(x=df['Road_surface_conditions'], y=df['Accident_severity'])
plt.show()

lists=['Vehicle_driver_relation', 'Work_of_casuality', 'Fitness_of_casuality','Day_of_week','Casualty_severity','Time','Sex_of_driver','Educational_level','Defect_of_vehicle','Owner_of_vehicle','Service_year_of_vehicle', 'Road_surface_type','Sex_of_casualty']
df.drop(columns = lists, inplace=True)

df.shape

df.columns

df['Driving_experience'].fillna(df['Driving_experience'].mode()[0], inplace=True)
df['Type_of_vehicle'].fillna(df['Type_of_vehicle'].mode()[0], inplace=True)
df['Area_accident_occured'].fillna(df['Area_accident_occured'].mode()[0], inplace=True)
df['Road_allignment'].fillna(df['Road_allignment'].mode()[0], inplace=True)
df['Type_of_collision'].fillna(df['Type_of_collision'].mode()[0], inplace=True)
df['Vehicle_movement'].fillna(df['Vehicle_movement'].mode()[0], inplace=True)
df['Lanes_or_Medians'].fillna(df['Lanes_or_Medians'].mode()[0], inplace=True)
df['Types_of_Junction'].fillna(df['Types_of_Junction'].mode()[0], inplace=True)

df.isnull().sum()

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df=df.apply(LE.fit_transform)

df.corr()

plt.figure(figsize=[25,15])
sns.heatmap(df.corr(),annot=True)