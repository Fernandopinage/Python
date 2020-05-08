#faça um programa que sortear um dos quatros alunos para apagar o quadro.
import random

nome1 = str(input('Digite o primiero nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))

lista = [nome1,nome2,nome3,nome4]

result = random.choice(lista)
print('O nome sorteado entre os alunos foi: {}'.format(result))