# Criei um algoritimo que leia uma matris 3x3

matris = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input("Digite um valor {}, {}: ".format(l,c)))

for l in range(0,3):
    for c in range(0,3):
        print(matris[l][c],end="")
    print()