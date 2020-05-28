# Crie um programa que leia varios numeros e coloque em uma lista.
# A) Quantos numeros foram digitados        B) Listar em forma decrecente 
# C) Se o valor '5' foi digitado está ou nao listado 
numero = list()
cont = 0
cinco = False
while True:
    cont += 1
    n = int(input('Digite um valor: '))
    numero.append(n)
    r = str(input('Deseja continuar [S/N]')).upper()

    if r == 'N' :
        break
    elif n == 5 :
        cinco = True
    else:
        cinco = False

print("Total de valores digitados forem {} ".format(cont))
numero.sort(reverse=True)
print("Lista de numeros são {}".format(numero))
print("Contem o numero '5' na lista? {} ".format(cinco))