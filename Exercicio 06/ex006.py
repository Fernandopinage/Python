# Criar um programa que resolva a seguencia de fibonacci


n = int(input('Digite quantos termos vc quer mostrar? '))
total = 0
t1 = 1
while n >= 1 :
    
    print(total,end=' ')
    
    total += 1
    total *= t1
    n = n -1