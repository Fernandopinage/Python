# Escreva um programa que leia dos numero inteiros e compare-os mostrando a tela da mensagem
# - O primeiro numero e maior que o segundo 
# - O segundo numero e maior que o primeiro
# - Os 2 numeros sao do mesmo valor 

n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))


if n1 > n2:
    print("O numero {} é maior que {}".format(n1,n2))

elif n2 > n1:
    print("O numero {} é maior que {}".format(n1,n2))

elif n1 == n2:
    print("Os dois numeros tem o mesmo valor")   

else:
    print("numero invalido ")