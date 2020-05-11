#escreva um programa que faça o computador "pensar" em um número inteiro é peça para o usuario descobrir qual foi 
# numero escolhido pelo computador.O progrma deverá escrever uma messagem usuario venceu ou perdeu

from random import randint
numero = int (input('Digite um nuemro: '))

computador = randint(0,5)

if numero == computador :
    print("você venceu")
    print("computador pensou no nuemro {}".format(computador))
else:
    print("voce perdeu")    
    print("computador pensou no nuemro {}".format(computador))