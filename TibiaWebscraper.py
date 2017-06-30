from bs4 import BeautifulSoup
import urllib
import re
from Player import Player

# TODO Fix Player object in dictionary/tuple

class TibiaWebscraper:
    __worlds = []

    def generate_top_players(self):
        htmlfile = urllib.urlopen('http://www.tibia.com/community/?subtopic=worlds')
        soup = BeautifulSoup(htmlfile, 'html.parser')

        for link in soup.find_all('a',
                                  href=re.compile('^https://secure\.tibia\.com/community/\?subtopic=worlds&world=')):
            self.__worlds.append(link.get_text())

        return self.generate_players(self.__worlds)

    def generate_players(self, worlds):
        count = 0
        top_players = {}
        name = ""
        sex = ""
        vocation = ""
        level = ""
        ach_points = ""
        world = ""
        residence = ""
        last_log = ""
        # acc_status = ""

        for server in worlds:
            status = False
            while (status == False):
                # Reqeusts top players for 'world'
                htmlfile = urllib.urlopen('https://secure.tibia.com/community/?subtopic=highscores&world=' + server)
                soup = BeautifulSoup(htmlfile, 'html.parser')

                # Requests top leveled player for 'world'
                link_top_player = soup.find('a', href=re.compile(
                    'https://secure\.tibia\.com/community/\?subtopic=characters&name='))

                if (link_top_player):
                    name = link_top_player.get_text()

                    # Requests character info of top leveled player for 'world'
                    htmlfile = urllib.urlopen('https://secure.tibia.com/community/?subtopic=characters&name=' + name)
                    soup = BeautifulSoup(htmlfile, 'html.parser')

                    # Checking if html-page is loaded (if 'td' has value)
                    if soup.find("td", text="Sex:") is not None:

                        # Requests character info of top leveled player for 'world'
                        sex = soup.find("td", text="Sex:").find_next_sibling("td").text
                        vocation = soup.find("td", text="Vocation:").find_next_sibling("td").text
                        level = soup.find("td", text="Level:").find_next_sibling("td").text
                        ach_points = soup.find("td", text="Achievement Points:").find_next_sibling("td").text
                        world = soup.find("td", text="World:").find_next_sibling("td").text
                        residence = soup.find("td", text="Residence:").find_next_sibling("td").text
                        last_log = soup.find("td", text="Last Login:").find_next_sibling("td").text
                        # Complex - To be developed
                        # acc_status = soup.find("td", text="Account\&#160;Status:").find_next_sibling("td").text
                        # print acc_status
                        # Prints top player per server
                        print server + ": " + name + " - LOADED"
                        top_players[server] = Player(name, sex, vocation, level, ach_points, world, residence, last_log)#, acc_status) Complex - To be developed

                        status = True

                else:
                    # Count number of times top player is null
                    count += 1
        res = "Number of callbacks due to null-value: " + `count`
        print res
        return top_players

    def get_worlds(self):
        return self.__worlds