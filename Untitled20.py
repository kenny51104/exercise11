#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().system('pip install openpyxl')
get_ipython().system('pip install XLRD')


# In[6]:


boston_data = pd.read_csv('boston.csv', header = 0 ,usecols = ['CHAS', 'NOX', 'RM'])
boston_data.to_excel('my_boston_data.xlsx')


# In[ ]:




