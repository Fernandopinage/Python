# Criar um programa onde 4 jogadores jogar um dado e tenha resultados aleatorios. Guarde esses resultados em um dicionario. Por fim mostrem eles ordenados

from random import randint
from time import sleep
from operator import itemgetter
ranking = dict()
jogador = {
            'jogador1': randint(1,6),
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)

            }
print(jogador)  
print("-=*=-"*12)          

for i,j in jogador.items():
    print("{} jogou dado tirou {}".format(i,j))
    sleep(1)
    ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print(ranking)   

for k,v in ranking :
    print("{} {}".format(k,v))