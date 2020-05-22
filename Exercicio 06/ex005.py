# Faça um programa que leia "primiero termo" e a "razão" de uma PA usando while



numero = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a razão: '))
total = numero
n = 10

while n >= 1:
    
    total = total + razao
    print(total ,end=' ')
    n -=1