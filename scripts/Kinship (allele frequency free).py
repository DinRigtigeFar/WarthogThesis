#!/usr/bin/env python
# coding: utf-8

# ## Loading data and plotting:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[185]:


data = pd.read_csv("desert_warthogs_relate", sep="\t")
ghana = pd.read_csv("Ghana_relate", sep="\t")
#related_vals = ghana[ghana["R0"]<0.0001].iloc[:,[0,1,28,29,30]]
ghana[ghana["a"]==4].iloc[:,[0,1,28,29,30]]
#related_vals.to_csv("Ghana_relate_vals.csv", sep=",")


# ### Plot the data:

# In[184]:


ghana_R1R0 = sns.scatterplot(ghana["R1"], ghana["R0"], color="white", ec="black")
related = []
for line in range(0,ghana.shape[0]):
    if ghana["R1"][line]>4:
        ghana_R1R0.text(ghana["R1"][line]+0.2, ghana["R0"][line], 
                     s=f'{ghana["a"][line]},{ghana["b"][line]}', horizontalalignment='left', 
                        size='large', color='red', rotation=45)
        related.append(f'{ghana["a"][line]},{ghana["b"][line]}')
ghana_R1R0.set_xlim(4,8)
ghana_R1R0.set_ylim(-0.00001, 0.00001)
#plt.show()
#related


# In[174]:


fig, ax = plt.subplots(1,2, figsize=(10, 5))
sns.scatterplot(ghana["R1"], ghana["R0"], color="white", ec="black", ax=ax[0])
#ax[0].set_ylim(-0.00000001,0.00000001)
#ax[0].set_xlim(4,7)
sns.scatterplot(ghana["R1"], ghana["KING"], color="white", ec="black", ax=ax[1])
#ax[1].set_ylim(0.42,0.48)
#ax[1].set_xlim(4,7)
plt.title('Pairwise comparisons relatedness between samples from Ghana\n', ha='right')
plt.show()


# In[49]:


ghana_R1KING = sns.scatterplot(ghana["R1"], ghana["KING"], color="white", ec="black")
"""for line in range(0,ghana.shape[0]):
    if ghana["R1"][line]>4:
        ghana_R1R0.text(ghana["R1"][line]+0.01, ghana["R0"][line], 
                     s=f'{ghana["a"][line]},{ghana["b"][line]}', horizontalalignment='left', 
                        size='large', color='red', rotation=45)"""
plt.show()


# In[ ]:





# In[35]:


p1 = sns.scatterplot(data["R1"], data["R0"], size=range(len(data["R0"])), hue=range(len(data["R0"])))
for line in range(0,data.shape[0]):
     p1.text(data.R1[line]+0.01, data.R0[line], 
     line, horizontalalignment='left', 
     size='medium', color='black', weight='semibold')
#plt.savefig('related_comparisons_r1r0.pdf')


# In[34]:


p2 = sns.scatterplot(data["R1"], data["KING"], size=range(len(data["R0"])), color="white", ec="black")
for line in range(0,data.shape[0]):
     p2.text(data.R1[line]+0.01, data.KING[line], 
     line, horizontalalignment='left', 
     size='medium', color='black', weight='semibold')
#plt.savefig('related_comparisons_kingr1.pdf')


# ## Kenya warthogs (including desert)

# In[37]:


kenya = pd.read_csv("Kenya_relate", sep="\t")


# In[38]:


kenya_p2 = sns.scatterplot(kenya["R1"], kenya["KING"], size=range(len(kenya["R0"])), hue=range(len(kenya["R0"])))
for line in range(0, kenya.shape[0]):
     kenya_p2.text(kenya.R1[line]+0.01, kenya.KING[line], 
     line, horizontalalignment='left', 
     size='medium', color='black', weight='semibold')
#plt.savefig('related_comparisons_kingr1.pdf')


# In[39]:


kenya_p1 = sns.scatterplot(kenya["R1"], kenya["R0"], size=range(len(kenya["R0"])), hue=range(len(kenya["R0"])))
for line in range(0,kenya.shape[0]):
     kenya_p1.text(kenya.R1[line]+0.01, kenya.R0[line], 
     line, horizontalalignment='left', 
     size='medium', color='black', weight='semibold')
#plt.savefig('related_comparisons_r1r0.pdf')

