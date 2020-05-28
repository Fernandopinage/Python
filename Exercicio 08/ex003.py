# Crie um programa onde usuario possa digitar 5 valores numericos e cadastra-os em uma lista. ja na possição correta da inserção

numero = list()

for n in range(0,5):
    n = int(input("Digite um valor: "))
    numero.append(n)    
    numero.sort()
    print("Add na posição {}".format(numero.index(n)))

print(numero)