# Faça um programa que leia o peso de 5 pessoas. No final mostre o maior e menor peso.
maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('digite seu peso: '))
    if peso >maior:
        maior = peso
    else:
        menor = peso

print("O Maior peso é {}, logo o menor peso é {}".format(maior,menor))            