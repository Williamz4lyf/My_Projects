from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import re

import warnings
warnings.simplefilter(action='ignore')

#%%
reg_season = list()
season = list()
rank = list()
year_list = list(range(2013, 2024))

for year in year_list:
    url = f'https://fbref.com/en/comps/9/{year - 1}-{year}/{year - 1}-{year}-Premier-League-Stats'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Collect Table
    stats_table = soup.find('table', id=f'results{year - 1}-{year}91_overall')

    # Get table headers
    columns = list()
    header = stats_table.find('thead')
    for i in header.find_all('th'):
        title = i.text
        columns.append(title)

    # Create a Lists for Table Values
    row_data = list()

    # Create a for loop to Collect Table Values
    body = stats_table.find('tbody')
    for i in body.find_all('tr'):
        rank.append(i.find('th').text)
        row_data.append(i.find_all('td'))
    for row in row_data:
        reg_season.append([record.text for record in row])
        season.append(f'{year-1}-{year}')

#%%

teams = pd.DataFrame(reg_season, columns=columns[1:])
teams.insert(loc=0, column='Rk', value=rank)
teams.insert(loc=0, column='Season', value=season)


#%%
teams

#%%
# Clean Team Names
squad = pd.DataFrame(teams['Squad'].unique())
squad.rename(columns={0:'team'}, inplace=True)

squad['team'] = squad['team'].apply(lambda x: x.strip())
squad['team'] = squad['team'].apply(lambda x: x.replace('Utd', 'United'))
squad['team'] = squad['team'].apply(lambda x: x.replace('West Ham', 'West Ham United'))
squad['team'] = squad['team'].apply(lambda x: x.replace('West Brom', 'West Bromwich Albion'))
squad['team'] = squad['team'].apply(lambda x: x.replace('Nott\'ham Forest', 'Nottingham Forest'))

squad['scores_link'] = 'link'
squad['shooting_link'] = 'link'

squad

