# -*- coding: utf-8 -*-
"""Source.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p9QuAeN2PHmDE5M1fL9KwuUYBCnj-Vjw

#### In this program, we are going to see how to analyse air quality trends of New York State by looking at two main pollutants: PM2.5 and PM10 affecting the region in two years 2019 and 2020.

####We would alse see the effect of COVID-19 on the air quality levels for 2020.

Importing the packages
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""##### Reading the files"""

PM102019 = pd.read_csv("PM10- 2019.csv")
PM2_52019 = pd.read_csv("PM2.5-2019.csv")
PM102020 = pd.read_csv("PM10- 2020.csv")
PM2_52020 = pd.read_csv("PM2.5-2020.csv")

#PM102020['Date'] = pd.to_datetime(PM102020['Date']).dt.strftime('%m/%d/%Y')

"""##### Changing the datatype to datetime




"""

PM102020['Date'] = pd.to_datetime(PM102020['Date'], format='%m/%d/%Y')

PM102019['Date'] = pd.to_datetime(PM102019['Date'], format='%m/%d/%Y')

PM2_52019['Date'] = pd.to_datetime(PM2_52019['Date'], format='%m/%d/%Y')

PM2_52020['Date'] = pd.to_datetime(PM2_52020['Date'], format='%m/%d/%Y')

"""### Filtering based on months

#### 2020 PM 10
"""

df_2020_mar = PM102020[PM102020['Date'].dt.month == 3]
df_2020_apr = PM102020[PM102020['Date'].dt.month == 4]
df_2020_may = PM102020[PM102020['Date'].dt.month == 5]
df_2020_jun = PM102020[PM102020['Date'].dt.month == 6]
df_2020_jul = PM102020[PM102020['Date'].dt.month == 7]

frames = [df_2020_mar, df_2020_apr, df_2020_may, df_2020_jun,df_2020_jul]
PM102020 = pd.concat(frames)

"""#### 2019 PM 10"""

df_2019_mar = PM102019[PM102019['Date'].dt.month == 3]
df_2019_apr = PM102019[PM102019['Date'].dt.month == 4]
df_2019_may = PM102019[PM102019['Date'].dt.month == 5]
df_2019_jun = PM102019[PM102019['Date'].dt.month == 6]
df_2019_jul = PM102019[PM102019['Date'].dt.month == 7]

frames = [df_2019_mar, df_2019_apr, df_2019_may, df_2019_jun, df_2019_jul]
PM102019 = pd.concat(frames)

"""#### 2019 PM 2.5"""

df_2019_mar_2_5 = PM2_52019[PM2_52019['Date'].dt.month == 3]
df_2019_apr_2_5 = PM2_52019[PM2_52019['Date'].dt.month == 4]
df_2019_may_2_5 = PM2_52019[PM2_52019['Date'].dt.month == 5]
df_2019_jun_2_5 = PM2_52019[PM2_52019['Date'].dt.month == 6]
df_2019_jul_2_5 = PM2_52019[PM2_52019['Date'].dt.month == 7]

frames = [df_2019_mar_2_5, df_2019_apr_2_5, df_2019_may_2_5, df_2019_jun_2_5, df_2019_jul_2_5]
PM2_52019 = pd.concat(frames)

"""#### 2020 PM 2.5"""

df_2020_mar_2_5 = PM2_52020[PM2_52020['Date'].dt.month == 3]
df_2020_apr_2_5 = PM2_52020[PM2_52020['Date'].dt.month == 4]
df_2020_may_2_5 = PM2_52020[PM2_52020['Date'].dt.month == 5]
df_2020_jun_2_5 = PM2_52020[PM2_52020['Date'].dt.month == 6]
df_2020_jul_2_5 = PM2_52020[PM2_52020['Date'].dt.month == 7]

frames = [df_2020_mar_2_5, df_2020_apr_2_5, df_2020_may_2_5, df_2020_jun_2_5, df_2020_jul_2_5]
PM2_52020 = pd.concat(frames)

"""# Average daily max 8-hour CO Concentration

The average daily max 8-hour concentration is defined as highest of the 24 possible 8-hour concentrations computed for the day. 

This is a very valuable parameter to measure how much pollutant exists during the day. So, let's compare the concentration value of PM2.5 and PM10 in the following analyses:

### 2019 Daily max 8-hour concentration for PM10
"""

PM102019_df = PM102019[['Date', 'Daily Mean PM10 Concentration']]

PM102019_df = PM102019_df.groupby(by=['Date']).mean()

PM102019_df = PM102019_df.reset_index()

import plotly.express as px

fig = px.line(PM102019_df, x='Date', y="Daily Mean PM10 Concentration")
fig.show()

PM102019_df['Daily Mean PM10 Concentration'].describe()

PM102019_df['Daily Mean PM10 Concentration'].quantile([.9])

