#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


array1 = np.array(range(30))
array1


# In[7]:


a = array1.reshape(5, 6, order="f")
a


# In[8]:


np.where(a%6==1)


# In[ ]:




