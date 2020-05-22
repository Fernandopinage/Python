# Crie um programa que leia vários números inteiros pelo teclado.No final mostre a media desses numeros e mostre qual e maior e qual e menor valores lidos. O programa deve pergunta se o usuario deseja continuar

maior = 0
menor = 0
soma = 0
cont = 0
auxi = True

while auxi :
    numero = int(input("Digite um numero: "))
    cont = cont + 1
    soma = soma + numero
    if numero > maior :
        maior = numero
    else:
        menor = numero
    variavel = str(input("Deseja continuar [N/Y]")).upper().strip()
    if variavel == 'N':
        auxi = False
print("O maior numero digitado foi {} é o Menor numero foi {} a Media dos numeros foi {:.2} ".format(maior,menor,soma/cont))

    
