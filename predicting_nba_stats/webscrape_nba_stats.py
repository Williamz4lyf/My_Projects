import requests
from bs4 import BeautifulSoup
import selenium
import pandas as pd
import numpy as np
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#%%
# Download MVP Pages

years = list(range(1991, 2023))

for year in years:
    url = f'https://www.basketball-reference.com/awards/awards_{year}.html'
    page = requests.get(url)

    with open(f'{year}.html', 'w+') as file:
        file.write(page.text)


#%%
# Parse MVP Pages

mvp_dfs = list()

years = list(range(1991, 2023))
for year in years:
    with open(f'mvps/{year}.html') as file:
        page = file.read()
    soup = BeautifulSoup(page, 'html.parser')

    # Remove irrelevant header row
    soup.find('tr', class_='over_header').decompose()
    mvp_table = soup.find('table', id='mvp')

    # Use pandas to read the table
    mvp = pd.read_html(str(mvp_table))[0]

    # Create Year Column for identification
    mvp['Year'] = year

    # append dataframes into list
    mvp_dfs.append(mvp)

# Combine the list of dfs into a single df
mvps = pd.concat(mvp_dfs)
mvps.head()

# Store df
mvps.to_csv('mvps.csv', index=False)

#%%
# Download Player Stats Pages
# Tables here load with javascript and are
# incomplete from requests
# Selenium will automate our Chrome browser
# To parse the tables we need

driver = webdriver.Chrome(executable_path='/Users/nnankewilliams/chromedriver_mac_arm64/chromedriver')

years = list(range(1991, 2023))
for year in years:
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'
    driver.get(url)
    # Javascript command to render the table
    driver.execute_script('window.scrollTo(1,10000)')
    time.sleep(2)

    # Save pages in folder
    with open(f'player_stats/{year}.html', 'w+') as file:
        file.write(driver.page_source)


#%%
# Parse the Pages

years = list(range(1991, 2023))
ps_dfs = list()
for year in years:
    with open(f'player_stats/{year}.html') as file:
        page = file.read()

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find_all(id='per_game_stats')[0]
    player_df = pd.read_html(str(player_table))[0]
    player_df['Year'] = year
    ps_dfs.append(player_df)

player_stats = pd.concat(ps_dfs)
print(player_stats.head())

player_stats.to_csv('player_stats.csv', index=False)


#%%
# Download Team Data

years = list(range(1991, 2023))
for year in years:
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_standings.html'
    page = requests.get(url)

    with open(f'team_data/{year}.html', 'w+') as file:
        file.write(page.text)



#%%
# Parse the Team Data

team_dfs = list()

years = list(range(1991, 2023))
for year in years:
    with open(f"team_data/{year}.html") as file:
        page = file.read()

    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_="thead").decompose()

    # Division Standings - Eastern Conference
    e_table = soup.find_all(id="divs_standings_E")[0]
    e_df = pd.read_html(str(e_table))[0]
    e_df["Year"] = year
    e_df["Team"] = e_df["Eastern Conference"]
    del e_df["Eastern Conference"]
    team_dfs.append(e_df)

    # Division Standings - Western Conference
    w_table = soup.find_all(id="divs_standings_W")[0]
    w_df = pd.read_html(str(w_table))[0]
    w_df["Year"] = year
    w_df["Team"] = w_df["Western Conference"]
    del w_df["Western Conference"]
    team_dfs.append(w_df)

team_data = pd.concat(team_dfs)
print(team_data.head())

team_data.to_csv('team_data.csv', index=False)


#%%
team_data.shape[0]