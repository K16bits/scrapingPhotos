from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

class Bot:
    def __init__(self,nick,password):
        self.nick = nick
        self.password = password
        self.pathdrive = os.getcwd()+"/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = self.pathdrive)
    
    def logar(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        

bot = Bot('kami',1231)
bot.logar()