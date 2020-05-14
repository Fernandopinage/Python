# cria um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
# Media abaixo de 5.0 :Reprovado
# Media acima de 5.0 a 6.9 :Recuperação
# Media acima de 7.0 :Aprovado


nota1 = float(input('digite primeira nota: '))
nota2 = float(input('digite segunda nota: '))

media = nota1 + nota2 / 2

if media <= 5.0:
    print("Aluno tirou a nota {} e está REPROVADO".format(media))

elif media > 5.0 and media < 6.9 :
    print("Aluno tirou a nota {} e por isto se encontra na RECUPERAÇÂO".format(media))

elif media >= 7.0:
    print("Aluno tiroi a nota {} está APROVADO".format(media))

else:
    print("Nota invalida...")   