import selenium
from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import os
from tkinter import *


class Pfam:
    def __init__(self):
        self.site = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe").replace("\\", "/"))
        master = Tk()

        variable = StringVar(master)
        variable.set("one")  # default value

        w = OptionMenu(master, variable, "one", "two", "three")
        w.pack()

        mainloop()

