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

# print (total_team_stats.get(get_name()).get("W"))

# oop class called team score that use fuzzy logic algorithms to compute some numbers
class team_score:
    # input name and get all the scores I need
    # team_name = get_name()
    # team = None
    # def __init__(self, team_name=get_name()):
    #     self.team = team_name
    #     PCT = total_team_stats.get(get_name())
    #
    # def __str__(self):
    #     return self.name, self.PCT

def main():
    print (1)

if __name__ == "__main__":
    main()









