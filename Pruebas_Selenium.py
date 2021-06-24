import math
import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('./chromedriver')

sleep(random.uniform(2.0,3.0))
browser.set_window_size(1500, 1000)
sleep(random.uniform(2.0,3.0))

browser.get('xxxxxxxxxxxxxxxxxxxxxxxx')
sleep(random.uniform(3.0,5.0))

mail = browser.find_element_by_xpath('//input[@id="sesion_login"]')
sleep(random.uniform(0.5,1.0))
mail.click()
sleep(random.uniform(0.5,1.0))
mail.send_keys('xxxxxxxxxxxxxxxxxxxx')
sleep(random.uniform(1.0,2.0))

passw = browser.find_element_by_xpath('//input[@id="sesion_password"]')
sleep(random.uniform(0.5,1.0))
passw.click()
sleep(random.uniform(0.5,1.0))
passw.send_keys('xxxxxxxxxxxxxx')
sleep(random.uniform(1.0,2.0))

login = browser.find_element_by_xpath('//input[@name="commit"]')
sleep(random.uniform(0.5,1.0))
login.click()
sleep(random.uniform(0.5,1.0))

#________________________________________________________________

browser.get('https://admin-tres.atentus.com/exportacion_datos/pasos_por_objetivo')
sleep(random.uniform(3.0,5.0))

exportar = browser.find_element_by_xpath('//input[@name="exportar"]')
sleep(random.uniform(0.5,1.0))
exportar.click()
sleep(15)


#####_____________________________________________________________

def fileUploading():

    browser.get('https://accounts.google.com/signin/v2/identifier?service=writely&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    sleep(random.uniform(3.0,5.0))
    mail = browser.find_element_by_xpath('//*[@id="identifierId"]')
    sleep(random.uniform(0.5,1.0))
    mail.click()
    sleep(random.uniform(0.5,1.0))
    mail.send_keys('xxxxxxxxxxxxxxxxxxx')
    sleep(random.uniform(0.5,1.0))
    siguiente1 = browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    sleep(random.uniform(0.5,1.0))
    siguiente1.click()
    sleep(random.uniform(3.0,5.0))
    password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    sleep(random.uniform(0.5,1.0))
    password.click()
    sleep(random.uniform(0.5,1.0))
    password.send_keys('xxxxxxxxxxxxxxxxxxxx')
    sleep(random.uniform(0.5,1.0))
    siguiente2 = browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
    sleep(random.uniform(0.5,1.0))
    siguiente2.click()
    sleep(random.uniform(5.0,7.0))

    browser.get('https://drive.google.com/drive/u/0/folders/1m9J8tIlBxqMNDbGRmwLMedVXxD06CXOJ')
    sleep(random.uniform(3.0,5.0))
    s = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/button[1]')
    sleep(random.uniform(1.0,2.0))
    s.click()
    sleep(random.uniform(1.0,2.0))
    s.send_keys(Keys.DOWN)
    sleep(random.uniform(3.0,5.0))
    s.send_keys(Keys.ENTER)
    sleep(random.uniform(3.0,5.0))
    s = os.system("chmod -R 777 /home/driquelme/Descargas/estados_de_objetivos-20210620172637.xlsx")
    sleep(random.uniform(3.0,5.0))

fileUploading()
