#

n1 = int(input("Digite o primiero valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
n5 = int(input("Digite o quinto valor: "))
maior= 0
menor = 0
lista = [n1,n2,n3,n4,n5]

print("Os valores digitados são {}".format(lista))
for n in lista :
    if n >= maior :
        maior = n
    else:
        menor = n

print("Maior valor digitado é {} na possiçao".format(maior),end=" ")
for i,v in enumerate(lista):
    if v == maior:
        print("{}...".format(i),end="")
print()     
for i,v in enumerate(lista):
    if v == menor:
        print("{}...".format(i),end="")
print()    
print('Menor valor digitado é {} na possiçao'.format(menor),end=" ")