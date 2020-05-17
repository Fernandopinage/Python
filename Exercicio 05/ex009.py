# cria um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sãodatetime A combination of a date and a time. Attributes: ()
from datetime import date
data = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    idade = int(input('Digite a idade {}º '.format(i)))
    total = data - idade
    if total >= 18:
        maior = maior + 1
    else:
        menor = menor +1
print("menor {},maior {}".format(menor,maior))
