# Crie um programa que leia nome, idade, sexo de varias pessoas.
# A) quantas pessoas cadastradas    B) A media de idade das pessoas
# C) Uma lista de mulheres          D) Uma lista de pessoas acima da media


pessoa = dict()
lista = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Digite seu nome: ')).upper()
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Digite seu sexo [M/F]: ')).upper()
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('Erro sexo nao indentificado')
        else:
            break
    lista.append(pessoa.copy())  
    res = str(input('Deseja continuar? [S/N]:')).upper()
    if res == 'N':
        break
  
print('Total de pessoas cadastradas {}'.format(len(lista)))
print('A media de idade das pessoas é {}'.format(soma / len(lista)))
print('Total de mulheres cadastradas ', end=" ")
for p in lista:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=" ")
print()
print('A lista de pessoas acima da media {}',end="")
for p in lista:
    if p['idade'] >= soma /len(lista):
        print('     ') 
        for k,v in p.items():
            print('{} = {}'.format(k,v),end=" ")
            print()
print()             
