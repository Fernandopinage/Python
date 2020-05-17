# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A media de idade do grupo             - Quantas mulheres tem menos de 18 anos.
# - Qual nome do homem mais velho.         

Maior = 0
menor = 0
media = 0
nomevelho = ""
nomenova = ''

for i in range(1,5):
    nome = str(input('Digite nome da {}º pessoa: '.format(i))).strip()
    idade = int(input('Digite a idade da {}º pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}º pessoa: '.format(i))).strip()
    if sexo == 'm':
        if Maior < idade:
            Maior = idade
            nomevelho = nome
    else:
        if idade < 18:
           menor = idade 
           nomenova = nome
           
    media = media + idade

print("A media de idade entre as pessoas é {}".format(media/i))
print("O Pessoa mascolina com maior idade {} com nome {} ".format(Maior,nomevelho))
print("A mulher com menor idade é {} tem nome {}".format(menor,nomenova))


