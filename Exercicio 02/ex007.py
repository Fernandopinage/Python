#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada digito separados.


numeiro =  int(input('digite um numero entre 0 a 9999: '))
num = str(numeiro)

print ('Unidade {}'.format(num[3]))
print ('Dezenas {}'.format(num[2]))
print ('Centena {}'.format(num[1]))
print ('Milhares {}'.format(num[0]))