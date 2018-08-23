
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/realpython/python-data-cleaning/master/Datasets/BL-Flickr-Images-Book.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
            'Engraver',
           'Contributors',
           'Issuance type',
          'Shelfmarks']

df.drop(to_drop, inplace=True, axis=1)


# In[6]:


df.head()


# In[7]:


df['Identifier'].is_unique


# In[8]:


df = df.set_index('Identifier')
df.head()


# In[9]:


df.loc[206]


# In[10]:


df.get_dtype_counts()


# In[11]:


df.loc[1905:, 'Date of Publication'].head(10)


# In[14]:


extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

extr.head()


# In[15]:


#change datas from objects to integers....as they are numnbers...duh

df['Date of Publication'] = pd.to_numeric(extr)
df['Date of Publication'].dtype


# In[17]:


#Check how many valid values remaind after conversion from text to numbers

df['Date of Publication'].isnull().sum() / len(df)


# In[18]:


df['Place of Publication'].head(10)


# In[23]:


df.loc[4157862]


# In[25]:


df.loc[4159587]


# In[24]:


pub = df['Place of Publication']
london = pub.str.contains('London')
london[:5]


# In[26]:


oxford = pub.str.contains ('Oxford')


# In[28]:


#Remove hyphens from names, standardize capital letters

df['Place of Publication'] = np.where(london, 'London',
                                     np.where(oxford, 'Oxford',
                                             pub.str.replace('-', '')))

df['Place of Publication'].head()


# In[29]:


df.head()

