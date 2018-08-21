# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:32:39 2018

@author: marce
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

#%%

from urllib.request import urlopen
from bs4 import BeautifulSoup
#%%
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

#%%
soup = BeautifulSoup(html, 'lxml')
print(type(soup)) #Llegado a este punto deberia dar: bs4.BeautifulSoup

#%%
# Get the title
title = soup.title
print(title)
# Print out the text
text = soup.get_text()
print(soup.text)
# Encuentra todos los hipervínculos
soup.find_all('a')
# use a loop over 'a' tags to find out only href
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
    
# =============================================================================
#     
# =============================================================================
# Print the first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])
# Sacamos cada elemento de cada fila 
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)

#   https://www.datacamp.com/community/tutorials/web-scraping-using-python
#%%
import re
#Regular expresions module
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)

#%%
df = pd.DataFrame(list_rows)
df.head(10)

df1 = df[0].str.split(',', expand=True)
df1.head(10)

col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)
df2 = pd.DataFrame(all_header)
df2.head()
df3 = df2[0].str.split(',', expand=True)
df3.head()
#↨Uniendo los dos dataframes
frames = [df3, df1]

df4 = pd.concat(frames)
df4.head(10)
#Asignar la primera fila como encabezados de la tabla
df5 = df4.rename(columns=df4.iloc[0])
df5.head()
#Ckeck point
df5.info()
df5.shape
#dropping out rows with missing values
df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])
df7.head()
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.head()
df7['Team'] = df7['Team'].str.strip(']')
df7.head()

#%% Data Analysis and Visualization
time_list = df7[' Chip Time'].tolist()

# You can use a for loop to convert 'Chip Time' to minutes

time_mins = []
for i in time_list:
    h, m, s = i.split(':')
    math = (int(h) * 3600 + int(m) * 60 + int(s))/60
    time_mins.append(math)
#print(time_mins)
df7['Runner_mins'] = time_mins
df7.head()    
df7.describe(include=[np.number])

from pylab import rcParams
rcParams['figure.figsize'] = 15, 5

df7.boxplot(column='Runner_mins')
plt.grid(True, axis='y')
plt.ylabel('Chip Time')
plt.xticks([1], ['Runners'])
#Is a normal distribution the Runner_mins??
x = df7['Runner_mins']
ax = sns.distplot(x, hist=True, kde=True, rug=False, color='m', bins=25, hist_kws={'edgecolor':'black'})
plt.show()
#male and female distribution plot
f_fuko = df7.loc[df7[' Gender']==' F']['Runner_mins']
m_fuko = df7.loc[df7[' Gender']==' M']['Runner_mins']
sns.distplot(f_fuko, hist=True, kde=True, rug=False, bins=25, hist_kws={'edgecolor':'black'}, label='Female')
sns.distplot(m_fuko, hist=False, kde=True, rug=False, bins=25, hist_kws={'edgecolor':'black'}, label='Male')
plt.legend()
#Using the groupby method  for describe
g_stats = df7.groupby(" Gender", as_index=True).describe()
print(g_stats)
#boxplot graphic 
df7.boxplot(column='Runner_mins', by='Team')
plt.ylabel('Chip Time')
plt.suptitle("")

    