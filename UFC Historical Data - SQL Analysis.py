#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

UFCdf = pd.read_csv('UFChistoricaldata.csv')
UFCdf


# In[7]:


conn = sqlite3.connect(':memory:')
UFCdf.to_sql('ufc_data', conn, index = False, if_exists = 'replace')


# In[14]:


red_corner_metrics_query = """
    SELECT 
        R_fighter,
        R_Reach_cms as Red_Reach,
        R_Height_cms as Red_Height
    FROM
        ufc_data
    GROUP BY
        R_fighter
    ORDER BY
        Red_Height DESC
"""

red_corner_metrics = pd.read_sql(red_corner_metrics_query, conn)
    


# In[15]:


red_corner_metrics


# In[12]:


plt.figure(figsize=(12, 6))
sns.barplot(x='R_fighter', y='Red_Reach', data=red_corner_metrics.head(15), color='blue', label='Reach')
sns.barplot(x='R_fighter', y='Red_Height', data=red_corner_metrics.head(15), color='red', label='Height')
plt.title('UFC Fighters - Measurements for Red Corner')
plt.xlabel('Fighter ID')
plt.ylabel('Measurements for Red Corner')
plt.legend()
plt.show()


# In[13]:


plt.figure(figsize=(12, 6))
sns.barplot(x='R_fighter', y='Red_Reach', data=red_corner_metrics, color='blue', label='Reach')
sns.barplot(x='R_fighter', y='Red_Height', data=red_corner_metrics, color='red', label='Height')
plt.title('UFC Fighters - Measurements for Red Corner')
plt.xlabel('Fighter ID')
plt.ylabel('Measurements for Red Corner')
plt.legend()
plt.show()


# In[20]:


red_measurements_comparision_query = """
    SELECT
        R_fighter,
        R_Reach_cms as Red_Reach,
        R_Height_cms as Red_Height,
        CASE 
            WHEN R_Reach_cms > R_Height_cms THEN 'Greater'
            WHEN R_Reach_cms < R_Height_cms THEN 'Less'
            ELSE 'Equal'
        END AS comparison_result
    FROM
        ufc_data
"""
red_measurement_comparision = pd.read_sql_query(red_measurements_comparision_query, conn)


# In[21]:


red_measurement_comparision


# In[23]:


code_counts = red_measurement_comparision['comparison_result'].value_counts()

plt.figure(figsize = (8,6))
plt.bar(code_counts.index, code_counts, color = 'r')
plt.title('Number of Occurences')
plt.xlabel('Comparision')
plt.ylabel('Number of Occurences')
plt.show()


# In[26]:


red_corner_metrics_query = """
    SELECT 
        B_fighter,
        B_Reach_cms as Blue_Reach,
        B_Height_cms as Blue_Height
    FROM
        ufc_data
    GROUP BY
        B_fighter
    ORDER BY
        Blue_Height DESC
"""

blue_corner_metrics = pd.read_sql(red_corner_metrics_query, conn)
    


# In[27]:


blue_corner_metrics


# In[28]:


plt.figure(figsize=(12, 6))
sns.barplot(x='B_fighter', y='Blue_Reach', data=blue_corner_metrics.head(15), color='blue', label='Reach')
sns.barplot(x='B_fighter', y='Blue_Height', data=blue_corner_metrics.head(15), color='red', label='Height')
plt.title('UFC Fighters - Measurements for Blue Corner')
plt.xlabel('Fighter ID')
plt.ylabel('Measurements for Blue Corner')
plt.legend()
plt.show()


# In[29]:


plt.figure(figsize=(12, 6))
sns.barplot(x='B_fighter', y='Blue_Reach', data=blue_corner_metrics, color='blue', label='Reach')
sns.barplot(x='B_fighter', y='Blue_Height', data=blue_corner_metrics, color='red', label='Height')
plt.title('UFC Fighters - Measurements for Blue Corner')
plt.xlabel('Fighter ID')
plt.ylabel('Measurements for Blue Corner')
plt.legend()
plt.show()


# In[31]:


red_measurements_comparision_query = """
    SELECT
        B_fighter,
        B_Reach_cms as Blue_Reach,
        B_Height_cms as Blue_Height,
        CASE 
            WHEN B_Reach_cms > B_Height_cms THEN 'Greater'
            WHEN B_Reach_cms < B_Height_cms THEN 'Less'
            ELSE 'Equal'
        END AS comparison_result
    FROM
        ufc_data
"""
blue_measurement_comparision = pd.read_sql_query(red_measurements_comparision_query, conn)
blue_measurement_comparision


# In[32]:


code_counts = blue_measurement_comparision['comparison_result'].value_counts()

plt.figure(figsize = (8,6))
plt.bar(code_counts.index, code_counts, color = 'b')
plt.title('Number of Occurences')
plt.xlabel('Comparision')
plt.ylabel('Number of Occurences')
plt.show()


# In[ ]:




