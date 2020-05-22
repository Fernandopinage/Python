# Faça um programa que jogue 'par' ou 'impar' com o computador. O jogo so devera ser interrompido quando o jogador perde , mostre o total de vitorias

from random import randint

random = randint(1,2)
total = 0
cont = 0
while True:
    print("=-"*20)
    print("Vamos jogar 'Par' ou 'Impar'")
    print("=-"*20)

    numero = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar [P/I]')).upper()
    total = random + numero
    if total % 2 == 1:
        resultado = 'P'
    else:
        resultado = 'I'
  
    if escolha == resultado:
        print("Eu vence !!!")
        cont += 1
    else:
        print("Eu perdi :( ")
        break
print('total de vezes que eu joguei {}'.format(cont))    