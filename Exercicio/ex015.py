#escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado.
#calcule  o preço a pagar , sabendo que o carro custa R$60 por dia e R$0,15 por KM  rodado.

aluguel = float(input('quantos dias o carro foi alugado: '))
km = float(input('quantos KM rodados: '))



todaldias = (60 * aluguel) + (km * 0.15)




print ('todal de valor a pagar {}'.format(todaldias))
