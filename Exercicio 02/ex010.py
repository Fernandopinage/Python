#faça um programa que leia uma frase pelo teclado e mostre:
# * Quantas vezes aparece a letra "A"
# * Em que posição ela aparece a primiera vez 
# * Em que posição ela aparece pela ultima vez

frase = str(input("digite uma frase: ")).strip()

print ("A frase contem {} letras A".format(frase.count("a")))
print ("A letra 'A' aparece {}".format(frase.find("a")))
print ("A letra 'A' ultima {}".format(frase.rfind("a")))