#%%
# Base Links for all teams
squad.loc[squad['team'] == 'Arsenal', 'scores_link'] = 'https://fbref.com/en/squads/18bb7c10/{}-{}/matchlogs/all_comps/schedule/Arsenal-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Arsenal', 'shooting_link'] = 'https://fbref.com/en/squads/18bb7c10/{}-{}/matchlogs/all_comps/shooting/Arsenal-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Manchester City', 'scores_link'] = 'https://fbref.com/en/squads/b8fd03ef/{}-{}/matchlogs/all_comps/schedule/Manchester-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Manchester City', 'shooting_link'] = 'https://fbref.com/en/squads/b8fd03ef/{}-{}/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Tottenham', 'scores_link'] = 'https://fbref.com/en/squads/361ca564/{}-{}/matchlogs/all_comps/schedule/Tottenham-Hotspur-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Tottenham', 'shooting_link'] = 'https://fbref.com/en/squads/361ca564/{}-{}/matchlogs/all_comps/shooting/Tottenham-Hotspur-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Tottenham', 'scores_link'] = 'https://fbref.com/en/squads/19538871/{}-{}/matchlogs/all_comps/schedule/Manchester-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Tottenham', 'shooting_link'] = 'https://fbref.com/en/squads/19538871/{}-{}/matchlogs/all_comps/shooting/Manchester-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Chelsea', 'scores_link'] = 'https://fbref.com/en/squads/cff3d9bb/{}-{}/matchlogs/all_comps/schedule/Chelsea-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Chelsea', 'shooting_link'] = 'https://fbref.com/en/squads/cff3d9bb/{}-{}/matchlogs/all_comps/shooting/Chelsea-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Manchester United', 'scores_link'] = 'https://fbref.com/en/squads/19538871/{}-{}/matchlogs/all_comps/schedule/Manchester-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Manchester United', 'shooting_link'] = 'https://fbref.com/en/squads/19538871/{}-{}/matchlogs/all_comps/shooting/Manchester-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Liverpool', 'scores_link'] = 'https://fbref.com/en/squads/822bd0ba/{}-{}/matchlogs/all_comps/schedule/Liverpool-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Liverpool', 'shooting_link'] = 'https://fbref.com/en/squads/822bd0ba/{}-{}/matchlogs/all_comps/shooting/Liverpool-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Brentford', 'scores_link'] = 'https://fbref.com/en/squads/cd051869/{}-{}/matchlogs/all_comps/schedule/Brentford-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Brentford', 'shooting_link'] = 'https://fbref.com/en/squads/cd051869/{}-{}/matchlogs/all_comps/shooting/Brentford-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Brighton', 'scores_link'] = 'https://fbref.com/en/squads/d07537b9/{}-{}/matchlogs/all_comps/schedule/Brighton-and-Hove-Albion-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Brighton', 'shooting_link'] = 'https://fbref.com/en/squads/d07537b9/{}-{}/matchlogs/all_comps/shooting/Brighton-and-Hove-Albion-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Newcastle United', 'scores_link'] = 'https://fbref.com/en/squads/b2b47a98/{}-{}/matchlogs/all_comps/schedule/Newcastle-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Newcastle United', 'shooting_link'] = 'https://fbref.com/en/squads/b2b47a98/{}-{}/matchlogs/all_comps/shooting/Newcastle-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Aston Villa', 'scores_link'] = 'https://fbref.com/en/squads/8602292d/{}-{}/matchlogs/all_comps/schedule/Aston-Villa-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Aston Villa', 'shooting_link'] = 'https://fbref.com/en/squads/8602292d/{}-{}/matchlogs/all_comps/shooting/Aston-Villa-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Fulham', 'scores_link'] = 'https://fbref.com/en/squads/fd962109/{}-{}/matchlogs/all_comps/schedule/Fulham-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Fulham', 'shooting_link'] = 'https://fbref.com/en/squads/fd962109/{}-{}/matchlogs/all_comps/shooting/Fulham-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Crystal Palace', 'scores_link'] = 'https://fbref.com/en/squads/47c64c55/{}-{}/matchlogs/all_comps/schedule/Crystal-Palace-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Crystal Palace', 'shooting_link'] = 'https://fbref.com/en/squads/47c64c55/{}-{}/matchlogs/all_comps/shooting/Crystal-Palace-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Wolves', 'scores_link'] = 'https://fbref.com/en/squads/8cec06e1/{}-{}/matchlogs/all_comps/schedule/Wolverhampton-Wanderers-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Wolves', 'shooting_link'] = 'https://fbref.com/en/squads/8cec06e1/{}-{}/matchlogs/all_comps/shooting/Wolverhampton-Wanderers-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'West Ham United', 'scores_link'] = 'https://fbref.com/en/squads/7c21e445/{}-{}/matchlogs/all_comps/schedule/West-Ham-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'West Ham United', 'shooting_link'] = 'https://fbref.com/en/squads/7c21e445/{}-{}/matchlogs/all_comps/shooting/West-Ham-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Nottingham Forest', 'scores_link'] = 'https://fbref.com/en/squads/e4a775cb/{}-{}/matchlogs/all_comps/schedule/Nottingham-Forest-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Nottingham Forest', 'shooting_link'] = 'https://fbref.com/en/squads/e4a775cb/{}-{}/matchlogs/all_comps/shooting/Nottingham-Forest-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Bournemouth', 'scores_link'] = 'https://fbref.com/en/squads/4ba7cbea/{}-{}/matchlogs/all_comps/schedule/Bournemouth-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Bournemouth', 'shooting_link'] = 'https://fbref.com/en/squads/4ba7cbea/{}-{}/matchlogs/all_comps/shooting/Bournemouth-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Leeds United', 'scores_link'] = 'https://fbref.com/en/squads/5bfb9659/{}-{}/matchlogs/all_comps/schedule/Leeds-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Leeds United', 'shooting_link'] = 'https://fbref.com/en/squads/5bfb9659/{}-{}/matchlogs/all_comps/shooting/Leeds-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Everton', 'scores_link'] = 'https://fbref.com/en/squads/d3fd31cc/{}-{}/matchlogs/all_comps/schedule/Everton-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Everton', 'shooting_link'] = 'https://fbref.com/en/squads/d3fd31cc/{}-{}/matchlogs/all_comps/shooting/Everton-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Leicester City', 'scores_link'] = 'https://fbref.com/en/squads/a2d435b3/{}-{}/matchlogs/all_comps/schedule/Leicester-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Leicester City', 'shooting_link'] = 'https://fbref.com/en/squads/a2d435b3/{}-{}/matchlogs/all_comps/shooting/Leicester-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Southampton', 'scores_link'] = 'https://fbref.com/en/squads/33c895d4/{}-{}/matchlogs/all_comps/schedule/Southampton-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Southampton', 'shooting_link'] = 'https://fbref.com/en/squads/33c895d4/{}-{}/matchlogs/all_comps/shooting/Southampton-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Burnley', 'scores_link'] = 'https://fbref.com/en/squads/943e8050/{}-{}/matchlogs/all_comps/schedule/Burnley-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Burnley', 'shooting_link'] = 'https://fbref.com/en/squads/943e8050/{}-{}/matchlogs/all_comps/shooting/Burnley-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Watford', 'scores_link'] = 'https://fbref.com/en/squads/2abfe087/{}-{}/matchlogs/all_comps/schedule/Watford-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Watford', 'shooting_link'] = 'https://fbref.com/en/squads/2abfe087/{}-{}/matchlogs/all_comps/shooting/Watford-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Norwich City', 'scores_link'] = 'https://fbref.com/en/squads/1c781004/{}-{}/matchlogs/all_comps/schedule/Norwich-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Norwich City', 'shooting_link'] = 'https://fbref.com/en/squads/1c781004/{}-{}/matchlogs/all_comps/shooting/Norwich-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Fulham', 'scores_link'] = 'https://fbref.com/en/squads/fd962109/{}-{}/matchlogs/all_comps/schedule/Fulham-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Fulham', 'shooting_link'] = 'https://fbref.com/en/squads/fd962109/{}-{}/matchlogs/all_comps/shooting/Fulham-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Sheffield United', 'scores_link'] = 'https://fbref.com/en/squads/1df6b87e/{}-{}/matchlogs/all_comps/schedule/Sheffield-United-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Sheffield United', 'shooting_link'] = 'https://fbref.com/en/squads/1df6b87e/{}-{}/matchlogs/all_comps/shooting/Sheffield-United-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Reading', 'scores_link'] = 'https://fbref.com/en/squads/b0ac61ff/{}-{}/matchlogs/all_comps/schedule/Reading-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Reading', 'shooting_link'] = 'https://fbref.com/en/squads/b0ac61ff/{}-{}/matchlogs/all_comps/shooting/Reading-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'QPR', 'scores_link'] = 'https://fbref.com/en/squads/a757999c/{}-{}/matchlogs/all_comps/schedule/Queens-Park-Rangers-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'QPR', 'shooting_link'] = 'https://fbref.com/en/squads/a757999c/{}-{}/matchlogs/all_comps/shooting/Queens-Park-Rangers-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Sunderland', 'scores_link'] = 'https://fbref.com/en/squads/8ef52968/{}-{}/matchlogs/all_comps/schedule/Sunderland-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Sunderland', 'shooting_link'] = 'https://fbref.com/en/squads/8ef52968/{}-{}/matchlogs/all_comps/shooting/Sunderland-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Wigan Athletic', 'scores_link'] = 'https://fbref.com/en/squads/e59ddc76/{}-{}/matchlogs/all_comps/schedule/Wigan-Athletic-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Wigan Athletic', 'shooting_link'] = 'https://fbref.com/en/squads/e59ddc76/{}-{}/matchlogs/all_comps/shooting/Wigan-Athletic-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Stoke City', 'scores_link'] = 'https://fbref.com/en/squads/17892952/{}-{}/matchlogs/all_comps/schedule/Stoke-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Stoke City', 'shooting_link'] = 'https://fbref.com/en/squads/17892952/{}-{}/matchlogs/all_comps/shooting/Stoke-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Cardiff City', 'scores_link'] = 'https://fbref.com/en/squads/75fae011/{}-{}/matchlogs/all_comps/schedule/Cardiff-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Cardiff City', 'shooting_link'] = 'https://fbref.com/en/squads/75fae011/{}-{}/matchlogs/all_comps/shooting/Cardiff-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Hull City', 'scores_link'] = 'https://fbref.com/en/squads/bd8769d1/{}-{}/matchlogs/all_comps/schedule/Hull-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Hull City', 'shooting_link'] = 'https://fbref.com/en/squads/bd8769d1/{}-{}/matchlogs/all_comps/shooting/Hull-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Swansea City', 'scores_link'] = 'https://fbref.com/en/squads/fb10988f/{}-{}/matchlogs/all_comps/schedule/Swansea-City-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Swansea City', 'shooting_link'] = 'https://fbref.com/en/squads/fb10988f/{}-{}/matchlogs/all_comps/shooting/Swansea-City-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'West Bromwich Albion', 'scores_link'] = 'https://fbref.com/en/squads/60c6b05f/{}-{}/matchlogs/all_comps/schedule/West-Bromwich-Albion-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'West Bromwich Albion', 'shooting_link'] = 'https://fbref.com/en/squads/60c6b05f/{}-{}/matchlogs/all_comps/shooting/West-Bromwich-Albion-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Middlesbrough', 'scores_link'] = 'https://fbref.com/en/squads/7f59c601/{}-{}/matchlogs/all_comps/schedule/Middlesbrough-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Middlesbrough', 'shooting_link'] = 'https://fbref.com/en/squads/7f59c601/{}-{}/matchlogs/all_comps/shooting/Middlesbrough-Match-Logs-All-Competitions'