"""### 2020 Daily max 8-hour concentration for PM10"""

PM102020_df = PM102020[['Date', 'Daily Mean PM10 Concentration']]

PM102020_df = PM102020_df.groupby(by=['Date']).mean()

PM102020_df = PM102020_df.reset_index()

import plotly.express as px

fig = px.line(PM102020_df, x='Date', y="Daily Mean PM10 Concentration")
fig.show()

"""## Analysis - 

#### Average Daily max 8-hour concentration

#### I have taken months from “March to July” for both the years 2019 and 2020 to indicate the impact of COVID on air pollution levels in New York. 
"""

## Code to display the image

from IPython.display import Image
Image(filename='fig1.png')

## Code to display the image

from IPython.display import Image
Image(filename='fig2.png')

"""**From the above two time series graphs (Fig 1 (left) and Fig 2(right)), we observe that the average daily CO concentration has  decreased in the year 2020 for both the PM2.5 and PM10 concentration as compared to the year 2019 from March to July.  The main reason for this might be a lockdown due to pandemic as less vehicles on roads. Since most people are forced to stay at homes, lot of actvities which typically emit pollution like vehicle use, industrial production and waste deposition in large quantities are reduced.**"""

PM102020_df['Daily Mean PM10 Concentration'].describe()

PM102020_df['Daily Mean PM10 Concentration'].quantile([.9])

"""### 2019 Daily mean concentration 2.5"""

PM2_52019_df = PM2_52019[['Date', 'Daily Mean PM2.5 Concentration']]

PM2_52019_df = PM2_52019_df.groupby(by=['Date']).mean()

PM2_52019_df = PM2_52019_df.reset_index()

import plotly.express as px

fig = px.line(PM2_52019_df, x='Date', y="Daily Mean PM2.5 Concentration")
fig.show()

PM2_52019_df['Daily Mean PM2.5 Concentration'].describe()

PM2_52019_df['Daily Mean PM2.5 Concentration'].quantile([.9])

"""### 2020 Daily mean concentration 2.5"""

PM2_52020_df = PM2_52020[['Date', 'Daily Mean PM2.5 Concentration']]
PM2_52020_df = PM2_52020_df.groupby(by=['Date']).mean()
#PM2_52019_df = PM102020_df.reset_index()

PM2_52020_df = PM2_52020_df.reset_index()

import plotly.express as px

fig = px.line(PM2_52020_df, x='Date', y="Daily Mean PM2.5 Concentration")
fig.show()

PM2_52020_df['Daily Mean PM2.5 Concentration'].describe()

PM2_52020_df['Daily Mean PM2.5 Concentration'].quantile([.9])



"""### Descriptive Analysis of Concentration"""

## Code to display the image

from IPython.display import Image
Image(filename='fig3.png')

"""**From the above two tables we can conclude that the mean and max PM10 concentration values for the year 2019 were 12.74 and 20.60 respectively which was higher than the PM10 concentration value for the year 2020, once again highlighting the effect of the pandemic in reducing values of key parameters.**"""

## Code to display the image

from IPython.display import Image
Image(filename='fig4.png')

"""**From the above two tables we can conclude that the mean and max PM2.5 concentration values for the year 2019 were 6.04 and 17.52 respectively which was higher than the PM2.5 concentration value for the year 2020 which were 5.02 and 16.40 respectively.**

# Air Quality Index (AQIs)

AQIs are yardsticks to measure the air quality. The higher the AQI value, the greater the public hazard and more dangerous the pollution is.

If any day as an AQI value of less than 50, it is considered a "good day". Similarly, "moderate" days are ones which have AQI values of 50-100 and anything above 100 are considered "bad". Here, we will attempt to analyse classify the datasets we have into good, bad and moderate days.

### Subsetting Date and Daily AQI value column
"""

PM102019_df_AQI = PM102019[['Date', 'DAILY_AQI_VALUE']]

PM102020_df_AQI = PM102020[['Date', 'DAILY_AQI_VALUE']]

PM2_52019_df_AQI = PM2_52019[['Date', 'DAILY_AQI_VALUE']]

PM2_52020_df_AQI = PM2_52020[['Date', 'DAILY_AQI_VALUE']]

PM102019_df_AQI = PM102019_df_AQI.groupby(by=['Date']).mean()

PM102020_df_AQI = PM102020_df_AQI.groupby(by=['Date']).mean()

PM2_52019_df_AQI = PM2_52019_df_AQI.groupby(by=['Date']).mean()

## Convert to csv

PM2_52019_df_AQI.to_csv("PM2_52019_df_AQI.csv")

PM2_52020_df_AQI.to_csv("PM2_52020_df_AQI.csv")

PM2_52020_df_AQI = PM2_52020_df_AQI.groupby(by=['Date']).mean()

