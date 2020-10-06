from NBA_Stats_Scraper import NBA_Stats_Scraper
from math import *
nba_class = NBA_Stats_Scraper()
nba_stats = nba_class.final_stats()
# print (str(nba_stats))
def get_score(team_a, team_b):
    if team_a == team_b:
        print ("Do not choose the same team")
        get_score(team_a, team_b)
    else:
        temp = nba_stats.get(team_a)
        print (type(temp))
        print (temp.get("PCT"))



get_score("Milwaukee Bucks", "Toronto Raptors")