squad.loc[squad['team'] == 'Huddersfield', 'scores_link'] = 'https://fbref.com/en/squads/f5922ca5/{}-{}/matchlogs/all_comps/schedule/Huddersfield-Town-Scores-and-Fixtures-All-Competitions'
squad.loc[squad['team'] == 'Huddersfield', 'shooting_link'] = 'https://fbref.com/en/squads/f5922ca5/{}-{}/matchlogs/all_comps/shooting/Huddersfield-Town-Match-Logs-All-Competitions'

squad

#%%

link = squad.loc[squad['team'] == 'Huddersfield', 'scores_link'].apply(lambda x: x.format(2016, 2017)).values[0]
link


#%%
scores_columns = list()
shoot_columns = list()

#%%
scores_date = list()
shoot_date = list()
scores = list()
shooting = list()
scores_team_name = list()
shooting_team_name = list()
scores_epl_season = list()
shoot_epl_season = list()


#%%
# Table Headers
scores_url = squad.loc[squad['team'] == 'Reading', 'scores_link'].apply(lambda x: x.format(2022, 2023)).values[0]
shoot_url = squad.loc[squad['team'] == 'Reading', 'shooting_link'].apply(lambda x: x.format(2022, 2023)).values[0]
scores_page = requests.get(scores_url)
shoot_page = requests.get(shoot_url)
scores_soup = BeautifulSoup(scores_page.content, 'html.parser')
shoot_soup = BeautifulSoup(shoot_page.content, 'html.parser')

scores_table = scores_soup.find('table', id='matchlogs_for')
shoot_table = shoot_soup.find('table', id='matchlogs_for')

# Get table headers

scores_header = scores_table.find('thead')
for i in scores_header.find_all('th'):
    title = i.text
    scores_columns.append(title)


shoot_header = shoot_table.find('thead')
for i in shoot_header.find_all('th'):
    title = i.text
    shoot_columns.append(title)

#%%
# Table Values
year_list = list(range(2015, 2024))
for i in range(18, 35):
    # Fill in the values loc
    # Skipped 18 - 24
    team = squad['team'].values[i]
    # for year in year_list:
    for year in year_list:
        scores_url = squad.loc[squad['team'] == team, 'scores_link'].apply(lambda x: x.format(year-1, year)).values[0]
        shoot_url = squad.loc[squad['team'] == team, 'shooting_link'].apply(lambda x: x.format(year-1, year)).values[0]
        scores_page = requests.get(scores_url)
        shoot_page = requests.get(shoot_url)
        scores_soup = BeautifulSoup(scores_page.content, 'html.parser')
        shoot_soup = BeautifulSoup(shoot_page.content, 'html.parser')

        # Collect Tables
        scores_table = scores_soup.find('table', id='matchlogs_for')
        shoot_table = shoot_soup.find('table', id='matchlogs_for')

        # Create a Lists for Table Values
        scores_row_data = list()
        shoot_row_data = list()

        # Create a for loop to Collect Table Values
        scores_body = scores_table.find('tbody')
        for i in scores_body.find_all('tr'):
            scores_date.append(i.find('th').text)
            scores_row_data.append(i.find_all('td'))
        for row in scores_row_data:
            scores.append([record.text for record in row])
            scores_team_name.append(team)
            scores_epl_season.append(f'{year-1}-{year}')

        shoot_body = shoot_table.find('tbody')
        for i in shoot_body.find_all('tr'):
            shoot_date.append(i.find('th').text)
            shoot_row_data.append(i.find_all('td'))
        for row in shoot_row_data:
            shooting.append([record.text for record in row])
            shooting_team_name.append(team)
            shoot_epl_season.append(f'{year-1}-{year}')


#%%
scores_df = pd.DataFrame(scores, columns=scores_columns[-18:])
scores_df.insert(loc=0, column='Date', value=scores_date)
scores_df.insert(loc=0, column='Team', value=scores_team_name)
scores_df.insert(loc=0, column='Season', value=scores_epl_season)
# scores_df.drop(scores_df.loc[scores_df['Comp'] != 'Premier League'].index, axis=0, inplace=True)


shoot_df = pd.DataFrame(shooting, columns=shoot_columns[-25:])
shoot_df.insert(loc=0, column='Date', value=shoot_date)
shoot_df.insert(loc=0, column='Team', value=shooting_team_name)
shoot_df.insert(loc=0, column='Season', value=shoot_epl_season)
# shoot_df.drop(shoot_df.loc[shoot_df['Comp'] != 'Premier League'].index, axis=0, inplace=True)


#%%

scores_df.to_csv('scores_reading_nfo.csv', index=False)
shoot_df.to_csv('shooting_reading_nfo.csv', index=False)


#%%

len(scores_columns)


#%%
scores_df.head()