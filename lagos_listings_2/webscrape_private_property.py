from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import re

import warnings

warnings.simplefilter(action='ignore')

titles = list()
locations = list()
pap = list()
dau = list()
bbt = list()

info_1 = list()
info_2 = list()

title_text = list()
location_text = list()
pap_text = list()
dau_text = list()
bbt_text = list()

# Final Page num = 1637
for i in range(201, 400):
    url = f'https://www.privateproperty.com.ng/property-for-rent/lagos?page={i}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    list_1 = soup.find_all('div', class_='similar-listings-info')
    list_2 = soup.find_all('div', class_='similar-listings-price')

    for item in list_1:
        title = item.find('h3', class_='')
        location = item.find('p', class_='listings-location')
        date_added_updated = item.find('h5', class_='mt-0')
        info_1.append([title, location, date_added_updated])

    for item in list_2:
        price_and_period = item.find('h4', class_='')
        bed_bath_toilet = item.find('ul', class_='property-benefit')
        info_2.append([price_and_period, bed_bath_toilet])

    for item in info_1:
        titles.append(item[0])
        locations.append(item[1])
        dau.append(item[2])

    for item in info_2:
        pap.append(item[0])
        bbt.append(item[1])

    for title in titles:
        if title is not None:
            title_text.append(title.text)

    for location in locations:
        if location is not None:
            location_text.append(location.text.replace('\\n',''))

    for i in pap:
        if i is not None:
            pap_text.append(i.text.replace('₦', ''))

    for i in dau:
        if i is not None:
            dau_text.append(i.text)

    for i in bbt:
        if i is not None:
            bbt_str = i.text.strip().replace('\n','').split()
            bbt_text.append(''.join(map(str, bbt_str)))

lag_priv_property = pd.DataFrame(
    {'Title': title_text,
     'Location': location_text,
     'Price_Period': pap_text,
     'Date_Added_Updated': dau_text,
     'Bed_Bath_Toilet': bbt_text})

lag_priv_property.drop_duplicates(keep='last', inplace=True)
lag_priv_property.to_csv('lag_priv_property_2.csv', index=False)

#%%
df = pd.read_csv('lag_priv_property_2.csv')
df.info()
#%%
