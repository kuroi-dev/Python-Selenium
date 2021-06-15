import time
import random
import math
from time import sleep
 

lista1 = [{"lunes"},{"martes"},{"miercoles"},{"jujueves"},{"friday"},{"saturday"},{"Sunday"}]
contador1 = 0

while contador1 < len(lista1):
    print(lista1[0])
    lista2 = 24
    contador2 = 0
    while contador2 < lista2:
        print(contador2)
        lista3 = 60
        contador3 = 0 
        while contador3 < lista3:
            print (contador3)
            lista4 = 60
            contador4 = 0   
            while contador4 < lista4:
                print(contador4)
                lista5 = 10
                contador5 = 0
                while contador5 < lista5:
                    print(contador5)
                    lista6 = 665
                    contador6 = 666
                    while contador6 > lista6:
                        print(contador6)
                        contador6-=1
                        sleep(random.uniform(0.00000000009,0.00000000001))
                    contador5+=1
                contador4+=1
            contador3+=1
        contador2+=1
    contador1+=1
