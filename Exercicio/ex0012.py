#cria um programa que leia o preço de um produto e mostre seu preço, com desconto de 5%

preco = float(input('Digite o preço atual: '))
desconto = int(input('informe o valor do desconto: '))
total = preco - (preco * desconto / 100)

print('O valor do preço {} com {} desconto, dá o total de {}'.format(preco,desconto,total))