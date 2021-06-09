from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

from config import EMAIL, SENHA

class Bot:
    def __init__(self,email,senha):
        self.email = email
        self.senha = senha
        self.pathdrive = os.getcwd()+"/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = self.pathdrive)
    
    def logar(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        campo_Username = driver.find_element_by_xpath(r"//input[@name='username']")
        campo_Username.click()
        campo_Username.send_keys(self.email)

        campo_Senha = driver.find_element_by_xpath(r"//input[@name='password']")
        campo_Senha.click()
        campo_Senha.send_keys(self.senha)
        campo_Senha.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get("https://www.instagram.com/")
    
    def close(self):
        drive = self.driver;
        drive.close()
        

bot = Bot(EMAIL,SENHA)
bot.logar()
bot.close()
time.sleep(5)
exit()
