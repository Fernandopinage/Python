from random import randint


def sortiar(lista):
    for cout in range(0,5):
        lista.append(randint(1,10))


def somarPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print('Os valores somados tem o resultado {} '.format(soma))        



numero = list()
sortiar(numero)
print(numero)
somarPar(numero)