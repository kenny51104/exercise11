#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[34]:


v0 = 20


# In[33]:


v1 = 20000


# In[35]:


v2 = 20*np.log10(v1/v0)
v2


# In[23]:


c1 = 30
c2 = 50


# In[36]:


d1 = (10**(c1/20))*v0
d1


# In[37]:


d2 = (10**(c2/20))*v0
d2


# In[41]:


np.round(d1/d2, decimals =  3)


# In[ ]:




