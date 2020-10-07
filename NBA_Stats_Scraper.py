import requests
from bs4 import BeautifulSoup

standing_URL = 'https://www.espn.com/nba/standings'
tradition_stats_URL = 'https://www.espn.com/nba/stats/team/_/season/2020/seasontype/2'

class NBA_Stats_Scraper:

    def request(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup


    def espn_team_name_standing(self, URL):
        soup = self.request(URL)
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

    def espn_stats_table_standing(self):
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
        return list_of_dict

    def espn_team_name_traditional(self, URL):
        soup = self.request(URL)
        res = {}
        team_name= []
        team_name_str = soup.find_all('img',{'class':'Image Logo Logo__sm'})
        for x in team_name_str:
            team_name.append(str(x))
        team = []
        for i in team_name:
            index_first = i.find("title=")
            index_last = i.rfind('"')
            # parse the string between first find the title= and last " .
            team.append(i[index_first + 7:index_last])
        res = dict.fromkeys(team)
        return res


    def final_stats_standing(self, team_name, team_stats):
        # team_name = self.espn_team_name_standing(standing_URL)
        # team_stats = self.espn_stats_table()
        stats = {}
        stats = dict(zip(team_name, team_stats))
        # print (str(stats))
        return stats




def main():
    nba = NBA_Stats_Scraper()
    team = nba.espn_team_name_traditional(tradition_stats_URL)
    print (team)


if __name__ == "__main__":
    main()
