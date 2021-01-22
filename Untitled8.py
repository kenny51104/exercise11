#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


english_score = np.array([55, 89, 76, 65, 48, 70])
math_score = np.array([60, 85, 60, 68, 55, 60])
chinese_score = np.array([65, 90, 82, 72, 66, 77])


# In[11]:


a = np.greater(english_score, math_score)
np.sum(a!=0)


# In[15]:


b = np.logical_and(chinese_score > english_score, chinese_score > math_score) 
c = np.all(b)
c


# In[ ]:




