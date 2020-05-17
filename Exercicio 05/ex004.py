# Cria um programa que faça tabuada usando laço 

numero = int(input('digite um numero da tabuada: '))

cont = 0
for i in  range(0,10):
    cont +=1
    total = numero * cont
    print("{} x {} = {}".format(numero,cont,total))