# faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro nome e ultimo nome separados


nome  = str(input('digite seu nome completo: ')).strip()

nome = nome.split()
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu primeiro nome é {}".format(nome[len(nome)-1]))