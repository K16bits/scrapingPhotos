from platform import processor
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
        self.postagens = []
        self.linkFotos = []
    
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

        driver.get("https://www.instagram.com/"+self.email)
        self.scrollFinal()
        self.pegarLinksPostagens()
      
    def scrollFinal(self):
        driver = self.driver
        alturaAnterior = driver.execute_script("return document.body.scrollHeight")  #Referencia https://qastack.com.br/programming/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            altura = driver.execute_script("return document.body.scrollHeight")
            if(alturaAnterior == altura):
                break   
            alturaAnterior = altura  

    def pegarLinksPostagens(self):
        drive = self.driver
        lista_link = drive.find_elements_by_tag_name('a')
        for i in lista_link:
            if "/p/" in i.get_attribute('href'):
                self.postagens.append(i.get_attribute('href'))

    
    def listarPost(self):
        print(self.postagens)
        print('Quantidade de link: ',len(self.postagens))
    
    def navegarLinks(self,postLink):
        driver = self.driver
        driver.get(postLink)
        link = driver.find_element_by_class_name('FFVAD').get_attribute('src')
        self.linkFotos.append(link)

    def pegarTodasFotos(self):
        for i in self.postagens:
            self.navegarLinks(i)

        for i in self.linkFotos:
            print(i)

  
    def close(self):
        drive = self.driver.close()
        
bot = Bot(EMAIL,SENHA)
bot.logar()
bot.pegarLinksPostagens()
bot.pegarTodasFotos()
bot.listarPost()
#time.sleep(5)
#bot.close()


