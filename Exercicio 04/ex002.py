# Faça um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão 
# 1 - binario
# 2 - octal
# 3 - hexadecimal


numero = int(input('Digite um numero para converter: '))

print('== '*8)
print('= 1 - Binario')
print('= 2 - Octal')
print('= 3 - Hexadecimal')
print('== '*8)

converter = int(input('Digite um numero: '))

if converter == 1:
    print('Sua base é Binaria {}'.format(bin(numero)[2:]))
elif converter == 2:
    print('Sua base é Octal {}'.format(oct(numero)[2:]))
elif converter == 3:
    print('Sua base é Hexadecimal {}'.format(hex(numero)[2:]))
else:
    print("Opção invalida")


