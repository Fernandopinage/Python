# Crie uma tupla preenchar com os 20 primeiros colocado da tabela do brasileirao.
# A) Os 5 primeiros colocados       B) Os ultimos 4 colocados       
# C) Time em ordem alfabetica       D) Em qual posição está o time da chapecoense.

times = ("Flamengo","Santos","Palmeiras","Grêmio","Athletico-PR","São Paulo","Internacional","Corinthians","Fortaleza EC","Goiás",
"Bahia","Vasco da Gama","Atlético-MG","Fluminense","Botafogo","Ceará","Cruzeiro","CSA","Chapecoense","Avaí",)

print("=-"*30)
print(" "*15)
print("Os 5 primeiro lideres do Brasileirao {}".format(times[0:5]))
print(" "*15)
print("=-"*30)
print(" "*15)
print("Os 4 ultimos do Brasileirao {}".format(times[-4:]))
print(" "*15)
print("=-"*30)
print(" "*15)
print("Os times em ordem alfabetica {}".format(sorted(times)))
print(" "*15)
print("=-"*30)
print(" "*15)
print('Qual posição do time da chapecoese {}'.format(times.index("Chapecoense")+1))
print(" "*15)
print("=-"*30)