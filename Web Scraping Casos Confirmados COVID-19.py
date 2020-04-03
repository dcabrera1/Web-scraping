#!/usr/bin/env python
# coding: utf-8

# In[128]:


import urllib.request 


datos = urllib.request.urlopen('https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6').read().decode()


# datos = urllib.request.urlopen('https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6').read().decode()

# In[129]:


import sys
sys.path.append(r"WhereverYourPackagesAre/site-packages/beautifulsoup4")


# In[130]:


from bs4 import BeautifulSoup
soup =  BeautifulSoup(datos)
tags = soup('a')
for tag in tags: 
    print(tag.get('href'))


# In[131]:


get_ipython().system('pip install selenium')


# In[132]:


#Importing packages
from selenium import webdriver
import pandas as pd


# In[133]:


driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')


# In[134]:


confirmados=[] #Lista casos confirmados
driver.get('https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')


# In[139]:


import csv
import pandas as pd
confirmados_element = driver.find_elements_by_xpath ('//*[@id="ember34"]/div[2]')  [0]
confirmados.append(confirmados_element.text)
print(confirmados_element.text)
 


# In[141]:


df = pd.DataFrame({'Casos confirmados':confirmados}) 
df.to_csv('casos_paises_covid-19.csv', index=False, encoding='utf-8')







