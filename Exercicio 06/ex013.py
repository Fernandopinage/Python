# Crie um programa que simule o funcionamento de um caixa eletronico 


cem = 0
c = 0
v = 0
d = 0
ci = 0
do = 0
dinheiro = float(input('Digite o valor do saque: '))

print('Total do dinheiro que vc quer sacar {}'.format(dinheiro))
while True:
    if dinheiro >= 100:
        cem = cem + 1
        dinheiro = dinheiro - 100
    elif dinheiro >= 50:
        c = c + 1
        dinheiro = dinheiro - 50 
    elif dinheiro >= 20:
        v = v + 1
        dinheiro = dinheiro- 20    
    elif dinheiro >= 10:
        d = d + 1
        dinheiro = dinheiro - 10  
    elif dinheiro >= 5:
        ci = ci + 1
        dinheiro = dinheiro - 5
    elif dinheiro >= 2:
        do = do + 1
        dinheiro = dinheiro - 2         
    elif dinheiro == 0 :
        break     
print('Total de notas de 100,  {}'.format(cem))
print('Total de notas de 50,  {}'.format(c))
print('Total de notas de 20,  {}'.format(v))
print('Total de notas de 10,  {}'.format(d))
print('Total de notas de 5,  {}'.format(ci))
print('Total de notas de 2,  {}'.format(do))

