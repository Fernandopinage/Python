# Aprimore o desafio aterior, mostrando no final
# A) A soma de todos os valores pares digitados     B) A soma dos valores da terceiras coluna 
# C) O maior valor da matriz da linha 2

soma = 0
soma2 = 0
maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz [i][j] = int(input('Digite um valor para {},{} : '.format(i,j)))

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0 :
            soma = soma + matriz[i][j]


for j in range(0,3):
    
    if matriz[1][j] >= maior :
        maior = matriz[1][j]

for i in range(0,3):
    soma2 += matriz[i][2]     


for l in range(0,3):
    for c in range(0,3):
        print(matriz[l][c],end=" ")
    print()


print('Soma dos valores pares é {} '.format(soma))
print('O maior valor da matriz da linha 2 é {}'.format(maior))
print('A soma dos elementos da 3 coluna é {}'.format(soma2))