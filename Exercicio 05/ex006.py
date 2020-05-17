# Desenvolva um programa que leia o primeiro termo ea razão de uma P.A no final. mostre os 10 primeiro termos dessa progressão


print("**"*10)
print(" "*8,"P.A")
print("**"*10)

primeiro = int(input("Primiero termo: "))
razao = int(input("razao:"))
decimo = primeiro +(10 - 1)*razao
for num in range(primeiro,decimo+razao,razao):
    print(num, end="->")