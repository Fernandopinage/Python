def jogo(nome=0,gols=0):
    if nome == 0:
        return print("O jogador desconhecido",end="")
    else:
        return print("O jogador {}".format(nome),end="")    
    if gols == 0:
        return print(' não fez gols')
    else:
        return print(" fez total de {} ".format(gols))    



nome = str(input('Digite nome do jogador: '))
gols = int(input('Digite quantidade de gols: '))
jogo(nome,gols)