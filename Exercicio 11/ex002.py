# Faça um programa que tenha uma função chamada 'linha()'que recebar texto qualquer com um parametro. 


def linha(palavra):
    print('~'*len(palavra))
    print(palavra)
    print('~'*len(palavra))
    

linha(palavra = str(input('Digite um texto')))