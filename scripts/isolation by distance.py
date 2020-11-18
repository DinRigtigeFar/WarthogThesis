#!/usr/bin/env python
# coding: utf-8

# # Dist fst plots

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import radians, cos, sin, asin, sqrt
from itertools import combinations


# In[2]:


data = pd.read_excel("Matrix.xlsx", index_col=0)
data2 = data.sort_values("Dist")
ticks = [i*1000 for i in range(1,11)]


# ### Dist vs Fst

# In[12]:


fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data2["Dist"], data2["Fst"], hue=list(data2.index))
plt.title("$F_{ST}$ between common warthog populations plotted against \ndistance measured around the equatorial rainforest",
        fontsize=15)
plt.ylabel("$F_{ST}$")
plt.xlabel("Distance in km")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
#plt.xlim(0,10000)
#plt.xticks(ticks)
plt.savefig("ibd_fstfolded_dist.pdf", bbox_inches = 'tight')
# Clear isolation by distance pattern


# ### Great circle distance vs Fst

# In[41]:


ticks2 = [i*1000 for i in range(1,8)]


# In[45]:


fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data2["GrCircDist"], data2["Fst"], hue=list(data2.index))
plt.title("Great circle distance between common warthog populations plotted against $F_{ST}$")
plt.ylabel("$F_{ST}$")
plt.xlabel("Distance in km")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
#plt.xlim(0,8000)
#plt.xticks(ticks2)
plt.savefig("ibd_fstfolded_grCircDist.pdf", bbox_inches = 'tight')
# Clear isolation by distance pattern


# ## Desert Fst and two dists

# In[10]:


data_des = pd.read_excel("Matrix.xlsx", index_col=0, sheet_name = 1)
data_des


# In[39]:


data_des2 = data_des.sort_values("Dist")


# In[47]:


fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data_des2["Dist"], data_des2["Fst"], hue=list(data_des2.index))
plt.title("Distance between common and desert populations plotted against $F_{ST}$")
plt.ylabel("$F_{ST}$")
plt.xlabel("Distance in km")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
plt.xlim(0,8000)
plt.xticks(ticks2)
plt.savefig("ibd_fstfolded_desert_dist.pdf", bbox_inches = 'tight')
# Clear isolation by distance pattern


# In[38]:


data_des3 = data_des.sort_values("CommonHet")
revPal = [i for i in ["#E41A1C", "#377EB8", "#984EA3", "#FF7F00", "#F0C000"][::-1]]
sns.set_palette(revPal)
fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data_des3["CommonHet"], data_des3["Fst"], hue=list(data_des3.index))
plt.title("Heterozygosity of common populations against $F_{ST}$ \nbetween desert and the respective population", fontsize=20)
plt.ylabel("$F_{ST}$")
plt.xlabel("Heterozygosity of the common warthog population in comparison")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
#plt.xlim(0,8000)
#plt.xticks(ticks2)
plt.savefig("desFstHet.pdf", bbox_inches = 'tight')
# Clear isolation by distance pattern


# In[30]:


sns.set_palette(["#E41A1C", "#377EB8", "#984EA3", "#FF7F00", "#F0C000"])
fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data_des["HetDiffs"], data_des["Fst"], hue=list(data_des.index))
plt.title("Differences in heterozygosities between \ncommon and desert populations against $F_{ST}$",fontsize =20)
plt.ylabel("$F_{ST}$")
plt.xlabel("Differences in heterozygosities (desert subtracted from common)")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
#plt.xlim(0,8000)
#plt.xticks(ticks2)
plt.savefig("desFstHetDiffs.pdf", bbox_inches='tight')
# Clear isolation by distance pattern


# ## Using common het and het diff instead of dist

# In[ ]:


fig = plt.figure(figsize=(9, 5))
sns.scatterplot(data_des["GrCircDist"], data_des2["Fst"], hue=list(data_des2.index))
plt.title("Great circle distance between common and desert populations plotted against $F_{ST}$")
plt.ylabel("$F_{ST}$")
plt.xlabel("Distance in km")
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.ylim(0.02, 0.3)
plt.xlim(0,8000)
plt.xticks(ticks2)
plt.savefig("ibd_fstfolded_desert_grCircDist.pdf", bbox_inches = 'tight')
# Clear isolation by distance pattern


# ## Calculating the great circle distance (direct distance)

# In[11]:


def haversine(lon1_lat1, lon2_lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1_lat1[0], lon1_lat1[1], lon2_lat2[0], lon2_lat2[1]])
    # haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


# #### Get distance for all pairs

# In[13]:


Ghana = [9.5, -2.0]
Kenya = [-0.4, 36.1]
Tanzania = [-5.8, 31.1]
Zimbabwe = [-19.8, 29.4]
Namibia = [-21.6, 16.6]
Desert = [1.5, 40.6]
all_pops = [Ghana, Kenya, Tanzania, Zimbabwe, Namibia, Desert]
dists = [haversine(i, k) for i, k in combinations(all_pops, 2)]
dists

