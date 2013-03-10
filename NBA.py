# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import json
from urllib2 import urlopen
pd.set_option('display.max_columns', 30)

# <codecell>

#Web URL to the JSON data source is obtained from NBA.com
url_base = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Base&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
url_adv = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Advanced&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
url_misc = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Misc&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
url_fourfactors = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Four+Factors&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
url_scoring = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Scoring&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
url_opponent = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Opponent&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'

#read JSON response from the web URL
response_base = urlopen(url_base)
response_adv = urlopen(url_adv)
response_misc = urlopen(url_misc)
response_fourfactors = urlopen(url_fourfactors)
response_scoring = urlopen(url_scoring)
response_opponent = urlopen(url_opponent)

# <codecell>

#Parse the JSON response into a Python dictionary
JSON_base = json.load(response_base)
JSON_adv = json.load(response_adv)
JSON_misc = json.load(response_misc)
JSON_fourfactors = json.load(response_fourfactors)
JSON_scoring = json.load(response_scoring)
JSON_opponent = json.load(response_opponent)

# <codecell>

#convert the useful data into a Panda DataFrame
table_base = pd.DataFrame(JSON_base['resultSets'][0]['rowSet'], columns=JSON_base['resultSets'][0]['headers'])
table_adv = pd.DataFrame(JSON_adv['resultSets'][0]['rowSet'], columns=JSON_adv['resultSets'][0]['headers'])
table_misc = pd.DataFrame(JSON_misc['resultSets'][0]['rowSet'], columns=JSON_misc['resultSets'][0]['headers'])
table_fourfactors = pd.DataFrame(JSON_fourfactors['resultSets'][0]['rowSet'], columns=JSON_fourfactors['resultSets'][0]['headers'])
table_scoring = pd.DataFrame(JSON_scoring['resultSets'][0]['rowSet'], columns=JSON_scoring['resultSets'][0]['headers'])
table_opponent = pd.DataFrame(JSON_opponent['resultSets'][0]['rowSet'], columns=JSON_opponent['resultSets'][0]['headers'])

# <codecell>

table_base

# <codecell>

table = pd.merge(table_base, table_adv, on=['TEAM_ID', 'TEAM_NAME'], suffixes=['','_adv'])

# <codecell>

table.T

# <codecell>


