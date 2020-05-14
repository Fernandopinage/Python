# Faça um programa que tire IMC 

peso = float(input('informe o seu peso: '))
altura = float(input('infome sua altura: '))

imc = peso/(altura**2)


if imc < 18.5:
    print("Abaixo do peso")

elif imc >= 18.5 and imc <= 25:
    print ("Peso ideal")

elif imc >= 25 and imc <= 30:
    print("Sobre peso")

elif imc >= 30 and imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")
else:
    print("Erro")        