# Faça um programa que leia nome e peso de varias pessoas.
# A) Quantas pessoas foram Cadastradas      B) Uma lista com varias pessoas mais pesadas
# C) Uma lista com pessoas mais leves 


maior = 0
menor = 900
dados = []
temp = []
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if temp[1] >= maior:
        maior = temp[1]
    else:
        menor = temp[1]

    dados.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar ? [S/N]')).upper()
    if r in'Nn':
        break
    
print('=-'*30)
print(dados)
print('Total de registro é {}'.format(len(dados))) 
print('O maior peso é {}'.format(maior),end=" ")
for n in dados:
    if n[1] == maior:
        print("nome :{}".format(n[0])) 
    
print('O menor peso é {}'.format(menor),end=" ")
for n in dados:
    if n[1] == menor:
        print("nome :{}".format(n[0]))    
