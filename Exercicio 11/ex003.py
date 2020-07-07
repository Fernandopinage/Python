
from time import sleep

def contagem(n):
    for i in range(1,n+1):
        print(i,end=" ",flush=True)
        sleep(0.5)    



def regressiva(n):
    for i in range(n,0,-1):
        print(i,end=" ",flush=True)
        sleep(1)


def escolha(n,f,v):
    for i in range(n,f,-v):
        print(i,end=" ",flush=True)
        sleep(1.5)

contagem(10)
print("\n")
regressiva(10)
print("\n")
escolha(n=7,f=2,v=1)
