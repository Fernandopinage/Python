# cria um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla. depois disso mostre a lista de numeros gerados 
# e tambem mostre o maior e menor numeros.

from random import randint

random =  randint(0, 9)

valores = (randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9))
print(valores)
maior = 0
menor = 10

for n in valores:
    if n <= menor :
        menor = n
    elif n >= maior:
        maior = n

print("O maior numero entre arrays é {}".format(maior))
print("O menor numero entre arrays é {}".format(menor))        
