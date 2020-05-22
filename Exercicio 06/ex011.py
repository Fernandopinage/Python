# crie um programa que leia idade e sexo de varias pessoas. A cada pessoa cadastrada o programa devera perguntar se usuario que ou nao continuar.Por fim o programa devera mostra.
# - A) quantas pessoas tem mais de 18 anos             - B) quantos homens foram cadastrados
# - C) quantas mulheres tem menos de 20 anos 


maior = 0
menor = 0
homen = 0
mulher = 0
cont = 0
print("=-"*20)
print(" "*7+ "Vamos cadastra uma pessoa")
print("=-"*20)
while True:
    print("--"*20)
    idade = int(input('idade: '))
    sexo = str(input('sexo: [M/F]')).upper().strip()
    print("--"*20)
    opcao = str(input('Quer continuar?: [S/N]')).upper().strip()
    if idade >= 18 :
        cont += 1
    if opcao == 'N':
        break
    else:
        if sexo == 'M':
            homen += 1
        else:
            if idade <= 20 :
                mulher += 1
print("Total de pessoas com a idade acima de 18 é {}".format(cont))
print('Quantas mulheres tem menos de 20 anos {}'.format(mulher))
print("Quantos homens foram cadastrados, total {}".format(homen))
