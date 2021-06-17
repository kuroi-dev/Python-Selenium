import math
import random
from time import sleep
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('./chromedriver')
sleep(random.uniform(2.0,3.0))

browser.set_window_size(1400, 1000)

sleep(random.uniform(2.0,3.0))


print("Paso 0")
browser.get('https://www.jumbo.cl/')
sleep(random.uniform(3.0,5.0))
validacion0 = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[3]/div/div[2]/div[1]/div/button').text
sleep(random.uniform(0.5,1.0))
print(validacion0)
sleep(random.uniform(3.0,5.0))
texto0 = "Modo de entrega"
sleep(random.uniform(8.0,10.0))
if validacion0 == texto0:
    print("Validacion correcta")
else:
    print("Error")
sleep(random.uniform(3.0,5.0))


print("Paso 1")
btnuno = browser.execute_script('document.getElementsByClassName("new-header-supermarket-title")[3].click()')
sleep(random.uniform(8.0,10.0))
validacion1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/main/div[4]/div[1]/div/div[1]/div[1]/nav/ul/li[2]/a').text
sleep(random.uniform(3.0,5.0))
texto1 = "Arroz, Legumbres y Semillas"
sleep(random.uniform(4.0,8.0))
if validacion1 == texto1:
    print("Validacion correcta")
else:
    print("Error")
sleep(random.uniform(3.0,5.0))


print("Paso 2")
btndos = browser.execute_script('document.getElementsByClassName("catalog-aside-nav-link")[1].click()')
sleep(random.uniform(4.0,8.0))
validacion2 = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/main/div[4]/div[2]/div[1]/ul/li[1]/div/div[3]/div/div/button/span').text
sleep(random.uniform(3.0,5.0))
texto2 = "Agregar"
sleep(random.uniform(4.0,8.0))
if validacion2 == texto2:
    print("Validacion correcta")
else:
    print("Error")
sleep(random.uniform(3.0,5.0))
