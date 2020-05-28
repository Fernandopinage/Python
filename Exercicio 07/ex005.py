# Criar um programa que tenha uma unica tupla com nome de produtos e seu respectivos preços. organizando os em forma de tabuada.


lista  = (
    'lapis',1.05,
    'grafite',3.75,
    'pont 0,10',0.50,
    'ponta 0.7',0.50,
    'borracha',2.25,
    'carderno',10.55,

)
print("=-"*20)
print(10*" "+"LISTA DE PRODUTOS")
print("=-"*20)
for i in range(0,len(lista)):
    if i%2 == 0 :
        print("{:.<30}".format(lista[i]),end="")
    else:    
        print("{:>10}".format(lista[i]))