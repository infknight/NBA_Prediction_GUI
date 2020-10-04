import requests
from bs4 import BeautifulSoup


class NBA_Stats_Scraper:

    def request(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup


    def espn_team_name(self):
        soup = self.request('https://www.espn.com/nba/standings')
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

    def espn_stats_table(self):
        soup = self.request('https://www.espn.com/nba/standings')
        # find the header for the table
        header = []
        counter = 0
        # parsed the data header to
        for data in soup.find_all('th', {'class' : 'tar subHeader__item--content Table__TH'}, ):
            header.append(data.text)
            counter+=1
            if counter >= 14:
                break
        header.pop(0)

        team_stat=[]
        # parsed all the data points
        for data in soup.find_all('span', {'class' : 'stat-cell'}):
            temp = (''.join(data.findAll(text=True)))
            team_stat.append(temp) # Find all the text in the class tag

        list_of_dict = []
        # Create 30 hash's name for each team's stat
        for i in range(30):
            name = "team" + str(i)
            name = dict()
            name = {header[j%13] : team_stat[13*i+j%len(team_stat)] for j in range(13)}
            list_of_dict.append(name)

        print(len(list_of_dict))
        return list_of_dict

