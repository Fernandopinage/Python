def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            
        else:
            print('\033[0;31m Erro nao e numero\033[m')    
        if ok:
            break    
    return valor    




n = leiaInt("Digite um numero: ")
print(n)