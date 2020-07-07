# faça um programa que tenha uma funçao chamada maior() que receba varios parametros com o valores inteiros. Seu programa tem que analiza todos os valores e dizer qual e o maior.
from time import sleep

def maior(*n):

    cont = m = 0
    print("*-*-"*len(n))
    for i in n:
        print(i, end=" ",flush=True)
        sleep(1)
        if i >= m:
            m = i
        cont += 1    
        
    print("O total de valores {}, é maior valor é {} ".format(cont,m))    


maior(1,2,3,4,5,6,7)
print()
maior(23,22,88,64,1,15)