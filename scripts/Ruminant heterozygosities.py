#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches


# In[11]:


data = pd.read_csv("ruminantHets.csv", sep=";")
data.sort_values("Heterozygosity", ascending=False)


# In[74]:


plt.figure(figsize=(20,10))
sns.scatterplot(data.sort_values("Heterozygosity", ascending=False)["Species"], data.sort_values("Heterozygosity", ascending=False)["Heterozygosity"])
plt.hlines(0.002891, -2, 19.5, colors='Brown', linestyles='solid', label='Desert')
plt.hlines(0.004233, -2, 42, colors='Red', linestyles='solid', label='Ghana')
plt.hlines(0.003757 , -2, 42, colors='Blue', linestyles='solid', label='Kenya')
plt.hlines(0.003569, -2, 42, colors='Purple', linestyles='solid', label='Tanzania')
plt.hlines(0.003293, -2, 42, colors='Green', linestyles='solid', label='Zambia')
plt.hlines(0.003061, -2, 42, colors='Orange', linestyles='solid', label='Zimbabwe')
plt.hlines(0.002891, 19.5, 42, colors='Yellow', linestyles='solid', label='Namibia')

plt.xticks(rotation=90)
plt.gca().margins(x=0.005)
plt.title("Heterozygosities of ruminants obtained from the ruminants genome project", fontsize=20)
plt.legend(loc="lower left", prop={'size': 16}, title="Warthog heterozygosities")
plt.savefig('rumHetwithWart.pdf', bbox_inches = 'tight', pad_inches = 0.1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




