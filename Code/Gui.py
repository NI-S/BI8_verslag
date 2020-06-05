from tkinter import filedialog
import selenium
from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import os

class Gui:
    def __init__(self):
        self.filename = filedialog.askopenfilename()
        print(os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe").replace("\\", "/"))

    def __remove_duplicates__(self):
        file = open(self.filename, "r")


    def __mafft__(self):
        self.driver.get("https://mafft.cbrc.jp/alignment/server/")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@id='mv']/form/div/div[1]/p[1]/input").send_keys(self.filename)
        self.driver.find_element_by_xpath("//*[@id='mv']/form/div/p[4]/input[1]").send_keys("\n")

    def __clustalo__(self):
        self.driver.get("https://www.ebi.ac.uk/Tools/msa/clustalo/")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id("upfile").send_keys(self.filename)
        #self.driver.find_element_by_name("name").send_keys("\n")
        self.driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").send_keys('\n')

gui = Gui()
#gui.__mafft__()
gui.__clustalo__()

