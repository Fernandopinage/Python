# criar uma tupla com varias paravras e mostre suas vogais 

lista = (
    'django python',
    'laravel php',
    'rest javascript',
    'freeMarker java'
    )


for i in range(0,len(lista)):
    print("\nNa palavra {} temos".format(lista[i],end=""))
    for letra in lista:
        if letra.lower()in 'aeiou':
            print(letra, end="")
    