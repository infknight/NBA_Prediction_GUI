from NBA_Stats_Scraper import NBA_Stats_Scraper
from math import *

nba_class = NBA_Stats_Scraper()
total_team_stats = nba_class.get_all_stats()
opp_stats = nba_class.get_opp_stats()


def convert_float_type(x):
    return float(x)

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
    team_name = None
    win_percentage = 0.0 # PCT
    field_goal_pt = 0.0 # FG%
    turn_over = 0.0 # TO
    off_rebound = 0.0 # REB
    free_throw = 0.0 # FT%

    opp_field_goal_pt = 0.0 # FG%
    opp_turn_over = 0.0 # TO
    opp_rebound = 0.0 # REB
    opp_free_throw = 0.0 # FT%

    # constructor takes 1 parameter
    def __init__(self, team):
        self.team_name = team
        self.win_percentage = total_team_stats.get(team).get("PCT")
        self.field_goal_pt = total_team_stats.get(team).get("FG%")
        self.turn_over = total_team_stats.get(team).get("TO")
        self.rebound = total_team_stats.get(team).get("OR")
        self.free_throw = total_team_stats.get(team).get("FT%")
        # this is the opponent stats
        self.opp_field_goal_pt = opp_stats.get(team).get("FG%")
        self.opp_turn_over = opp_stats.get(team).get("TO")
        self.opp_rebound = opp_stats.get(team).get("DR")
        self.opp_free_throw = opp_stats.get(team).get("FT%")



    def four_factor_analysis(self):
        team_factors = 40 * convert_float_type(self.field_goal_pt) - 25 * convert_float_type(self.turn_over) + 20 * convert_float_type(self.rebound) + 15 * convert_float_type(self.free_throw)
        opp_factors = -40 * convert_float_type(self.opp_field_goal_pt) + 25 * convert_float_type(self.opp_turn_over) + 20 * convert_float_type(self.opp_rebound) - 10 * convert_float_type(self.opp_free_throw)
        return team_factors + opp_factors
        # return self.convert_float_type(self.field_goal_pt) * 0.4 + self.convert_float_type(self.turn_over) * 0.25 + self.convert_float_type(self.rebound) * 0.2 + self.convert_float_type(self.free_throw) * 0.15
        # return float(self.field_goal_pt) * 0.4 + float(self.turn_over) * 0.25 + float(self.rebound * 0.2) + float(self.free_throw) * 0.15


    # the toString function
    def __str__(self):
        return self.team_name + "\n" + self.win_percentage  + "\n" + self.field_goal_pt + "\n" + self.turn_over + "\n" + self.rebound + "\n" + self.free_throw


def main():
    t1 = team_score(get_name())
    t2 = team_score(get_name())
    print (t1.four_factor_analysis())
    print (t2.four_factor_analysis())

if __name__ == "__main__":
    main()









