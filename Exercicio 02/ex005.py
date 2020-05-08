#faça um programa que leia nome de 4 alunos e mostre a ordem soteadas

import random

nome1 = str(input('Nome do primiero: '))
nome2 = str(input('Nome do segundo: '))
nome3 = str(input('Nome do terceiro: '))
nome4 = str(input('Nome do quarto: '))

lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)

print(lista)