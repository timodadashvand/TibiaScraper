from GUI import GUI
from Tkinter import *

class Main:
    root = Tk()
    root.title("Tibia webscraper")
    root.geometry("250x500")
    app = GUI(root)
    app.mainloop()