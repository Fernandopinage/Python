# Faça um programa que leia um salario de um funcionario e calcule o valor de seu aumento.
#  Para o salario superiores à 1.250, calcule o aumento de 10% para inferiores ou iguais o aumento e de 15%

salario = float(input("informe o salario do funcionario: "))

if salario <= 1250 :
    reajuste = salario + (salario * 15 / 100)
    print("O salario do funcionario com o reajuste é de {:.2f}".format(reajuste)) 
else:
    reajuste = salario + (salario * 10 / 100)
    print("O salario do funcionario com o reajuste é de {:.2f}".format(reajuste)) 