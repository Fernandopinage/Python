# faça um programa que leia o ângulo qualquer e mostre na tela o valor "seno","cosseno" é "tangente" desse ângul.
import math

a = float(input('informe um ângulo: '))
seno = math.sin(math.radians(a)) # tem que converter para radino
cosseno = math.cos(math.radians(a)) # tem que converter para radino
tangente = math.tan(math.radians(a))
print ('O angulo tem o seno {:.2}'.format(seno))
print ('O angulo tem o cosseno {:.2}'.format(cosseno))
print ('O angulo tem o tangente {:.2}'.format(tangente))