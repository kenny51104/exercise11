#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array1 = np.array([[10, 8], [3, 5]])


# In[6]:


array2 = np.linalg.inv(array1)
array2


# In[30]:


array3 = np.dot(array1, array2)
array3


# In[20]:


print("It is a 2*2 identity matrix")


# In[21]:


w, v = np.linalg.eig(array3)


# In[22]:


w


# In[23]:


v


# In[24]:


u, s, vh = np.linalg.svd(array3)


# In[25]:


u


# In[26]:


v


# In[27]:


vh


# In[ ]:




