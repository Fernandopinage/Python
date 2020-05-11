# Faça um programa que leia três numeros mostre qual e o maior e qual e o menor.

n1 = int(input("Digite o primiero numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2:
    menor = n2
    maior = n1

if n1 > n3:
    maior = n1
    menor = n1

if n2 > n1:
    maior = n2 
    menor = n1

if n2 > n3:
    maior = n2 
    menor = n3    

if n3 > n1:
    maior = n3 
    menor = n1


if n3 > n2:
    maior = n3 
    menor = n2


print("O maior valor é {}, o menor valor é{}".format(maior,menor))    