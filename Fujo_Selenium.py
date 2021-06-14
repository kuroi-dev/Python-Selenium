# Python-Selenium


	import math
	import random
	from time import sleep
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By


	browser = webdriver.Chrome('./chromedriver')
	browser.get('https://docs.google.com/forms/d/e/1FAIpQLSchJzBQMz0z3Z_wLd_kBOH-IIbPRHkV1rYibPEZtTwgtQiQYA/viewform')
	sleep(random.uniform(3.0,5.0))
	mail = browser.find_element_by_xpath('//*[@id="identifierId"]')
	sleep(random.uniform(0.5,1.0))
	mail.click()
	sleep(random.uniform(0.5,1.0))
	mail.send_keys('xxxxxxxxxxxxxxx')
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

	date1 = [("01062021") , ("02062021") , ("03062021") , ("04062021") , ("05062021")]

	date = '05062021'

	lista1 = [("Banco Central","970290001"), ("Claro","96799250K"), ("Grupo Falabella","776124109"), ("Inacap","720120003"), ("PUC","816989000"), ("Clinica Universidad de Los Andes","0"), ("Dipres","608020004"), ("Banchile","965712208"), ("Previred","969293900"), ("Saesa","779655504")]
	lista2 = [("Banco Patagonia","30500006613") , ("Nastec","763371093") , ("Atentus","772375700") , ("BCI","970060006")  , ("Banco Chile","970040005") , ("AFP Habitat","980001008")]

	text1 = 'Revision ticket del turno'

	conteo = 0

	indice = 0
	while indice < len(lista1):

		clock = random.uniform(10,20)

		clock = round(clock,0)

		clock1 = int(clock)

		clock2 = str(clock1)

		print(clock2)

		fecha = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
		sleep(random.uniform(0.5,1.0))

		fecha.send_keys(date)
		sleep(random.uniform(1.0,2.0))

		user = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
		sleep(random.uniform(0.5,1.0))
		user.click()
		sleep(random.uniform(0.5,1.0))
		user1 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]')
		sleep(random.uniform(0.5,1.0))
		user1.click()
		sleep(random.uniform(1.0,2.0))
		cargo = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
		sleep(random.uniform(0.5,1.0))
		cargo.click()
		sleep(random.uniform(0.5,1.0))
		cargo2 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
		sleep(random.uniform(0.5,1.0))
		cargo2.click()
		sleep(random.uniform(1.0,2.0))
		cliente = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
		sleep(random.uniform(0.5,1.0))
		cliente.click()
		sleep(random.uniform(0.5,1.0))

		cliente.send_keys(lista1[indice][0])
		sleep(random.uniform(1.0,2.0))
		idcliente = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
		sleep(random.uniform(0.5,1.0))
		idcliente.click()
		sleep(random.uniform(0.5,1.0))

		idcliente.send_keys(lista1[indice][1])
		sleep(random.uniform(2.0,4.0))
		actividad0 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[1]')
		sleep(random.uniform(0.5,1.0))
		actividad0.click()
		sleep(random.uniform(0.5,1.0))
		actividad1 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[3]')
		sleep(random.uniform(0.5,1.0))
		actividad1.click()
		sleep(random.uniform(1.0,2.0))
		proyect = browser.find_element_by_xpath('//*[@id="i31"]')
		sleep(random.uniform(0.5,1.0))
		proyect.click()
		sleep(random.uniform(1.0,2.0))
		hora1 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
		sleep(random.uniform(0.5,1.0))
		hora1.click()
		sleep(random.uniform(0.5,1.0))
		hora1.send_keys('00')
		sleep(random.uniform(0.5,1.0))
		hora2 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
		sleep(random.uniform(0.5,1.0))
		hora2.click()
		sleep(random.uniform(0.5,1.0))
		hora2.send_keys(clock2)
		sleep(random.uniform(1.0,2.0))
		comentario = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea')
		sleep(random.uniform(0.5,1.0))
		comentario.click()
		sleep(random.uniform(0.5,1.0))
		comentario.send_keys(text1)
		sleep(random.uniform(1.0,2.0))
		enviar = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div/div')
		sleep(random.uniform(0.5,1.0))
		enviar.click()
		sleep(random.uniform(5.0,8.0))
		nuevo = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
		sleep(random.uniform(0.5,1.0))
		nuevo.click()
		sleep(random.uniform(20.0,30.0))
		indice+=1


