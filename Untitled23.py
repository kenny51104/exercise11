#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


stock_data1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock_data2 = pd.read_csv('STOCK_DAY_0050_202010.csv')


# In[21]:


stock_data = pd.concat([stock_data1,stock_data2])


# In[22]:


stock_data.loc[stock_data.open < stock_data.close ]


# In[ ]:




