import requests
from bs4 import BeautifulSoup

def espn():
    url = 'https://www.espn.com/nba/standings'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_of_web = soup.select('title')

    # String of all the teams
    team_name_class = soup.find_all("abbr")
    team_name_list = []

    # convert it into a list of strings
    for x in team_name_class:
        team_name_list.append(str(x))

    for i in (team_name_list):
        index_first = i.find("title=")
        index_last = i.rfind('"')
        print(i[index_first + 7:index_last])


