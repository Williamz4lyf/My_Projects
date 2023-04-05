# Date Created: 22 February 2023
# Author : @Nanke

import pandas as pd
import numpy as np
import matplotlib as plt
import re
import datetime as dt

import warnings
warnings.simplefilter(action='ignore')

#%%

# Read and Combine datasets
df_1 = pd.read_csv('datasets/lag_priv_property_1.csv')
df_2 = pd.read_csv('datasets/lag_priv_property_2.csv')
df_3 = pd.read_csv('datasets/lag_priv_property_3.csv')
df_4 = pd.read_csv('datasets/lag_priv_property_4.csv')
df_5 = pd.read_csv('datasets/lag_priv_property_5.csv')
df_6 = pd.read_csv('datasets/lag_priv_property_6.csv')
df_7 = pd.read_csv('datasets/lag_priv_property_7.csv')
df_8 = pd.read_csv('datasets/lag_priv_property_8.csv')
df_9 = pd.read_csv('datasets/lag_priv_property_9.csv')

df = pd.concat([df_1, df_2, df_3, df_4, df_5,
                df_6, df_7, df_8, df_9], ignore_index=True)

#%%
# Review dataset
df.info()
#%%
df.head()
#%%
df.tail()

#%%
# Parse title column to segment listing types
def listing_type(row):
    if 'for rent' in row.lower():
        return 'Rent'
    elif 'for sale' in row.lower():
        return 'Sale'
    else:
        return 'Unknown'

df['Listing_Type'] = df['Title'].apply(listing_type)
df['Listing_Type'].value_counts()

#%%
# Clean Location Column
df['Location'] = df['Location'].str.replace('\\n', '')
df['Location'].head()

# Parse City from Location
df['City'] = df['Location'].str.split().str[-2]
df['City'].value_counts()

# There's a few odd entries: [Island, Road, Express, Metta, 1,
# Phase, Expressway]
odd_cities = ['Island', 'Road', 'Express', 'Metta',
              '1', 'Phase', 'Expressway']

# Let's analyze the items in each city to determine the right names
df.loc[df['City'] == odd_cities[2]].sample(17)

# Update the City variable with the proper city names
df['City'] = df['City'].apply(lambda x: 'Victoria Island' if x == 'Island' else x)
df['City'] = df['City'].apply(lambda x: 'Ikorodu Road' if x == 'Road' else x)
df['City'] = df['City'].apply(lambda x: 'Ebute Metta' if x == 'Metta' else x)
df['City'] = df['City'].apply(lambda x: 'Lekki' if x == '1' else x)
df['City'] = df['City'].apply(lambda x: 'Lekki' if x == 'Expressway' else x)

for index, row in df.loc[df['City'] == 'Express'].iterrows():
    if 'Alimosho' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Iju' in row['Location']:
        df.at[index, 'City'] = 'Iju'
    elif 'Sango' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Idimu' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Badagry' in row['Location']:
        df.at[index, 'City'] = 'Badagry'
    elif 'Igando' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Isheri' in row['Location']:
        df.at[index, 'City'] = 'Isheri'
    elif 'Alagbado' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Lasu Road' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Okokomaiko' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    elif 'Idimu' in row['Location']:
        df.at[index, 'City'] = 'Alimosho'
    else:
        pass

# Drop the records with City == 'Phase' since these are not Lagos listings
# Drop the remainder City == 'Express' records.
df.drop(index=list(df.loc[df['City'] == 'Phase'].index), inplace=True)
df.drop(index=list(df.loc[df['City'] == 'Express'].index), inplace=True)

# Segment City Data into Island and Mainland
island_list = ['Lekki', 'Ajah', 'Ikoyi', 'Victoria Island']
df['Location_Area'] = df['City'].apply(lambda x:'Island' if x in island_list else 'Mainland')
df[['City', 'Location_Area']].head()

df['City'].value_counts()
df['Location_Area'].value_counts()

