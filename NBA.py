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
#url_adv = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Advanced&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
#url_misc = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Misc&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
#url_fourfactors = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Four+Factors&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
#url_scoring = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Scoring&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'
#url_opponent = 'http://stats.nba.com/stats/leaguedashteamstats?Season=2012-13&SeasonType=Regular+Season&MeasureType=Opponent&PerMode=Totals&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&DateFrom=&DateTo=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&GameScope=&PlayerExperience=&PlayerPosition=&StarterBench=&sortField=PTS&sortOrder=DES'

#read JSON response from the web URL
response_base = urlopen(url_base)

# <codecell>

#Parse the JSON response into a Python dictionary
JSON_base = json.load(response_base)

# <codecell>

#convert the useful data into a Panda DataFrame
table_base = pd.DataFrame(JSON_base['resultSets'][0]['rowSet'], columns=JSON_base['resultSets'][0]['headers'])

# <codecell>

table_base

# <codecell>


# <codecell>