df = pd.read_csv("Book.csv")

import plotly.express as px
fig = px.line(df, x="Date", y=df.columns,
              title='Air Quality Index for PM10')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show()

df1 = pd.read_csv("Book3.csv")

import plotly.express as px
fig = px.line(df1, x="Date", y=df1.columns,
              title='Air Quality Index for PM 2.5')
# fig.update_xaxes(
#     dtick="M1",
#     tickformat="%b\n%Y")
fig.show()

## Code to display the image

from IPython.display import Image
Image(filename='fig5.png')

"""**From the above figures of Air Quality Index, we can conclude that the Air Quality index values for the year 2019 
are high for both PM10 and PM2.5 as compared to values for the year 2020.**

(The red line indicates data values for 2019 compared to blue line which is data values for 2020)

# Air Quality index descriptive statistics

### Daily AQI value for PM10

#### 2019
"""

# create a list of our conditions
conditions = [
    (df['DAILY_AQI_VALUE_19'] >= 0) & (df['DAILY_AQI_VALUE_19'] <= 50),
    (df['DAILY_AQI_VALUE_19'] >= 51) & (df['DAILY_AQI_VALUE_19'] <= 100),
    (df['DAILY_AQI_VALUE_19'] > 100)
    ]

# create a list of the values we want to assign for each condition
values = ['Good', 'Moderate', 'Bad']

# create a new column and use np.select to assign values to it using our lists as arguments
df['AQI Level 2019'] = np.select(conditions, values)

# display updated DataFrame
df.head()

"""#### 2020"""

# create a list of our conditions
conditions = [
    (df['DAILY_AQI_VALUE_20'] >= 0) & (df['DAILY_AQI_VALUE_20'] <= 50),
    (df['DAILY_AQI_VALUE_20'] >= 51) & (df['DAILY_AQI_VALUE_20'] <= 100),
    (df['DAILY_AQI_VALUE_20'] > 100)
    ]

# create a list of the values we want to assign for each condition
values = ['Good', 'Moderate', 'Bad']

# create a new column and use np.select to assign values to it using our lists as arguments
df['AQI Level 2020'] = np.select(conditions, values)

# display updated DataFrame
df.head()

df['AQI Level 2019'].value_counts()

df['AQI Level 2020'].value_counts()

"""**This shows the number of "Good" AQI value days i.e. days with an AQI value of less than 50 days was 24 days in both 2019 and 2020. **

#**Urban vs Rural Communities**

**Both the pollutants PM2.5 and PM10 are prevalent in urban and rural areas. But is there a difference in concentration between them? As one would expect, due to higher density of vehicles in urban areas, more pollution is expected in those areas. But is that actually true? (In this analysis, the five boroughs are marked as urban areas while the other counties in New York are marked as rural)**
"""

#### Reading the CSV File

PM102019 = pd.read_csv("PM10- 2019.csv")
PM2_52019 = pd.read_csv("PM2.5-2019.csv")
PM102020 = pd.read_csv("PM10- 2020.csv")
PM2_52020 = pd.read_csv("PM2.5-2020.csv")

PM102019['Date']= pd.to_datetime(PM102019['Date'])

PM2_52019['Date']= pd.to_datetime(PM2_52019['Date'])

PM102020['Date']= pd.to_datetime(PM102020['Date'])

PM2_52020['Date']= pd.to_datetime(PM2_52020['Date'])

PM102019['COUNTY'].unique()

PM102020['COUNTY'].unique()

PM2_52019['COUNTY'].unique()

PM2_52020['COUNTY'].unique()

"""### Subsetting the urban and rural states"""

Urban102019 = PM102019[(PM102019['COUNTY'] == "New York") | (PM102019['COUNTY'] == "Queens") | (PM102019['COUNTY'] == "Bronx")]

rural102019 = PM102019[(PM102019['COUNTY'] == "Erie") | (PM102019['COUNTY'] == "Monroe")]

# Urban102019
# rural102019

Urban102020 = PM102020[(PM102020['COUNTY'] == "New York") | (PM102020['COUNTY'] == "Queens") | (PM102020['COUNTY'] == "Bronx")]

rural102020 = PM102020[(PM102020['COUNTY'] == "Erie") | (PM102020['COUNTY'] == "Monroe")]

# Urban102020
# rural102020

Urban2_52019 = PM2_52019[(PM2_52019['COUNTY'] == "New York") | (PM2_52019['COUNTY'] == "Queens") | (PM2_52019['COUNTY'] == "Bronx") | (PM2_52019['COUNTY'] == "Kings")]

