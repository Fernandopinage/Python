# faça um programa que leia o comprimento do cateto oposto e cateto adjacentes de um triangulo retangulo 
#calcule  e mostre o comprimernto da hipotenusa

#import math #importando a função "matematica"
from math import *
oposto = float(input('digite o cateto oposto'))
adjacente = float(input('digite o cateto adjacente'))

result = hypot(oposto,adjacente)
print("O resultando {:.2}".format(result))
