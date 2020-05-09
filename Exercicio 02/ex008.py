#crei um programa que leia nome de uma cidade e diga se ela começa ou nao com o nome de "santo"


cidade = str(input("digite nome da sua cidade: ")).strip()
variavel = cidade.upper()
print("sua cidade {} está {}".format(variavel,variavel[:5] == "SANTO"))