#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np


# In[22]:


dt = np.dtype({'names':('name','sex','weight','rank','myopia'), 'formats':('U5','U5','f','i','?')})


# In[23]:


a = np.zeros(8, dtype=dt)
a


# In[24]:


name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]


# In[25]:


a['name'] = name_list
a['sex'] = sex_list
a['weight'] = weight_list
a['rank'] = rank_list
a['myopia'] = myopia_list


# In[26]:


print(a)


# In[36]:


np.mean(a['weight'])


# In[44]:


boy_weight = np.where(a['sex'] == 'boy')[0]
np.mean(a['weight'][boy_weight])


# In[43]:


girl_weight = np.where(a['sex'] == 'girl')[0]
np.mean(a['weight'][girl_weight])


# In[ ]:





# In[ ]:




