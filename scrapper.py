import requests
from bs4 import BeautifulSoup

def request(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def espn_team_name():
    soup = request('https://www.espn.com/nba/standings')
    # String of all the teams
    team_name_class = soup.find_all("abbr")
    team_name_list = []
    team = []

    # convert it into a list of strings
    for x in team_name_class:
        team_name_list.append(str(x))

    for i in (team_name_list):
        index_first = i.find("title=")
        index_last = i.rfind('"')
        # parse the string between first find the title= and last " .
        team.append(i[index_first + 7:index_last])
    #create a hash with key and no values for now yet
    res = dict.fromkeys(team)
    # returns a dictionary key is the team name and none as its value
    return res

def espn_stats_table():
    soup = request('https://www.espn.com/nba/standings')
    header = soup.find_all('span', {'class' : 'fw-medium w-100 dib tar subHeader__item--content underline'}, )
    print(header)
    # parsed all the data points
    for data in soup.find_all('span', {'class' : 'stat-cell'}):
        team_stat=[]
        team_stat.append(''.join(data.findAll(text=True))) # Find all the text in the class tag

    # return team_stat

espn_stats_table()