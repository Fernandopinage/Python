# crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. depois vai ler a quantidade de gols feitos em cada partida.
# No final tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato


print("-==- "*10) 
gols = list()
jogador = dict()
soma = 0
jogador['nome'] = str(input('Digite nome do jogador: '))

cont = int(input('Quantas partidas {} ele fez? :'.format(jogador['nome'])))

for i in range(0,cont):
    partidas = int(input('Quantos gols na partida ?: '))
    soma += partidas
    gols.append(partidas)
    jogador['gols'] = gols
    jogador['total'] = soma

print("-==- "*10)    

for k,v in jogador.items():
    print("{} tem valor {} ".format(k,v))

print("-==- "*10) 

print("O jogador {} jogou {} partidas ".format(jogador['nome'],cont))

for i in range(0,cont):
  print("Na partida {}, fez {} gols".format(1,jogador['gols'][i]))