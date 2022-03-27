#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None


# In[5]:


data=pd.read_csv('C:/Users/Dell/Downloads/Telco-Customer-Churn.csv',skiprows=2)


# In[6]:


data


# # Compare churn count with respect to gender.

# In[7]:


sns.countplot(data=data,x='gender',hue='Churn',palette=['#432371',"#FAAE7B"])
plt.title("Churn count with respect to gender",fontsize=16)


# # Find out how many female senior citizens there in the dataset

# In[8]:


df=data[data.gender == 'Female']
df.loc[df.SeniorCitizen==1,'SeniorCitizen'] = "Yes"
df.loc[df.SeniorCitizen==0,'SeniorCitizen'] = "No"
sns.countplot(x ='gender', hue = "SeniorCitizen", data = df,palette='dark')
sns.despine()
plt.title( "Female senior citizens there in the dataset",fontsize=16) 
plt.xlabel('')
plt.ylabel('Count',fontsize=14)


# # Compare tenure with Total Charges

# In[9]:


sns.lineplot(data=data, x="tenure", y="TotalCharges",color='red', linewidth=2.5)


# # Find out which contract is preferred by the senior citizen.

# In[10]:


sn= data[data["SeniorCitizen"]==1]
plt.figure(figsize=(6,6))
plt.title( "Distribution of contract is preferred by the senior citizens",fontsize=16) 
sn.Contract.value_counts(sort=True).plot.pie(fontsize=14,autopct ='%1.1f',colors = ['#ff9999','#66b3ff','#99ff99'])
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.show()


# # Payment Method based on gender

# In[11]:


plt.figure(figsize=(10,7))
sns.countplot(data[ 'PaymentMethod' ], hue=data[ 'gender'],palette='Set2')
sns.despine()
plt.title( "Payment Method based on gender",fontsize=16) 
plt.xlabel('Payment Method', fontsize=14)
plt.ylabel('Count',fontsize=14)


# In[ ]:




