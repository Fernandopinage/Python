# Faça um programa que leia um sexo de uma pessoa.Mas só aceite o valor 'M' ou 'F'. caso esteja errado, peça para digitar novamente

sexo = str(input('Digite seu sexo: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Datos invalidos. Por favor, informe seu sexo: ')).upper()
print('Obrigado seu Sexo é {}'.format(sexo))