# Criei um programa que leia 7 valores e cadastre em uma lista. Que mantem separado de 'pares' de 'impares'. 

numero = [[],[]]
num = 0
for n in range(0,7) :
    num = int(input('Digite um valor: '))
    if num % 2 == 1:
        numero[0].append(num)
    else:
        numero[1].append(num)
numero[0].sort()
numero[1].sort()
print("Todos os impares {} ".format(numero[0]))
print("Todos os Pares {} ".format(numero[1]))

    