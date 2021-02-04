#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


boston_data = pd.read_csv('boston.csv')
boston_data


# In[27]:


df = pd.read_csv("boston.csv")
df.boxplot()


# In[29]:


print("TAX", "B")


# In[19]:


df.plot.scatter(x ='NOX', y = 'DIS')


# In[20]:


print("成反比關係")


# In[ ]:




