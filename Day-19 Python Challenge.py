#!/usr/bin/env python
# coding: utf-8

# # Day-19 Python Challenge

# # Seaborn Library Part - 2

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# ## Bar Plot in Seaborn Library

# In[14]:


df1 = sns.load_dataset("penguins")


# In[19]:


df1.head()


# In[16]:


sns.barplot(x = df1.island, y = df1.bill_length_mm)
plt.show()


# ## Category Function

# In[17]:


sns.barplot(x='island', y='bill_length_mm', data = df1, hue = 'sex')
plt.show()


# In[18]:


sns.displot(df1['flipper_length_mm'])
plt.show()

