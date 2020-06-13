#


from random import randint

numero = int(input('Qauntos jogos você quer fazer ?:'))


lista = []
copia = []
for i in range(0,5):
    num = randint(1, 60)
    lista.append(num)
    lista.sort()
    copia.append(lista[:])
    lista.clear()    

for i in range(0,numero):
    print(copia)

