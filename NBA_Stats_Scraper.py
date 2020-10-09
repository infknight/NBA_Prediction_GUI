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

    def espn_stats_table_standing(self, URL):
        soup = self.request(URL)
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

        # getting all the team's name
        for i in team_name:
            index_first = i.find("title=")
            index_last = i.rfind('"')
            # parse the string between first find the title= and last " .
            team.append(i[index_first + 7:index_last])
        res = dict.fromkeys(team)
        return res

    def espn_stats_table_traditional(self, URL):
        soup = self.request(URL)
        header = []
        for data in soup.find_all('th', {'class' : 'Table__TH'}):
            header.append(data.text)
        # we not want the first 2 arguments; therefore, we poped it.
        header.pop(0)
        header.pop(0)

        count = 0
        stats = []
        for data in soup.find_all('td',{'class': 'Table__TD'}):
            temp = (''.join(data.findAll(text=True)))
            if count > 59:
                stats.append(temp)
            # print (''.join(data.findAll(text=True)))
            count+=1

        list_of_dict = []
        for i in range(30):
            name = {header[j%19] : stats[19*i+j%len(stats)] for j in range(19)}
            list_of_dict.append(name)
        return list_of_dict

    def stats_combine(self, team_name, team_stats):
        stats = {}
        stats = dict(zip(team_name, team_stats))
        return stats

    def hash_combine_helper(self, dictA, dictB, path = None):

        if path is None: path = []
        for key in dictB:
            if key in dictA:
                if isinstance(dictA[key], dict) and isinstance(dictB[key], dict):
                    self.hash_combine_helper(dictA[key], dictB[key], path + [str(key)])
                elif dictA[key] == dictB[key]:
                    pass
                else:
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
            else:
                dictA[key] = dictB[key]
        return dictA

    def get_all_stats(self):
        nba = NBA_Stats_Scraper()
        team_standing = nba.espn_team_name_standing(standing_URL)
        team_standing_stats = nba.espn_stats_table_standing(standing_URL)
        team_standing_total = nba.stats_combine(team_standing, team_standing_stats)

        team_traditional = nba.espn_team_name_traditional(tradition_stats_URL)
        team_traditional_stats = nba.espn_stats_table_traditional(tradition_stats_URL)
        team_traditional_total = nba.stats_combine(team_traditional, team_traditional_stats)

        team_all_stats = nba.hash_combine_helper(team_standing_total, team_traditional_total)
        return team_all_stats


def main():
    nba = NBA_Stats_Scraper()
    team_standing = nba.espn_team_name_standing(standing_URL)
    team_standing_stats = nba.espn_stats_table_standing(standing_URL)
    team_standing_total = nba.stats_combine(team_standing, team_standing_stats)

    team_traditional = nba.espn_team_name_traditional(tradition_stats_URL)
    team_traditional_stats = nba.espn_stats_table_traditional(tradition_stats_URL)
    team_traditional_total = nba.stats_combine(team_traditional, team_traditional_stats)

    team_all_stats = nba.hash_combine_helper(team_standing_total, team_traditional_total)
    print ((team_all_stats.get("Houston Rockets").get("W")))

if __name__ == "__main__":
    main()
