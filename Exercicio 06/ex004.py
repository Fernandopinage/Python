# Crie um programa que faça fatorial de um numero no final mostre todos os numeros fatorados e sua mutiplicação

n = int(input('digite um numero para fatora: '))
f = 1
while n != 0 :
    print(n,end=" ")
    f = f*n
    n = n-1
print("Fatorial do numero {} é {}".format(n,f))
    