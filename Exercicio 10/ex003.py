# Faça um programa que leia nome ano de nascimento e carteira de trabalho, 
# e cadastre-os em uma digionario se carteira de trabalho for diferente de 0 pergunte ano de contratação é salario.

from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = int(input('Digite ano de nascimento: '))
pessoa['ctps'] = int(input('Numero da carteira de trabalho: '))
if pessoa['ctps'] == 0:
    pessoa['idade'] = datetime.now().year - pessoa['idade'] 
    print (pessoa)
else:
    pessoa['idade'] = datetime.now().year - pessoa['idade'] 
    pessoa['ano'] = str(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario R$: ')) 
    print(pessoa)   

for k,v in pessoa.items():
    print(' - {} tem o valor {}'.format(k,v))   