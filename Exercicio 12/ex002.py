# Faça um programa que leia um numero e depois faça um fatorial

def fatorial(x,show=False):
    
    f = 1
    for i in range(x,0,-1):
        f *= i
        if show:
            print(i,end=" ")
    print("{}".format(f))  

fatorial(5,True)