# Criei um programa onde o usuario possa digitar varios valores numericos e cadastra-os em uma lista caso numero ja exista nao vai ser cadastrado.

n = 0
numero = list()
while True :
    
    n = int(input('Digite um numero: '))
    if n not in numero :
        numero.append(n)
    else:
        print("Valor duplicado, nao vou adicionar")    
    r = str(input('Deseja continuar [S/N]')).upper()
    if r == 'N' :
        break
    
print("valor digitados foi {}".format(sorted(numero)))
    




