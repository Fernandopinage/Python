#cria um programa que leia um valor em dinheiro real, é converta para dólar

dinheiro  = float (input('qual o valor que deseja converter R$ '))

dolar = dinheiro / 3.27

print ('Seu dinheiro R$ {:.2f} convertendo para EU$ {:.2f}'.format(dinheiro,dolar))

