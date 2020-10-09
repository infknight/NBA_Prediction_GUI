from NBA_Stats_Scraper import NBA_Stats_Scraper
from math import *

nba_class = NBA_Stats_Scraper()
total_team_stats = nba_class.get_all_stats()


def get_name():
    i = 1
    output = "Please select the name of the team you want to analysis: \n"
    name_list = []
    for name in total_team_stats.keys():
        output+=str(i)
        output+=". "
        output+=name
        output+="\n"
        name_list.append(name)
        i+=1
    x = input(output)
    x = int(x)
    return name_list[x - 1]

print (get_name())

# oop class called team score that use fuzzy logic algorithms to compute some numbers
class team_score:
    team_name = get_name()
    # input name and get all the scores I need
    def __init__(self, name):







