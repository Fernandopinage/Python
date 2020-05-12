# Escreva um programa para aprovar um emprestimo bancario a compra de uma casa. 
# Pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# A prestação mensal, nao pode exceder 30% do salario ou entao o emprestimo será negado

casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o valor do salario: "))
emprestimo = int(input("Quantos anos você quer pagar: "))

prestação = casa / (emprestimo * 12)
print ("Para pagar uma casa de {:.2f} em {} anos".format(casa,emprestimo))
print("A prestação sera de {:.2f}".format(prestação))
mediaSalario = (salario * 30)/100
print (mediaSalario)

if prestação <= mediaSalario:
    print ("emprestimo Realizado com sucesso")

else:
    print("emprestimo Negado !")    