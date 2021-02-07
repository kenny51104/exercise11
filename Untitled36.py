#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)
series


# In[10]:


series.to_period('W')


# In[9]:


series.resample('W').mean()


# In[ ]:




