#cria um programa que leia o nome completo de uma pessoa e mostre
# * O nome com todas as letras maiusculas e minusculas 
# * Quantas letras ao todo (sem contarar com os espaços)
# * Quantas letras tem o primeiro nome
# * Criar um array de lista com nome digitado


nome = str(input('digite seu nome: ')).strip()

print (nome.upper())
print (nome.lower())
print (len(nome)- nome.count(" "))
print(nome.find(" "))
print (nome.split())
