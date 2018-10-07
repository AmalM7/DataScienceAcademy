
# coding: utf-8

# In[1]:


url = 'https://fr.wikipedia.org/wiki/Discographie_de_Charles_Aznavour'


# In[21]:


import requests
from bs4 import BeautifulSoup
from matplotlib.pyplot import plot
from collections import Counter


# In[8]:


soup = BeautifulSoup(requests.get(url).content,"html.parser")


# In[10]:


table = soup.find(class_="wikitable")


# In[16]:


years = []
for tr in table.findAll('tr')[1:]:
    years.append(int(tr.find('td').getText()))


# In[22]:


Counter(years)


# In[19]:


ryears = range(min(years),max(years)+1)


# In[23]:


production_charles_aznavour = {}
for year in ryears:
    if year in years:
        production_charles_aznavour[year] = Counter(years)[year]
    else:
        production_charles_aznavour[year] = 0


# In[28]:


get_ipython().magic(u'matplotlib inline')
plot(ryears,[production_charles_aznavour[year] for year in ryears],'b')

