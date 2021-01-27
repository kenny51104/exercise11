#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array1 = np.array(range(30))
array2 = np.array([2, 3, 5])


# In[7]:


np.savez('array.npz', array1, array2)


# In[48]:


load_array = np.load('array.npz')
array3 = np.array([[4, 5, 6],[1, 2, 3]])
np.savez('new_array.npz', load_array['arr_0'], load_array['arr_1'], array3)

