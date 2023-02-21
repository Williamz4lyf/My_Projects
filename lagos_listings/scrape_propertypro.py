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
serv = list()
desc = list()
bbt = list()

info = list()
title_text = list()
location_text = list()
pap_text = list()
dau_text = list()
desc_text = list()
serv_text = list()
bbt_text = list()

for i in range(801, 896):
    url = f'https://www.propertypro.ng/property-for-rent/in/lagos?page={i}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lists = soup.find_all('div', class_='single-room-text')

    for item in lists:
        title = item.find('h4', class_='listings-property-title')
        location = item.findNext('h4', class_='')
        price_and_period = item.find('div', class_='n50')
        date_added_updated = item.find('h5', class_='')
        serviced = item.find('div', class_='furnished-btn')
        description = item.find('p', class_='d-none d-sm-block')
        bed_bath_toilet = item.find('div', class_='fur-areea')
        info.append([title, location, price_and_period, date_added_updated,
                     serviced, description, bed_bath_toilet])

    for item in info:
        titles.append(item[0])
        locations.append(item[1])
        pap.append(item[2])
        dau.append(item[3])
        serv.append(item[4])
        desc.append(item[5])
        bbt.append(item[6])

    for title in titles:
        if title is not None:
            title_text.append(title.text)

    for location in locations:
        if location is not None:
            location_text.append(location.text)

    for i in pap:
        if i is not None:
            pap_t = i.text.replace('\n₦', '').split(' ')[2]
            pap_text.append(pap_t)

    for i in dau:
        if i is None:
            pass
        else:
            dau_text.append(i.text)

    for i in serv:
        if i is None:
            pass
        else:
            serv_text.append(i.text.replace('\n', ''))

    for i in desc:
        if i is None:
            pass
        else:
            desc_text.append(i.text)

    for i in bbt:
        if i is None:
            pass
        else:
            bbt_text.append(i.text.replace('\n', ''))

lag_rents_pp = pd.DataFrame(
    {'Location': location_text,
     'Price_Period': pap_text,
     'Date_Added_Updated': dau_text,
     'Description': desc_text,
     'Serviced': serv_text,
     'Bed_Bath_Toilet': bbt_text})


lag_rents_pp.drop_duplicates(keep='last', inplace=True)
lag_rents_pp.to_csv('lag_rents_pp_8.csv', index=False)

# %%
df = pd.read_csv('lag_rents_pp_8.csv')
df.info()
