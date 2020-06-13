# Faça um programa que leia nome, media de um aluno, guardando tambem a situação em digionario. no final, mostre o conteudo da estrutura.


aluno = dict()

aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua media: '))
if aluno['media'] <5 :
    aluno['situacao'] = "reprovado"
elif 5>= aluno['media'] <7:
    aluno['situacao'] = "recuperacao"
else:
    aluno['situacao'] = "Aprovado"

print("=-="*7)
print(aluno)
print("=-="*7) 

for k,v in aluno.items():
    print('{} - é igual {}'.format(k,v))