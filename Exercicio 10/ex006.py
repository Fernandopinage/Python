# Aprimorando Desefio anterior para que ele funcione com varios jogadores 


lista = list()
jogador = dict()
gols = list()
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite seu nome: '))
    qtd = int(input('Quantas partidas o {} jogou?: '.format(jogador['nome'])))

    for i in range(0,qtd):
        gol = int(input("Quantos gols na partida {} ".format(i+1)))
        gols.append(gol)
        soma += gol
        jogador['gols'] = gols.copy()    
        jogador['total'] = soma
    lista.append(jogador.copy())


    opcao = str(input('Deseja continuar [S/N]?: ')).upper()
    if opcao == 'N':
        break
print("-*-"*15)
print(lista)