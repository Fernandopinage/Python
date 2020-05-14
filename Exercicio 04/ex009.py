# Faça um programa que calcule o valor a se pagar por um produto, considerando seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto              - Em até 2X no cartão preço normal
# - À vista no cartao 5% desconto                         - 3x ou mais no cartão: 20% juros


valor = float(input('digite o valor das compras: '))

print(("="*7 )+" Luiz Fernando " +("="*7) )
print("1 - Dinheiro")
print("2 - Cartão")
print("3 - 2x no Cartão")
print("4 - 3x ou mais no Cartão")

compras = int(input('Digite forma de pagamento: '))

if compras == 1:
    total = valor - (valor * 10)/100
    print("O valor a pagar e de {}".format(total))

elif compras == 2:
    total =    valor - (valor * 5)/100 
    print("O valor a pagar e de {}".format(total))

elif compras == 3:
    total = valor / 2
    print("O valor das parcelas de 2x é {} sem juros".format(total))

elif compras == 4:

    total =  (valor + (valor * 20)/100)/4

    print("O valor das parcelas em 4x ficou de {}".format(total))

else:
    print("Opção invalidar ")