#faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tintas necessario 
#para pintá-lo, sabendo que cada litro de tinta, pinta uma area de 2m²


largura = float(input("informe quantos metros de largura: "))
altura = float(input("informe altura: "))

area = largura * altura
print ("Sua parede tem o diametro de {}x{} e sua area e de {}m²".format(altura,largura,area))
total = area /2
print ("quantidade de tinta para pinta a parede é: {}L".format(total))