#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as geo
df=pd.read_excel("downloads/corona.xlsx")
df[['Country_Region','Deaths']].head()


# In[19]:


df.groupby(['Country_Region']).sum()


# In[12]:


import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
plt.style.use('seaborn')

data = pd.read_excel('downloads/timeseries.xlsx')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
corona_date = data['Date']
corona_cases = data['Cases']
plt.plot_date(corona_date, corona_cases, linestyle='solid')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.title('Corona Virus in the World')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()


# In[ ]:




