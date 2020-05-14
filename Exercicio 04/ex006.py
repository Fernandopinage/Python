# cria um programa que leia um ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade
# - Até 9 anos: MIRIM               - Até 19 anos: JUNIOR
# - Até 14 anos: INFANTIL           - Até 25 anos: SÊNIO
# - Acima: MASTER

ano = int(input('digite ano de nascimento: '))

if ano <= 9:
    print("{}anos MIRIM: ".format(ano))
elif ano >=10 and ano <= 14 :
    print("{}anos INFANTIL: ".format(ano))
elif ano >=15 and ano <= 19:
    print("{}anos JUNIOR: ".format(ano))
elif ano >=20 and ano <=25:
    print("{}anos SÊNIO: ".format(ano))
elif ano>25:
    print("{}anos MASTER: ".format(ano))        