#%%
# Clean the Price Column
# Parse the Price_period column to remove $ listings
usd_listings = df.loc[df['Price_Period'].str.contains('$', regex=False)]
df.drop(index=usd_listings.index, inplace=True)
print(df.loc[df['Price_Period'].str.contains('$', regex=False)].head())

# Convert Price_Period to Float
df['Price'] = df['Price_Period'].str.split('/').str[0]
df['Price'] = df['Price'].apply(lambda x: ''.join(map(str, x.strip().split(','))))
df['Price'] = df['Price'].astype(float)

# Parse Period to highlight different size values
size = df['Price_Period'].str.split('/').str[-1]
sqm = size.loc[lambda x: x.str.strip() == 'sqm']
month = size.loc[lambda x: x.str.strip() == 'month']
day = size.loc[lambda x: x.str.strip() == 'day']

# Update the Price figures for month and day sizes
for i in month.index:
    df.at[i, 'Price'] = df.at[i, 'Price'] * 12

for i in day.index:
    df.at[i, 'Price'] = df.at[i, 'Price'] * 365

# Drop records with sqm Size since we don't have the total sqm value
df.drop(index=list(sqm.index), inplace=True)

# Drop all records with Price below 100,000 to avoid skewing errors
df.drop(index=df.loc[df['Price'] < 100000].index, inplace=True)

# Drop Price_Period column
df.drop(columns=['Price_Period'], inplace=True)

df['Price'].sample(30)

#%%
# Clean the Date_Added_Updated Column
# Separate date added and date updated
df['Date_Added_Updated'] = df['Date_Added_Updated'].str.strip()
df['Date_Added'] = df['Date_Added_Updated'].str.split(',').str[-1]
df['Date_Added'] = df['Date_Added'].str.strip().str[6:]

df['Date_Updated'] = df['Date_Added_Updated'].str.split(',').str[0]
# Done using reverse indexing to avoid losses for records without update dates
df['Date_Updated'] = df['Date_Updated'].str.strip().str[-11:]

# Convert Today in Date_Added into datetime format
today = df['Date_Added'].loc[df['Date_Added'] == 'Today']
for i in today.index:
    df.at[i, 'Date_Added'] = dt.date.today()

# Updated Today string in Date Added & Date Updated to date
today = df['Date_Added'].loc[df['Date_Added'] == 'Today']
for i in today.index:
    df.at[i, 'Date_Added'] = dt.date.today()

today_1 = df['Date_Updated'].loc[df['Date_Updated'] == 'Added Today']
for i in today_1.index:
    df.at[i, 'Date_Updated'] = dt.date.today()

# Convert to datetime format
df['Date_Added'] = pd.to_datetime(df['Date_Added'])
df['Date_Updated'] = pd.to_datetime(df['Date_Updated'])

df[['Date_Added', 'Date_Updated']].head()

#%%
# Parse the bed bath toilet column
for index, value in df['Bed_Bath_Toilet'].items():
    try:
        df.at[index, 'bbt_i'] = str(int(value))
    except ValueError:
        df.at[index, 'bbt_i'] = '000'

for index, value in df['bbt_i'].items():
    if len(value) == 3:
        df.at[index, 'Beds'] = value[0]
        df.at[index, 'Baths'] = value[1]
        df.at[index, 'Toilets'] = value[2]
    elif len(value) == 2:
        df.at[index, 'Beds'] = value[0]
        df.at[index, 'Baths'] = value[1]
        df.at[index, 'Toilets'] = '0'
    elif len(value) == 1:
        df.at[index, 'Beds'] = value[0]
        df.at[index, 'Baths'] = '0'
        df.at[index, 'Toilets'] = '0'

df[['Bed_Bath_Toilet', 'Beds', 'Baths', 'Toilets']].head(30)

#%%
# Drop Columns Not in Use
df.drop(columns=['Date_Added_Updated', 'Bed_Bath_Toilet', 'bbt_i'], inplace=True)

#%%
df.sample(5)

#%%
# Save to local device
df.to_csv('private_property_listing.csv', index=False)


