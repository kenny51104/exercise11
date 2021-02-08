#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[23]:


import matplotlib.pyplot as plt
import numpy as np


# In[34]:


x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)

plt.plot(x, y_cos)

plt.savefig('filename.png', dpi=300, forma='png')


# In[33]:


x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)

plt.scatter(x, y, s=75, c='red', alpha=.5)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.show()


# In[ ]:




