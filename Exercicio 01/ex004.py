#faça um programa que leia algo pela teclado e mostre na tela seu tipo primitivo e todos as informações possiveis sobre ela.

telcado = input('informe alguma coisa ')

print('tipo primitivo é ?',type(telcado))
print('Só tem espaço? ',telcado.isspace())
print('É um numero ?', telcado.isnumeric())
print('É uma letra ? ', telcado.isalpha())
print('É uma letra ou numero ? ', telcado.isalnum())
print('Contem letras maiúsculas ? ', telcado.isupper())
print('Contem so letras minusculas ?', telcado.islower())
