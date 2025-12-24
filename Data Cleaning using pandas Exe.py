#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df =  pd.read_csv("customer_shopping_behavior.csv")


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe(include = "all")


# In[8]:


df.isnull().sum()


# In[9]:


df.groupby("Category")["Review Rating"].median()


# In[10]:


df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x : x.median())


# In[10]:


df.isnull().sum()


# In[11]:


df.columns = df.columns.str.lower()


# In[12]:


df.columns = df.columns.str.replace( " ", "_")


# In[13]:


df = df.rename(columns={"purchase_amount_(usd)":"purchase_amount"})


# In[14]:


df.columns


# # create a column age group

# In[15]:





# In[16]:


df[["age","age_group"]].head()


# # purchase_frequency_days

# In[17]:


frequecny_mapping = { "Fortnightly" : 14, "Weekly" : 7, "Monthly" : 30 , "Quarterly" : 90, "Bi-weekly" : 14, "Annually" : 365, "Every 3 Months" : 90}

df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequecny_mapping)


# In[18]:


df


# In[19]:


df[["purchase_frequency_days","frequency_of_purchases"]].head(10)


# In[20]:


df[["discount_applied","promo_code_used"]].head(10)


# In[21]:


(df["discount_applied"] == df["promo_code_used"]).all()


# In[22]:


del df["promo_code_used"]


# In[23]:


df


# In[24]:


get_ipython().system('pip install sqlalchemy mysql-connector-python')


# In[25]:


from sqlalchemy import create_engine


# In[26]:


engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost:3306/customer_behavior")


# In[27]:


df.to_sql(
    name="customer_beh",
    con=engine,
    if_exists="replace",
    index=False
)


# In[24]:


df.isnull().sum()


# In[29]:


df


# In[ ]:




