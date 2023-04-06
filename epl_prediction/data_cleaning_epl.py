import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore')

#%%

man_u_wigan_scores = pd.read_csv('scores_man_u_wigan.csv')
man_u_wigan_shoots = pd.read_csv('shooting_man_u_wigan.csv')
reading_nfo_scores = pd.read_csv('scores_reading_nfo.csv')
reading_nfo_shoots = pd.read_csv('shooting_reading_nfo.csv')

#%%
# reading_nfo_scores.head()
# reading_nfo_shoots.head()
# man_u_wigan_scores.head()
# man_u_wigan_shoots.head()
#
# #%%
# # Rearrange columns in Man U - Wigan
# man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2017-2018'].head()
# man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2017-2018'].head()

#%%
# Create copies of the right values across all relevant seasons
poss_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'xG'].copy()
attendance_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'xGA'].copy()
captain_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Poss'].copy()
formation_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Attendance'].copy()
referee_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Captain'].copy()
match_report_1213 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Formation'].copy()

poss_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'xG'].copy()
attendance_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'xGA'].copy()
captain_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Poss'].copy()
formation_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Attendance'].copy()
referee_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Captain'].copy()
match_report_1314 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Formation'].copy()

poss_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'xG'].copy()
attendance_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'xGA'].copy()
captain_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Poss'].copy()
formation_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Attendance'].copy()
referee_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Captain'].copy()
match_report_1415 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Formation'].copy()

poss_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'xG'].copy()
attendance_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'xGA'].copy()
captain_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Poss'].copy()
formation_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Attendance'].copy()
referee_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Captain'].copy()
match_report_1516 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Formation'].copy()

poss_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'xG'].copy()
attendance_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'xGA'].copy()
captain_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Poss'].copy()
formation_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Attendance'].copy()
referee_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Captain'].copy()
match_report_1617 = man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Formation'].copy()


pk_1213 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'FK'].copy()
pkatt_1213 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'PK'].copy()
mr_1213 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'PKatt'].copy()

pk_1314 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'FK'].copy()
pkatt_1314 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'PK'].copy()
mr_1314 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'PKatt'].copy()

pk_1415 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'FK'].copy()
pkatt_1415 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'PK'].copy()
mr_1415 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'PKatt'].copy()

pk_1516 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'FK'].copy()
pkatt_1516 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'PK'].copy()
mr_1516 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'PKatt'].copy()

pk_1617 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'FK'].copy()
pkatt_1617 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'PK'].copy()
mr_1617 = man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'PKatt'].copy()


#%%
# Place the values copied in the right place
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Poss'] = poss_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Poss'] = poss_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Poss'] = poss_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Poss'] = poss_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Poss'] = poss_1617

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Attendance'] = attendance_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Attendance'] = attendance_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Attendance'] = attendance_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Attendance'] = attendance_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Attendance'] = attendance_1617

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Captain'] = captain_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Captain'] = captain_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Captain'] = captain_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Captain'] = captain_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Captain'] = captain_1617

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Formation'] = formation_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Formation'] = formation_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Formation'] = formation_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Formation'] = formation_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Formation'] = formation_1617

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Referee'] = referee_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Referee'] = referee_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Referee'] = referee_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Referee'] = referee_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Referee'] = referee_1617

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'Match Report'] = match_report_1213
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'Match Report'] = match_report_1314
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'Match Report'] = match_report_1415
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'Match Report'] = match_report_1516
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'Match Report'] = match_report_1617


man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'PK'] = pk_1213
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'PKatt'] = pkatt_1213
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'Match Report'] = mr_1213

man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'PK'] = pk_1314
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'PKatt'] = pkatt_1314
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'Match Report'] = mr_1314

man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'PK'] = pk_1415
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'PKatt'] = pkatt_1415
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'Match Report'] = mr_1415

man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'PK'] = pk_1516
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'PKatt'] = pkatt_1516
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'Match Report'] = mr_1516

man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'PK'] = pk_1617
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'PKatt'] = pkatt_1617
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'Match Report'] = mr_1617


#%%
# Replace xG and xGA and FK with Nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'xG'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'xG'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'xG'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'xG'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'xG'] = np.nan

man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2012-2013', 'xGA'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2013-2014', 'xGA'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2014-2015', 'xGA'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2015-2016', 'xGA'] = np.nan
man_u_wigan_scores.loc[man_u_wigan_scores['Season'] == '2016-2017', 'xGA'] = np.nan

man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2012-2013', 'FK'] = np.nan
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2013-2014', 'FK'] = np.nan
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2014-2015', 'FK'] = np.nan
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2015-2016', 'FK'] = np.nan
man_u_wigan_shoots.loc[man_u_wigan_shoots['Season'] == '2016-2017', 'FK'] = np.nan





#%%
# Reading - NFO
# Select the Appropriate Answers
# poss_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'xG'].copy()
# attendance_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'xGA'].copy()
# captain_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Poss'].copy()
# formation_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Attendance'].copy()
# referee_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Captain'].copy()
# match_report_1213 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Formation'].copy()
#
# poss_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'xG'].copy()
# attendance_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'xGA'].copy()
# captain_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Poss'].copy()
# formation_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Attendance'].copy()
# referee_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Captain'].copy()
# match_report_1314 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Formation'].copy()

poss_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'xG'].copy()
attendance_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'xGA'].copy()
captain_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Poss'].copy()
formation_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Attendance'].copy()
referee_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Captain'].copy()
match_report_1415 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Formation'].copy()

poss_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'xG'].copy()
attendance_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'xGA'].copy()
captain_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Poss'].copy()
formation_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Attendance'].copy()
referee_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Captain'].copy()
match_report_1516 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Formation'].copy()

poss_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'xG'].copy()
attendance_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'xGA'].copy()
captain_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Poss'].copy()
formation_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Attendance'].copy()
referee_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Captain'].copy()
match_report_1617 = reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Formation'].copy()


# pk_1213 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'FK'].copy()
# pkatt_1213 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'PK'].copy()
# mr_1213 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'PKatt'].copy()
#
# pk_1314 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'FK'].copy()
# pkatt_1314 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'PK'].copy()
# mr_1314 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'PKatt'].copy()

pk_1415 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'FK'].copy()
pkatt_1415 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'PK'].copy()
mr_1415 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'PKatt'].copy()

pk_1516 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'FK'].copy()
pkatt_1516 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'PK'].copy()
mr_1516 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'PKatt'].copy()

pk_1617 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'FK'].copy()
pkatt_1617 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'PK'].copy()
mr_1617 = reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'PKatt'].copy()


#%%
# Place the values copied in the right place
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Poss'] = poss_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Poss'] = poss_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Poss'] = poss_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Poss'] = poss_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Poss'] = poss_1617

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Attendance'] = attendance_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Attendance'] = attendance_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Attendance'] = attendance_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Attendance'] = attendance_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Attendance'] = attendance_1617

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Captain'] = captain_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Captain'] = captain_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Captain'] = captain_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Captain'] = captain_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Captain'] = captain_1617

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Formation'] = formation_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Formation'] = formation_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Formation'] = formation_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Formation'] = formation_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Formation'] = formation_1617

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Referee'] = referee_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Referee'] = referee_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Referee'] = referee_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Referee'] = referee_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Referee'] = referee_1617

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'Match Report'] = match_report_1213
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'Match Report'] = match_report_1314
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'Match Report'] = match_report_1415
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'Match Report'] = match_report_1516
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'Match Report'] = match_report_1617


# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'PK'] = pk_1213
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'PKatt'] = pkatt_1213
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'Match Report'] = mr_1213
#
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'PK'] = pk_1314
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'PKatt'] = pkatt_1314
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'Match Report'] = mr_1314

reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'PK'] = pk_1415
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'PKatt'] = pkatt_1415
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'Match Report'] = mr_1415

reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'PK'] = pk_1516
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'PKatt'] = pkatt_1516
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'Match Report'] = mr_1516

reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'PK'] = pk_1617
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'PKatt'] = pkatt_1617
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'Match Report'] = mr_1617


#%%
# Replace xG and xGA with Nan
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'xG'] = np.nan
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'xG'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'xG'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'xG'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'xG'] = np.nan

# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2012-2013', 'xGA'] = np.nan
# reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2013-2014', 'xGA'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2014-2015', 'xGA'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2015-2016', 'xGA'] = np.nan
reading_nfo_scores.loc[reading_nfo_scores['Season'] == '2016-2017', 'xGA'] = np.nan

# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2012-2013', 'FK'] = np.nan
# reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2013-2014', 'FK'] = np.nan
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2014-2015', 'FK'] = np.nan
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2015-2016', 'FK'] = np.nan
reading_nfo_shoots.loc[reading_nfo_shoots['Season'] == '2016-2017', 'FK'] = np.nan


#%%

scores_fixtures = pd.concat([man_u_wigan_scores, reading_nfo_scores], axis=0, ignore_index=True)
shooting_stats = pd.concat([man_u_wigan_shoots, reading_nfo_shoots], axis=0, ignore_index=True)

#%%
scores_fixtures.shape
shooting_stats.shape

#%%
matches_2 = pd.merge(scores_fixtures, shooting_stats, how='left',
                     left_on=['Season', 'Team', 'Date', 'Comp',
                              'Time', 'Round', 'Day', 'Venue',
                              'Result', 'GF', 'GA', 'Opponent', 'xG',
                              'Match Report'],
                     right_on=['Season', 'Team', 'Date', 'Comp',
                               'Time', 'Round', 'Day', 'Venue',
                               'Result', 'GF', 'GA', 'Opponent', 'xG',
                               'Match Report'])

matches_2.info()

#%%
matches_2.to_csv('matches_2.csv', index=False)




