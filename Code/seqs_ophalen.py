import selenium
from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import os
from tkinter import *



class Pfam:
    def __init__(self):
        self.site = "https://pfam.xfam.org/search#tabview=tab2"

    def __ask_protein__(self):
        self.master = Tk()
        self.master.geometry("300x100")
        self.master.title("Choose protein")
        self.variable = StringVar(self.master)
        self.variable.set("Neuraminidase")  # default value
        OptionMenu(self.master, self.variable, "Neuraminidase", "Haemagglutinin", "Porin_1", "META domain", "Thioredoxin").pack()
        Button(self.master, text="Confirm", command=self.__confirm__).pack(padx=5, side=RIGHT)
        Button(self.master, text="Close", command=self.__close__).pack(padx=5, side=RIGHT)
        self.master.mainloop()

    def __close__(self):
        self.master.destroy()

    def __confirm__(self):
        self.chosen_protein=self.variable.get()
        self.__pfam_search__()

    def __pfam_search__(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe").replace("\\", "/"))
        self.driver.get(self.site)
        self.driver.find_element_by_link_text("Keyword").click()
        self.driver.find_element_by_id("kwQuery").send_keys(self.chosen_protein)
        self.driver.find_element_by_xpath("//*[@id='keywordSearchForm']/div[2]/input[1]").click()
        elementen = self.driver.find_elements_by_class_name("rowNum")
        for i in range(len(elementen)):
            if i != 0:
                if self.chosen_protein.__eq__("Porin_1"):
                    if self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr[" + str(i) + "]/td[3]").text.__eq__(self.chosen_protein):
                        self.driver.find_element_by_xpath(
                            "//*[@id='resultTable']/tbody/tr[" + str(i) + "]/td[2]/a").send_keys("\n")
                        break
                if self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+str(i)+"]/td[4]").text.__eq__(self.chosen_protein):
                    self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+str(i)+"]/td[2]/a").send_keys("\n")
                    break
        self.__download_seq__()

    def __download_seq__(self):
        self.driver.find_element_by_id("seqIcon").click()
        self.driver.find_element_by_partial_link_text("download").send_keys("\n")

pfam = Pfam()
pfam.__ask_protein__()
