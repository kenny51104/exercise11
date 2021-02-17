#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


pip install notebook


# In[3]:


df_red = pd.read_csv('winequality_red.csv')
df_white = pd.read_csv('winequality_white.csv')


# In[4]:


df_red['color'] = 'R'
df_white['color'] = 'W'

df_all = pd.concat([df_red,df_white],axis=0)

df_all.head()


# In[5]:


df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
# 檢查合併後的資料集
df_all.head()


# In[6]:


df_all = pd.get_dummies(df_all, columns=['color'])
df_all.isnull().sum()


# In[7]:


df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)
plt.tight_layout()


# In[8]:


f, ax = plt.subplots(figsize=(10, 6))
b = sns.heatmap(df_all.corr(), annot=True, linewidths=.05, ax=ax)
f.subplots_adjust(top=0.93)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top-0.5)
title = f.suptitle('Correlation Heatmap for wine attributes', fontsize=1)


# In[9]:


a = sns.jointplot('fixed_acidity', 'citric_acid', data=df_all, kind='reg')
b = sns.jointplot('alcohol','citric_acid', data=df_all, kind='reg')
c = sns.jointplot('volatile_acidity', 'citric_acid', data=df_all, kind='reg')


# In[10]:


sns.catplot(x='quality', y='pH',kind='swarm', data = df_all)


# In[ ]:


sns.set(style='white')

g = sns.PairGrid(df_all)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)

