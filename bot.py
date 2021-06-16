from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

from config import EMAIL, SENHA

class Bot:
    def __init__(self,email,senha,alvo=''):
        self.email = email
        self.senha = senha
        self.alvo = alvo
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
    
    def logOff(self):
        drive = self.driver
        drive.get("https://www.instagram.com/"+self.email)
        clickPerfil = drive.find_element_by_class_name("_6q-tv")
        clickPerfil.click()
        time.sleep(1)
        clickSair = drive.find_element_by_xpath(r"//div[contains(text(),'Sair')]")
        clickSair.click()
    
    def UsuarioAlvo(self):
        drive = self.driver
        drive.get("https://www.instagram.com/"+self.alvo)
        self.scrollFinal()

      
    def scrollFinal(self):   #Scroll até o final da pagina
        driver = self.driver #Referencia https://qastack.com.br/programming/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
        alturaAnterior = driver.execute_script("return document.body.scrollHeight")  
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.3)
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
    
    def salvarFoto(self):
        drive = self.driver
        for i in range(len(self.linkFotos)):
            drive.get(self.linkFotos[i])
            drive.get_screenshot_as_file('./prints/'+str(i)+'.png')
            
  
    def close(self):
        self.driver.close()
        
bot = Bot(EMAIL,SENHA)
bot.logar()
bot.UsuarioAlvo()
bot.pegarLinksPostagens()
bot.pegarTodasFotos()
bot.listarPost()
bot.salvarFoto()
bot.logOff()
#time.sleep(5)
bot.close()
exit()