# Crie um programa que leia nome do protudo e seu preço. O programa devera pergunta se o usuario deseja continuar e mostre.
#  - A) Qual total de gasto na compra               - B) Quantos produtos custam mas de 1000 reais
#  - C) Qual nome do produto mais barato
# 
nome = 0
total = 0
menor = 0
cont = 0
print("=-"*20)
print(" "*7+ "Comprar produto")
print("=-"*20)
while True :
    produto = input('Digite nome do produto: ')
    preco = int(input('Valor do produto: '))
    opcao = input('Deseja continua? [S/N] ').upper()   
    if preco >= 1000 :
        cont = cont + 1
        nome = produto
    elif menor <= preco :
        menor = preco
   
    total = total + preco   
    if opcao == 'N':
           break    
print('Total de gasto é {}'.format(total))
print('O produto mais barato é {}R$'.format(menor))
print('Quantos produtos passaram de 1000 reais {}, {}'.format(cont,nome))
