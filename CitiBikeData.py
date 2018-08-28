
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='Ashwini__', api_key='ipQKFM2zb12IsrIIrveI')
import io
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


#Loading File
CitiDataFile = pd.read_csv("CitiBike Data.csv")
CitiDataFile.head(5)
CitiDataFile.dtypes


# In[45]:


#Summary Statistics
CitiDataFile.describe()
CitiDataFile.describe().transpose()
CitiDataFile.ndim


# In[46]:


#Data Cleaning - Checking for missing data
CitiDataFile.isnull().any().any(), CitiDataFile.shape
CitiDataFile.isnull().sum(axis=0)


# In[47]:


#Summary Statistics for tripduration in minutes

CitiDataFile['tripduration'] = CitiDataFile['tripduration'].apply(lambda x: x/60)
CitiDataFile['tripduration']


# In[48]:


#Correlation between age and tripduration

CitiDataFile['Age'] = 2018 - CitiDataFile['birth year']
CitiDataFile['Age'] = CitiDataFile['Age'].astype(int)
CitiDataFile['Age'].corr(CitiDataFile['tripduration'])
CitiDataFile['Age']


# In[49]:


#subsetting data
femaletrip = CitiDataFile['gender'] == 2
CitiDataFile[femaletrip].head()
FemaleTripData = CitiDataFile[femaletrip]
FemaleTripData.head()


# In[50]:


#anamolies in the data set
sns.boxplot(x="usertype",y="tripduration",data=CitiDataFile, showfliers=False)
Customertype =CitiDataFile['usertype']=="Customer"
CitiDataFile[Customertype].usertype.count()
#just one record with the usertype customer - which is insufficent for any data analysis 


# In[51]:


#Droping the anamolies
d1 = CitiDataFile[CitiDataFile.gender !=0 ]
df = d1[d1.usertype!='customer']


# In[52]:


#Box Plot for tripduration by gender

sns.set(style="darkgrid")
sns.boxplot(y="tripduration",x="gender",data=df,showfliers=False)


# In[53]:


#The total revenue - all users riding bikes from 0 to 45 minutes pay $3 per ride and user exceeding 45 minutes pay an additional $2 per ride.
durationabove45 = df['tripduration'] > 45
durationbelow45 = df['tripduration'] <= 45
revenue= sum(df[durationbelow45].tripduration)*3+ sum(df[durationabove45].tripduration)*2
revenue


# In[54]:


#Looking at tripduration in minutes, what can we say about the variance in the data.
df['tripduration'].std()
df['tripduration'].var()
durationabove45 = df['tripduration'] > 45

print(df[durationabove45].tripduration.count())#216 records above 45 minutes of trip duration.

PercentageOfrecords = (df[durationabove45].tripduration.count()/df['tripduration'].count())*100
PercentageOfrecords #just 1% of Data have tripduration above 45mins 


# In[55]:


#Pricing Strategy - 
#The pricing strategy is targeting the duration of trips above 45mins per ride. With just 1% of data accounting to trips above 45mins, clearly the strategy is less effective.


# In[63]:


#Highly popular trip from the data

PopularTrip = df.groupby(['start station name','end station name']).size().reset_index(name = 'Total Trips')
PopularTrip
PopularTrip['station details'] = PopularTrip['start station name'].map(str) + " to " + df['end station name']
PopularTrip
barp = [go.Bar(x=PopularTrip['Total Trips'], y=PopularTrip['station details'])]
url = py.plot(barp, filename='Popular Trips-chart')


# In[ ]:




