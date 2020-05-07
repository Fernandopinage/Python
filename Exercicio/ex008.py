#escreva um codigo que leia um valor em metros e a exiba convertindo em centimetro e metros

numero = float(input('digite um valor para convertar '))

print('O numero digitado foi {} '.format(numero))
print ('O numero em KM {}'.format(numero / 1000))
print ('O numero em HM {} '.format(numero / 100))
print ('O numero em DAM {} '.format(numero / 10))
print ('O numero em METROS {}'.format(numero))
print ('O numero em DM {} '.format(numero * 10))
print ('O numero em CM {} '.format(numero * 100))
print ('O numero em MM {} '.format(numero * 1000))