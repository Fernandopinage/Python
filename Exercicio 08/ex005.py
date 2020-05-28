# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso crie 2 lista extras que vao conter numeros PAR e IMPAR.

par = list()
impar = list()
numero = list()
while True:
    n = int(input('Digite um valor: '))
    numero.append(n)
    r = str(input('Deseja continuar [Y/N]')).upper()
    if r == 'N' :
        break
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print("A lista total é {}".format(numero))
print("Valores Pares total é {}".format(par))
print("Valor impar total é {}".format(impar))    