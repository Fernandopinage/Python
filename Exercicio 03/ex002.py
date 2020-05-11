#Escreva um programa que leia a velocidade de um carro se ele altrapassar 80km/h mostre um messagem dizendo que foi multado. A multa vai custar R$7,00 por cada km acima do limite.


velocidade  = float(input("informe a velocidade do carro: "))

if velocidade <= 80:

    print("dirija com cuidado")

else:
    print("Você está correndo muito sua velocidade é {}".format(velocidade))
    print("Você recebeu uma multa de {}R$".format((velocidade - 80) *7))        