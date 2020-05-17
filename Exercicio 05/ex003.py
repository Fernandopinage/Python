# Faça um programa que calcule a soma entre os numeros inpas que são multiplos de 3 e que se encontra no intervalo de 1 ate 500

cont = 0
soma = 0
for num in range(1,500,2):
    if num % 3 == 0 :
        soma = soma + num
        print(soma)
        cont = cont + 1
        print(cont)
        