from Tkinter import *
from Player import Player
from TibiaWebscraper import TibiaWebscraper

# TODO Calc global top players (if lvl > prevLvl = highest)
# TODO List top players: level;server;name
# TODO Listbox + scrollbar not fixed position. Fix/display the button

class GUI(Frame):
    def __init__(self, master):
        frame = Frame.__init__(self, master)
        # self.grid()

        scrollbar = Scrollbar(frame, orient=VERTICAL)
        # self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

        self.listbox = Listbox(frame, yscrollcommand=scrollbar.set, width = 42, height = 30)
        self.listbox.grid(row = 1, column = 0)

        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

        self.btnListTopPlayers = Button(self, text = "Show char info")#, command = self.generate_top_players) Actionbutton to be developed
        self.btnListTopPlayers.grid(row = 0, column = 0, sticky = W)
        self.btnListTopPlayers.pack()

        self.generate_top_players()

    def generate_top_players(self):
        webscraper = TibiaWebscraper()
        servers = webscraper.get_worlds()
        top_players = webscraper.generate_top_players()
        for i in range(top_players.__len__()):
            self.listbox.insert(i, top_players[servers[i]].level + ";" + servers[i] + ";" + top_players[servers[i]].name)