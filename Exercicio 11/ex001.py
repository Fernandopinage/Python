# faça um programa que tenha uma funçao com nome 'area()' que recebar uma dimensoes de um terreno retangular. 

def area(largura,comprimento):
    total = largura * comprimento
    print("Total de area é {}".format(total))
  

total = 0

print('-*-'*10)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura,comprimento)