rural2_52019 = PM2_52019[(PM2_52019['COUNTY'] == "Albany") | (PM2_52019['COUNTY'] == "Chautauqua") | (PM2_52019['COUNTY'] == "Essex") | 
                        (PM2_52019['COUNTY'] == "Nassau") | (PM2_52019['COUNTY'] == "Oneida") | (PM2_52019['COUNTY'] == "Onandaga") |
                       (PM2_52019['COUNTY'] == "Orange") | (PM2_52019['COUNTY'] == "Richmond") | (PM2_52019['COUNTY'] == "Rockland") |
                       (PM2_52019['COUNTY'] == "Steuben") | (PM2_52019['COUNTY'] == "Suffolk") | (PM2_52019['COUNTY'] == "Westchester")]

# Urban2_52019
# rural2_52019

Urban2_52020 = PM2_52020[(PM2_52020['COUNTY'] == "New York") | (PM2_52020['COUNTY'] == "Queens") | (PM2_52020['COUNTY'] == "Bronx") | (PM2_52020['COUNTY'] == "Kings")]

rural2_52020 = PM2_52020[(PM2_52020['COUNTY'] == "Albany") | (PM2_52020['COUNTY'] == "Chautauqua") | (PM2_52020['COUNTY'] == "Essex") | 
                        (PM2_52020['COUNTY'] == "Nassau") | (PM2_52020['COUNTY'] == "Oneida") | (PM2_52020['COUNTY'] == "Onandaga") |
                       (PM2_52020['COUNTY'] == "Orange") | (PM2_52020['COUNTY'] == "Richmond") | (PM2_52020['COUNTY'] == "Rockland") |
                       (PM2_52020['COUNTY'] == "Steuben") | (PM2_52020['COUNTY'] == "Suffolk") | (PM2_52020['COUNTY'] == "Westchester")]

# Urban2_52020
# rural2_52020

Urban2_52020

Urban102019.columns

"""#### Comparison of pollution level in urban and rural areas in year 2019 for PM10"""

Urban102019['DAILY_AQI_VALUE'].mean()

rural102019['DAILY_AQI_VALUE'].mean()

"""#### Comparison of pollution level in urban and rural areas in year 2020 for PM10"""

Urban102019['DAILY_AQI_VALUE'].describe()

Urban102020['DAILY_AQI_VALUE'].mean()

rural102020['DAILY_AQI_VALUE'].mean()

"""**From the above analysis, we can say that for both the years 2019 and 2020 the pollution level for PM10 in urban areas are more as compared to that of the rural areas. As we can observe that the mean AQI value for year 2019 for urban and rural areas are 11.94 and 10.27 respectively and for year 2020 are 11.56 and 9.91 respectively.**

#### Comparison of pollution level in urban and rural areas in year 2019 for PM 2.5
"""

Urban2_52019['DAILY_AQI_VALUE'].mean()

rural2_52019['DAILY_AQI_VALUE'].mean()

"""#### Comparison of pollution level in urban and rural areas in year 2020 for PM 2.5"""

Urban2_52020['DAILY_AQI_VALUE'].mean()

rural2_52020['DAILY_AQI_VALUE'].mean()

"""**From above analysis, we can say that for both the years 2019 and 2020 the pollution level for PM 2.5 in urban areas are more as compared to that of the rural areas. As we can observe that the mean AQI value for year 2019 for urban and rural areas are 27.76 and 22.87 respectively and for year 2020 are 25.58 and 22.02 respectively.**

### Stations which is most involved in pollutants
"""

PM102019['Site Name'].unique()

PM102019site = PM102019.groupby(by="Site Name").mean()

PM102019site = PM102019site.reset_index()

ax = PM102019site.plot.barh(x='Site Name', y='DAILY_AQI_VALUE', rot=0)

PM102020['Site Name'].unique()

PM102020site = PM102020.groupby(by="Site Name").mean()

PM102020site = PM102020site.reset_index()

ax = PM102020site.plot.barh(x='Site Name', y='DAILY_AQI_VALUE', rot=0)

"""**Division Street station has most number of pollutant as compared to other stations for PM 10 in both 2019 and 2020.**"""

PM2_52019['Site Name'].unique()

PM2_52019site = PM2_52019.groupby(by="Site Name").mean()

PM2_52019site = PM2_52019site.reset_index()

x = PM2_52019site[PM2_52019site['DAILY_AQI_VALUE']>=25]

ax = x.plot.barh(x='Site Name', y='DAILY_AQI_VALUE', rot=0)

PM2_52020['Site Name'].unique()

PM2_52020site = PM2_52020.groupby(by="Site Name").mean()

PM2_52020site = PM2_52020site.reset_index()

x = PM2_52020site[PM2_52020site['DAILY_AQI_VALUE']>=25]

ax = x.plot.barh(x='Site Name', y='DAILY_AQI_VALUE', rot=0)

"""****For the year 2019, PS19 station is more polluted and for year 2020 Division Street Station is more polluted as compare to other stations**"""