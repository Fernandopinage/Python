# Crie um programa que leia uma frase qualquer e diga se ela é uma palindromo, desconsiderando os espaços

frase = str(input("Digite uma frase: ")).strip().upper()
palavra =   frase.split()
juntar = "".join(palavra)
inverso = juntar[::-1]
print(juntar,inverso)
if juntar == inverso:
    print("temos um palimetro")
else:
    print("nao e um palimetro")    