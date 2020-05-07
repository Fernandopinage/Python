#faça um programa que leia o salario de um funcionario e atribui 15% de reajuste

salario = float(input('Digite a quantida do salario do servidor: '))
reajuste = int(input('informe a porcentagem do reajuste: '))
total = (salario * reajuste)/100

totalfinal = total + salario

print('O salario do servidor é {} com {} de reajuste da o total de {}'.format(salario,reajuste,totalfinal))