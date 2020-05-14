# Faça um programa que mostre que tipo de triangulo e formado 

# Equilatero: Todos os lados iguais
# Isósceles: Dois iguais 
# Escolatero: Todos os lados diferente

t1 = int(input('digite primiero seguimento: '))
t2 = int(input('digite segundo seguimento: '))
t3 = int(input('digite terceiro seguimento: '))

if t1 < t2 + t3 and t2 < t3 + t1 and t3 < t1 + t2:
    print("Os seguimento acima pode forma Triangos")

    if t1 == t2 and t2 == t3 and t3 == t1:
        print ("Equilatero todos os lados são iguais")
    elif t1 != t2 != t3 != t1:
        print("Escolatero todos os lados são diferente")

    else:
        print("Isósceles dois dos triangulos sao iguais")   
else:
    print("Dados nao podem forma um triangulo")        