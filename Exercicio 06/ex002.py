# Crie um programa  que o jogador tente adivinha qual numero a maquina escolheu, no final mostre quantas tentativas foram necessaria para acerta

from random import randint

num = randint(1,10)
cont = 1
numero = int(input('informe um numero que vc achar que maquina escolheu: '))

while num != numero:
    if numero < num:
        numero = int(input('Você errou tente de novo com numero maior: '))
        cont = cont + 1
    else:
        numero = int(input('Você errou tente de novo com um numero menor: '))
        cont = cont + 1
print("Parabens voce acertou com {} tentativas, o numero que maquina escolheu foi {}".format(cont,num))            