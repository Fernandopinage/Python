# Desenvolva um programa que leia 6 numero inteiros e mostre a soma de todos os numeros pares 

soma = 0
cont = 0
for cont in range(1,7):
    num = int(input("Digite o numero: "))
    if (num % 2) == 0:
        soma = soma + num
print("Soma dos numeros {}:".format(soma))        