# Crie um programa que verifica se o ano e bissexto

ano = int(input("Informe o ano que vc quer saber: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print("ano bissexo")

else:
    print("nao e bissexo")    