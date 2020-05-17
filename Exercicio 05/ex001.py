# Faça um programa de contagem regreciva 
from time import sleep 
numero = int(input("Digote numero: "))


for cont in range(numero, 0 ,-1):
    sleep(2)
    print(cont)
print("BOOM ")
