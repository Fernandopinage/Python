# Desenvolva um programa que leia 4 numeros de um teclado.
# A) Quantas vezes aparece o valor 9.       B) Em qual posição apareceu o valor 3
# C) Quais numeros foram Pares.

n1 = int(input('Digite o 1º numeoro: '))
n2 = int(input('Digite o 2º numeoro: '))
n3 = int(input('Digite o 3º numeoro: '))
n4 = int(input('Digite o 4º numeoro: '))
lista = (n1,n2,n3,n4)
print("Quantas vezes apareceu o valor 9 ? o valor apareceu {}".format(lista.count(9)))
if 3 in lista:
    print("Qual posição apareceu numero 3 ? foi na posição {}".format(lista.index(3)+1))
else:    
    print("Os numeros pares digitados foram ",end=" ")
for n in lista :
    if n % 2 == 0 :
        print(n,end=" ")
