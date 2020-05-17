# Faça um programa que leia um numero e informe se ele e primo.


numero = int(input('Digite um numero: '))


for cont in range(1,numero +1):
    if numero % cont == 0:
        print('\033[32m',end=" ")
    else:
        print('\033[m',end=" ")
    print(cont, end=" ")