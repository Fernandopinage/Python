# Faça um programa que tenha uma função com nome de vota() que vai receber como paramentro o ano de nascimento de uma pessoa, retornando o valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleiçoes 
from datetime import date

def voto(id):
    data = date.today().year
    result = data - id
    if result >= 18 :
        return "Voto OBRIGATORIO"
    elif result == 17:
        return "Voto OPCIONAL"    
    elif result <= 16:
        return "Voto NEGADO"

idade = int(input("Digite o ano de nascimento: "))

print(voto(idade))