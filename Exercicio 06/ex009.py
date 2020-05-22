# Crie um programa que leia varios valores de um teclado.
# O programa só vai parar quando for digitado '999' que é a condição para finalizar, além disso deve mostra no final quantas vezes usuario digitou e somas dos numeros


cont = 0
soma = 0
numero = 0
while True:
    numero = int(input("Digite um numero: "))
    if numero == 999:
        break
    else:
        cont += 1
        soma += numero
print('A soma dos numeros é {} e quantidades de vezes que usaurio digitou {}'.format(soma,cont))